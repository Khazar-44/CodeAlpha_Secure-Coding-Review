from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    if result:
        return "Login successful"
    else:
        return "Invalid credentials"

if __name__ == "__main__":
    app.run(debug=True)
