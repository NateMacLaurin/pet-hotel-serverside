from flask import Flask
from flask import request
from flask import jsonify
import flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=pet_pie_hotel")

cur = conn.cursor()

@app.route('/', methods=['GET'])
def dbtest():
    cur.execute('SELECT * FROM owners')
    return jsonify(cur.fetchall())

if __name__ == "__main__" :
    app.run(debug=True)