from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')         
def index():
    return render_template('index.html') # in parens NEEDS to be a string named after your template file      

@app.route('/<first_name>') # pro tip - you can stack as many of them as you want, but you have to add default values like in line 11
@app.route('/<first_name>/<last_name>')
def hello_world_2(first_name, last_name='Mitchell'):
    return f'Hello {first_name} {last_name}'

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return render_template("hello.html", banana=banana, num=num)



if __name__=="__main__":     
    app.run(debug=True)