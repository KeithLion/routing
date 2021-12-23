from flask import Flask
app= Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<string:name>')
def say_hi(name):
    return f'Hi {name.capitalize()}!'

@app.route('/repeat/<int:number>/<string:thing>')
def repeat_thing(thing,number):
    return f'{thing * number}'

if __name__ == "__main__":
    app.run(debug=True)
