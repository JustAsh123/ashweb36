from flask import Flask, render_template,session,redirect, url_for, flash,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key = "82ju41udh18184jfdu19"
app.config["SQLAlchemy_DATABASE_URI"] = "sqlite:///info.sqlite3"

db=SQLAlchemy(app)

class info(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))
	city = db.Column(db.String(100))
	age = db.Column(db.Integer)

	def __init__(self,name,email,city,age):
		self.name = name
		self.email = email
		self.city = city
		self.age = age 

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/view")
def view():
	return render_template("view.html", values=info.query.all())

@app.route("/info", methods=["POST","GET"])
def user():
	if request.method =="POST":
		name = request.form["nm"]
		email = request.form["em"]
		city = request.form["ct"]
		age = request.form["ag"]
		usr = info(name,email,city,age)
		db.session.add(usr)
		db.session.commit()
		return render_template("thank.html")
	else:
		return render_template("info.html")

if __name__ == '__main__':
	db.create_all()
	app.run(host="0.0.0.0", debug=True)