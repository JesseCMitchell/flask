from flask import Flask
app = Flask(__name__)


@app.route('/')         
def hello_world():
    return 'Hello World!'  

@app.route('/<first_name>') # pro tip - you can stack as many of them as you want, but you have to add default values like in line 11
@app.route('/<first_name>/<last_name>')
def hello_world_2(first_name, last_name='Mitchell'):
    return f'Hello {first_name} {last_name}'



if __name__=="__main__":     
    app.run(debug=True)