from flask import Flask, render_template, request, redirect
from db_config import get_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)  # Debug print
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        address = request.form['address']
        phone = request.form['phone']
        aadhaar = request.form['aadhaar']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, dob, gender, address, phone, aadhaar_number) VALUES (%s, %s, %s, %s, %s, %s)",
                       (name, dob, gender, address, phone, aadhaar))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_user.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    conn = get_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        address = request.form['address']
        phone = request.form['phone']
        aadhaar = request.form['aadhaar']

        cursor.execute("UPDATE users SET name=%s, dob=%s, gender=%s, address=%s, phone=%s, aadhaar_number=%s WHERE id=%s",
                       (name, dob, gender, address, phone, aadhaar, id))
        conn.commit()
        conn.close()
        return redirect('/')
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()
    conn.close()
    return render_template('update_user.html', user=user)

@app.route('/delete/<int:id>')
def delete_user(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)