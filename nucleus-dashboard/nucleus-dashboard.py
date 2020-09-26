from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'appDbSandbox'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/template.html")
def template():
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO messageLogTable (channelId, origin, message, status) VALUES ('twitter', '192.168.1.24', 'testMessage', 'test');")
    mysql.get_db().commit()
    cur.close()
    return render_template('template.html')

@app.route("/template1.html")
def template1():
    cur = mysql.get_db().cursor()
    cur.execute("select id, channelId, origin from messageLogTable;")
    results = cur.fetchall()
    print("Type of results: ", type(results))
    cur.close()
    return render_template('template1.html', data=results)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1024)
