from asyncio import tasks
from email import message
from pydoc import describe
from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        "data": [
            {
                "Contact": "9987644456",
                "Name":"Raju",
                "done": false,
                "id": 1
            },
            {
                "Contact": "9876543222",
                "Name":"Rahul",
                "done": false,
                "id": 2
            }        
        ]
    }
    
]
@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pleade provide the data!"
        },400)

    task = {
        "id":tasks[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }

    tasks.append(task)
    return jsonify({ "status":"success", "message": "Task added succesfully!" })

@app.route("/get-data") 
def get_task(): 
    return jsonify({ "data" : tasks })

if (__name__ == "__main__"): 
    app.run(debug=True)