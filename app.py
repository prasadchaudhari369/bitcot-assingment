from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="bitcotdb.cdsqkummgaz5.us-east-1.rds.amazonaws.com",
    user="authuser",
    password="Bitcot2024",
    database="db1",
)

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])


def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Insert data into the database
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        return 'Data submitted successfully.'
if __name__ == '__main__':
    app.run(debug=True)
