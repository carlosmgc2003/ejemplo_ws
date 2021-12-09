from flask import Flask,jsonify,request
from datetime import datetime

app =   Flask(__name__)
  
@app.route('/returntime', methods = ['GET'])
def ReturnTimeJson():
    """
    ReturnTimeJson recibe una peticion GET a /returntime y devuelve un JSON con la hora actual
    del servidor.
    """
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    if(request.method == 'GET'):
        data = {
            "time" : date_time
        }
        return jsonify(data)
  
if __name__=='__main__':
    app.run(debug=True)