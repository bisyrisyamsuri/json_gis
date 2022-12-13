from ast import keyword
from unittest import result
from flask import Flask, request
from flask_mysqldb import MySQL
from flask import jsonify
import yaml

# access image with url /galeri/file_name.jpg
app = Flask(__name__, static_folder='galeri')

db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/futsal', methods=['GET'])
def futsal():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM tbl_futsal")
    if result > 0:
        futsal = cur.fetchall()
        return jsonify({'Data':futsal},200)

@app.route('/detail/<detail_id>', methods=['GET'])
def detail_by_id(detail_id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM tbl_futsal where id = %s", [detail_id])
    if result > 0:
        detail = cur.fetchone()
        return jsonify({'data': detail}, 200)
    
if __name__ == '__main__':
    app.run(debug=True)