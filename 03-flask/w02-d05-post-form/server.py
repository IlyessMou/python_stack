from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("*"*20, "PROCESS-FORM RECEIVED","*"*20)
    print(("-"*20, request.form,"-"*20))
    print(f"USERNAME: {request.form['username']}")

    return None

if (__name__=='__main__'):
    app.run(debug=True, port=5003)