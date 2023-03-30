import pickle
from flask import Flask, request, render_template
import mysql.connector as sqltor
mycon = sqltor.connect(host = "localhost", user = "root", passwd = "SI_nd_HU_24", database = "ml")
cursor = mycon.cursor()

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def login():
    
    username = request.form.get("username")
    password = request.form.get("password")
    cursor.execute("select * from user_details")
    if (username, password) in cursor.fetchall():
            return render_template("model.html")
    return render_template("signIn.html")

@app.route("/signUp", methods = ["POST"])
def signUp():
    
    username = request.form.get("username")
    password = request.form.get("password")
    cursor.execute("insert into user_details values('{}','{}')".format(username, password))
    mycon.commit()
    return render_template("login.html")

@app.route("/model", methods = ["POST"])
def model():
    
    features = [float(i) for i in (request.form.values())]
    model = pickle.load(open('regression_model.pkl','rb'))
    pred = model.predict([features])
    return render_template("success.html",data = round(pred[0],3))
    
if __name__ == "__main__":
    app.run(host = "localhost", port = 5000)