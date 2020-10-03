from flask import Flask, render_template, jsonify, request
from flaskext.mysql import MySQL
import time
import json

from models import dbConfig as dbc
from models.data import Models
from models.data import ModelType


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

    results = Models(mysql.get_db()).fetch(ModelType.NODE_LIST)
    print("Type of results: ", type(results))

    newResults = ()
    for var in results:
        nodeId = var[3]
        nodeQuery = ("select * from node_telemetry"
			            +" where nodeId = " + str(nodeId)
                        +" order by ts_created desc limit 1;")
        print (nodeQuery)
        cur = mysql.get_db().cursor()
        cur.execute(nodeQuery)
        r = cur.fetchall()
        print("nodeQuery results: ", r)
        cur.close()

        element = var + r[0]

        eList = list(element) #[*element]
        ctr=0
        for i in eList:
            print(ctr, ":::", i)
            
            if(ctr == 12):
                try:
                    jsonE = json.loads(i)
                except:
                    jsonE = {}
                    print("Unable to convert to json")

                try:
                    print("JSON: ", jsonE['ip'])
                    itemIp = jsonE['ip']
                except:
                    itemIp = "IPV4 unknown"
                    print("ip not found")

                try:    
                    print("JSON: ", jsonE['session']['uptime'])
                    itemUptime = "Up since "+jsonE['session']['uptime']
                except:
                    itemUptime = "Uptime unknown"
                    print("uptime not found")

                try:
                    print("JSON: ", jsonE['calendarEvents'])
                    itemCe = str(jsonE['calendarEvents']) + " calendar events"
                except:
                    itemCe = "Calendar events unknown"
                    print("calendarEvents not found")

                try:
                    print("JSON: ", jsonE['scheduledEvents'])
                    itemSe = str(jsonE['scheduledEvents']) + " scheduled events"
                except:
                    itemSe = "Scheduled events unknown"
                    print("scheduledEvents not found")

                try:
                    print("JSON: ", jsonE['temperature'])
                    if(jsonE['temperature'] == -100):
                        itemTe = "No onboard Temp. sensor"
                    else:
                        itemTe = "Onboard temp:" + str(jsonE['temperature'])
                except:
                    itemTe = "Temp. unknown"
                    print("temp not found")

                tupToAdd = (itemIp, itemUptime, itemCe, itemSe, itemTe, )
                element = element + tupToAdd
            
            ctr = ctr+1

        print ("\nElement: ", element, "\n")
        newResults = newResults + (element,)


        print("\n\n")

    print("\n\n\nNew Results: ", newResults)

    for nr in newResults:
        ctx = 0
        for i in nr:
            print(ctx," >>> ", i)
            ctx=ctx+1

    templateData = {
        'jsInclude' : jsInclude,
        'cssInclude' : cssInclude
    }
    return render_template('index.html', **templateData, data=newResults)

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

@app.route("/manageNode.json", methods=['get'])
def manageNode():
    ts = str(int(time.time()))

    qpNodeId = request.args.get("nodeId")
    print("qpNodeID: ",qpNodeId)

    if(qpNodeId == '9999999'):
        return "Node not found", 400
    

    response = {
        "state":"unsuccessful",
        "ts": ts,
        "last_updated": ""
    }
    return(jsonify(response))

@app.route("/manageNodes.html", methods=['get'])
@app.route("/managenodes.html", methods=['get'])
def managenodes():
    ts = str(int(time.time()))

    jsInclude = '<script src="/static/js/scripts.js?t='+ts+'"></script>'
    jsInclude += '<script src="/static/js/manageNodes.js?t='+ts+'"></script>'
    jsInclude += '<script src="https://kit.fontawesome.com/7daabcbab0.js" crossorigin="anonymous"></script>'
    
    cssInclude = '<link rel="stylesheet" href="static/css/styles.css?t='+ts+'">'

    cur = mysql.get_db().cursor()
    cur.execute("select * from node_list order by ts_created asc;")
    results = cur.fetchall()
    print("Type of results: ", type(results))
    cur.close()

    newResults = ()
    for var in results:
        nodeId = var[3]
        nodeQuery = ("select * from node_telemetry"
			            +" where nodeId = " + str(nodeId)
                        +" order by ts_created desc limit 1;")
        print (nodeQuery)
        cur = mysql.get_db().cursor()
        cur.execute(nodeQuery)
        r = cur.fetchall()
        print("nodeQuery results: ", r)
        cur.close()

        element = var + r[0]

        eList = list(element) #[*element]
        ctr=0
        for i in eList:
            print(ctr, ":::", i)
            
            if(ctr == 12):
                try:
                    jsonE = json.loads(i)
                except:
                    jsonE = {}
                    print("Unable to convert to json")

                try:
                    print("JSON: ", jsonE['ip'])
                    itemIp = jsonE['ip']
                except:
                    itemIp = "IPV4 unknown"
                    print("ip not found")

                try:    
                    print("JSON: ", jsonE['session']['uptime'])
                    itemUptime = "Up since "+jsonE['session']['uptime']
                except:
                    itemUptime = "Uptime unknown"
                    print("uptime not found")

                try:
                    print("JSON: ", jsonE['calendarEvents'])
                    itemCe = str(jsonE['calendarEvents']) + " calendar events"
                except:
                    itemCe = "Calendar events unknown"
                    print("calendarEvents not found")

                try:
                    print("JSON: ", jsonE['scheduledEvents'])
                    itemSe = str(jsonE['scheduledEvents']) + " scheduled events"
                except:
                    itemSe = "Scheduled events unknown"
                    print("scheduledEvents not found")

                try:
                    print("JSON: ", jsonE['temperature'])
                    if(jsonE['temperature'] == -100):
                        itemTe = "No onboard Temp. sensor"
                    else:
                        itemTe = "Onboard temp:" + str(jsonE['temperature'])
                except:
                    itemTe = "Temp. unknown"
                    print("temp not found")

                tupToAdd = (itemIp, itemUptime, itemCe, itemSe, itemTe, )
                element = element + tupToAdd
            
            ctr = ctr+1

        print ("\nElement: ", element, "\n")
        newResults = newResults + (element,)


        print("\n\n")

    print("\n\n\nNew Results: ", newResults)

    for nr in newResults:
        ctx = 0
        for i in nr:
            print(ctx," >>> ", i)
            ctx=ctx+1

    templateData = {
        'jsInclude' : jsInclude,
        'cssInclude' : cssInclude
    }
    return render_template('manageNodes.html', **templateData, data=newResults)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1024)
