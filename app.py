from crypt import methods
from flask import Flask
from flask import jsonify
import pdb
app= Flask(__name__)


lista_empleados=[{
    'id':'1',
    'nombre':'Jhon Doe',
    'salario':'1000'
},{
    'id':'2',
    'nombre':'Kate Doe',
    'salario':'2000'
}
]
#Crear una ruta
@app.route('/')
def index():
    return "Bienvenido a la api"

@app.route('/empleados')
def obtener_empleados():
    return jsonify(lista_empleados)

@app.route('/enviar',methods=['GET','POST'])
def obtener_enviar():
    resp={
        mensaje:"Mensaje enviado"
    }
    print(resp)
    

    return jsonify(resp)


#Punto de inicio 
if __name__ == '__main__':
    app.run(debug=True)
