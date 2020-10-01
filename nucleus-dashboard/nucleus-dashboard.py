from flask import Flask, render_template
from flaskext.mysql import MySQL
import time


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'appDb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    ts = str(int(time.time()))

    jsInclude = '<script src="/static/js/scripts.js?t='+ts+'"></script>'
    jsInclude += '<script src="https://kit.fontawesome.com/7daabcbab0.js" crossorigin="anonymous"></script>'
    
    cssInclude = '<link rel="stylesheet" href="static/css/styles.css?t='+ts+'">'

    cur = mysql.get_db().cursor()
    cur.execute("select * from node_list order by ts_created asc;")
    results = cur.fetchall()
    print("Type of results: ", type(results))
    cur.close()
    
    templateData = {
        'jsInclude' : jsInclude,
        'cssInclude' : cssInclude
    }
    return render_template('index.html', **templateData, data=results)

@app.route("/template.html")
def template():
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO messageLogTable (channelId, origin, message, status) VALUES ('twitter', '192.168.1.24', 'testMessage', 'test');")
    mysql.get_db().commit()
    cur.close()
    return render_template('template.html')

@app.route("/nodeList.html")
@app.route("/nodelist.html")
def nodeList():
    cur = mysql.get_db().cursor()
    cur.execute("select * from node_list order by ts_created asc;")
    results = cur.fetchall()
    print("Type of results: ", type(results))
    cur.close()
    return render_template('nodeList.html', data=results)


@app.route("/nodeTelemetry.html")
@app.route("/nodetelemetry.html")
def template1():
    cur = mysql.get_db().cursor()
    cur.execute("select * from node_telemetry order by ts_created desc;")
    results = cur.fetchall()
    print("Type of results: ", type(results))
    cur.close()
    return render_template('nodeTelemetry.html', data=results)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1024)
