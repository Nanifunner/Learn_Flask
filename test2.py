from flask import Flask, redirect,request, url_for

app = Flask(__name__)

@app.route('/success/<name>')  # decorator function for the route /
def success(name):
    return f'Welcome {name}'

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        username=request.form['nm']
        return redirect(url_for('success',name = username))
    else:
        username = request.args.get('nm')
        return redirect(url_for('success',name = username))

if __name__ == '__main__':
    app.run(debug = True)