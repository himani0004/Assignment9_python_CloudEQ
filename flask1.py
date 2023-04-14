#API using FLASK----->>>>>>>>


from flask import Flask, jsonify ,request


app = Flask(__name__)

tasks= [
    {
       'id':2,
        'title':'cources',
        'description':'mca,mba,mbbs,law',
        
  
    },
    {
        'id':3,
        'title':'students',
        'discription':'riya,himani,mandy',
        

   
    }
]

@app.route("/")
def hello_world():
    return "Hi Himani here !" 

@app.route("/add-data1",methods=["POST"])
def add_data():
    
    
    task = {
       'id':tasks[-1]['id'] + 1,
       'title':request.json['title'],
       'discription': request.json['discription']
    

    }
    tasks.append(task)
    return jsonify({
       "status":"success",
       "message":"added sucesfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })

if  (__name__== "__main__"):
    app.run(debug=True)  

