from flask import Flask
from flask import render_template
from flask import request
import sequence
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    name = ""
    myData=""
    myResult=""
    if  request.method == 'POST':
        myData = request.form['myData']
        myResult = sequence.sequenceToChinese(myData)
    return render_template('index.html', name=name, myData=myData, myResult=myResult)


