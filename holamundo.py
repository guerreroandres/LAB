from flask import Flask

app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Hola Mundo!'

@app.route('/adios')
def adiosmundo():
    return 'Adios Mundo!'

if __name__ == '__main__':
    #app.run()
    app.run(port=3000, debug=True)

