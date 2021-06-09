import pandas as pd
import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = '167.99.59.246',
            user = 'angeleduardogj',
            password = 'Exodo333Exodo',
            db = 'escaner'
        )
        self.cursor = self.connection.cursor()
        print('Conexion establecida exitosamente')

    def close(self):
        self.connection.close()

    
    def consulta(self):
        query = f"SELECT surtido_call.id_surtido_call, surtido_call.codigo_serial, surtido_call.fecha, surtido_call.hora_presurtido, surtido_call.hora_parte,surtido_call.hora_vacio, surtido_call.estado, operador.numero_empleado, parte.numero_parte FROM surtido_call INNER JOIN parte ON surtido_call.id_parte = parte.id_parte INNER JOIN operador ON surtido_call.id_operador = operador.id_operador WHERE fecha = '2021-05-31'"
        try:
            self.cursor.execute(query)
            r = self.cursor.fetchall()
        except Exception as e:
            raise
        return r

db =DataBase()

r = db.consulta()


import csv
with open('reporte-surtido-secuenciado.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['ID SURTIDO CALL', 'CODIGO SERIAL', 'FECHA', 'HORA PRESURTIDO', 'HORA PARTE', 'HORA VACIO','ESTADO', 'OPERADOR', 'NUMERO PARTE'])
  for x in r:
      A =  x[0]
      B = x[1]
      C = x[2]
      D = x[3]
      E = x[4]
      F = x[5]
      G = x[6]
      H = x[7]
      I = x[8]
      writer.writerow([A, B, C, D,E, F,G, H, I])

  db.close()