from flask import Flask

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Definimos una ruta para la página de inicio
@app.route('/')
def hola_mundo():
    return '¡Hola, Mundo desde Render!'

# Una ruta adicional para demostrar el enrutamiento
@app.route('/bienvenido/<nombre>')
def bienvenido(nombre):
    return f'<h1>Bienvenido, {nombre}!</h1><p>Este es tu primer despliegue en la nube.</p>'
