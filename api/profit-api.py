from flask import Flask, render_template
import sqlite3
import sqlite3
from flask_cors import CORS  
import json

app = Flask(__name__)
CORS(app)

def get_user_data(user_id):
    conn = sqlite3.connect("SeniorProject.db")
    cursor = conn.cursor()
    cursor.execute("SELECT FirstName, LastName, Email, PhoneNumber FROM user WHERE ID = ?", (user_id,))
    data = cursor.fetchone()
    conn.close()
    if data:
        return {
            "FirstName": data[0],
            "LastName": data[1],
            "Email": data[2],
            "PhoneNumber": data[3]
        }
    else:
        return None

@app.route("/profile")
def profile():
    user_data = get_user_data(user_id=1)  
    if not user_data:
        return "User not found", 404
    return render_template("profile.html", user=user_data)  
if __name__ == "__main__":
    app.run(debug=True)
