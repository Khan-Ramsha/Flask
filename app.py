from flask import Flask,render_template , request, jsonify

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def home():
    return render_template("index.html")

@app.route("/math",methods = ["POST"])
def math_operation():
    if(request.method=="POST"):
        op=request.form['operation']
        num1=int(request.form['input1'])
        num2=int(request.form['input2'])
        if(op=="add"):
            result=num1+num2
        if(op=="subtract"):
            result=num1-num2
        if(op=="multiply"):
            result=num1*num2
    return render_template("results.html", result=result)
    


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001, debug=True)
