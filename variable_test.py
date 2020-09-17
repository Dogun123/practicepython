from flask import Flask, render_template,request,jsonify
app = Flask(__name__)


@app.route('/hello')
def hello_name():
    email_address = request.args.get("email_address")
    inputpw = request.args.get("inputpw")
    
    return render_template('variable.html',name1=email_address,name2=inputpw)

@app.route('/')
def login():
    return render_template('login.html')    


if __name__ == '__main__':
    app.run(host="localhost", port="8080", debug = True)
