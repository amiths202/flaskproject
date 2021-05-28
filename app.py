from flask import Flask, json,render_template,request,redirect,url_for
# 
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
# 

app = Flask(__name__)

#
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dbapplication'
app.config['MYSQL_PASSWORD'] = 'XpVT@ivNb0N7w.3@'
app.config['MYSQL_DB'] = 'applicationusers'
mysql = MySQL(app) 

# 


@app.route('/', methods= ["GET","POST"])
def home():
	return render_template('home.html')




@app.route('/adhd_adult', methods = ["GET","POST"])
def adhd_adult():
	
	if request.method == "POST":
		age = request.form['age']
				
		q = []
		for i in range(18):
			q.append(request.form[str(i+1)])
			
		res = 0
		for i in range(18):
			if q[i] == "Rarely":
				res+=1
			elif q[i] == "Sometimes" :
				res+=2
			elif q[i] == "Often" :
				res+=3
			elif q[i] == "Always" :
				res+=4
		
		data = { "value" : res , "total" : 64 }

		# 
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('INSERT INTO priliminary_test VALUES(NULL,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(age,q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9],q[10],q[11],q[12],q[13],q[14],q[15],q[16],q[17]))
		mysql.connection.commit()

		# 

		return render_template("result.html",data=data)
	return render_template("adhd_adult.html")


@app.route('/comprehensive_test')
def comprehensive_test():
	return render_template('comprehensive_test.html')


@app.route('/adhd_children', methods = ["GET","POST"])
def adhd_children():

	if request.method == "POST":
		age = request.form['age']
		q = []
		res = 0
		for i in range(10):
			q.append(request.form[str(i+1)])
		for i in range(10):
			if q[i] == "Sometimes":
				res+=1
			else :
				res+=2
		data = { "value" : res , "total" : 20 }
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('INSERT INTO children_preliminary_test VALUES(NULL,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(age,q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9]))
		mysql.connection.commit()
		return render_template("result.html", data=data)
	return render_template('adhd_children.html')


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/result')
def result():
	return render_template('result.html')


if __name__=="__main__":
	app.run(debug=True)