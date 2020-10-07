from flask import *
from functools import wraps
import sqlite3
import pandas as pd
import requests


DATABASE = 'dataweb.db'

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config.from_object(__name__)

def connect_db():
    con = sqlite3.connect('dataweb.db')
    cursor = con.cursor()
    print('La base funcionò bien')

def run_query(query='',parameters=()):
    conn = sqlite3.connect('dataweb.db')
    cursor = conn.cursor()                 # Crear un cursor
    cursor.execute(query, parameters)                  # Ejecutar una consulta
    if query.upper().startswith('SELECT'):
       data= cursor.fetchall()               # Traer los resultados de un select
       
    else:
        conn.commit()                          # Hacer efectiva la escritura de datos
        data = None
         
    #cursor.close()                         # Cerrar el cursor
    #conn.close()                           # Cerrar la conexión
    #conn.close()                           # Cerrar la conexión
    
    return data




@app.route('/')
def index():

    query = 'SELECT * FROM datosclientes_v1'
    curs  = run_query(query)

    return render_template('index_desa.html', contacts = curs)


@app.route('/enviar')
def enviar():

            query = "SELECT * FROM datosclientes_v1 " 
            result = run_query(query)

            nombre = []
            nombre1 = request.args
            nombre2 = list(nombre1)

            for x1 in nombre2:
                nombre.append(x1)

            #print(nombre)
            for x2 in result:
                if x2[0] in nombre:
                    #print('Marcar:'+x2[0])
                    query = "UPDATE datosclientes_v1 SET checkbox = 'checked=checked' WHERE fullname  ='%s' " % x2[0] 
                    result_v1 = run_query(query)
                else:
                    query = "UPDATE datosclientes_v1 SET checkbox = '' WHERE fullname  ='%s' " % x2[0] 
                    result_v1 = run_query(query)
                    #print('Desmarcar:'+x2[0])
            
            #flash ('Seleccion de items actualizados exitosamente')
            return render_template('index_desa2.html')
            

if __name__ == '__main__':
    app.run(port = 3000, debug=True)



