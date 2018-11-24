from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
import sqlite3 as db

app = Flask(__name__)
 

# Working chart example for 2nd beach, Fixed Date.
@app.route("/")
def chart():
	conn = db.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	for l in labels:
		values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Nahant'").fetchall()
		dates = l[5:]
		print(dates)
# 	# values = [10,9,8,7,6,4,7,8]
		return render_template('chart.html', values=values, dates=dates)

# chart()
if __name__ == '__main__':
	app.run(debug=True)