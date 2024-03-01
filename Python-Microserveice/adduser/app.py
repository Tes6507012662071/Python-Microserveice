from flask import Flask, request, render_template, redirect, jsonify
import mysql.connector as mysql

conn = mysql.connect(
    host = "localhost",
    user = "root",
    password = "12345678",
    port = 3306,
    database = "my_memo"
)

app = Flask(__name__)

@app.route('/postuser', methods=["POST"])
def post_user():
    response = request.get_json()
    firstname = response['firstname']
    lastname = response['lastname']
    email = response['email']
    
    cur = conn.reconnect()
    cur = conn.cursor()
    sql = "INSERT INTO memo(firstname, lastname, email) "
    sql += " VALUES(%s, %s, %s)"
    data = (firstname, lastname, email)
    cur.execute(sql,data)
    conn.commit()
    conn.close()
    return redirect('http://localhost:5003/getuser')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)