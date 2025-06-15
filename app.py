from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        return "Login successful"
    else:
        return "Invalid credentials"

if __name__ == "__main__":
    app.run(debug=True)
