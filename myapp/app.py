from flask import Flask,redirect,url_for,render_template,request,jsonify
from Alumnos.routes import alumnos
from Directivos.routes import directivos
from Maestros.routes import Maestros

app=Flask(__name__)
app.config['DEBUG']= True

@app.route('/', methods = ['GET'])
def home():
 return jsonify({'Datos':'Hola'})

app.register_blueprint(alumnos)
app.register_blueprint(directivos)
app.register_blueprint(Maestros)


if __name__ == '__main__':
    app.run()