from flask import Flask  

app = Flask(__name__)   

@app.route('/')         
def index():
    return 'Hello, world'

@app.route('/dojo')         
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name.capitalize()}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat_num(num, word):
    return f'{word * num}'

@app.errorhandler(404)
def resource_not_found(e):
    return f'{e.message}'

if __name__=="__main__":   
    app.run(debug=True)   