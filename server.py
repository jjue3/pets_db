from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('pets')
    petdata = mysql.query_db('SELECT * FROM pets;')
    print(petdata)    
    return render_template("index.html", petdata= petdata)

@app.route("/createpet", methods=['POST'])
def create_pet():
        mysql = connectToMySQL('pets') 
        data = {
                "name": request.form["name"],
                "type": request.form["type"],
        }
        query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());"
        petdata = mysql.query_db(query, data)
        print(request.form)
        return redirect('/')
if __name__ == "__main__":
        app.run(debug=True)
