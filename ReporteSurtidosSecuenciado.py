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
        query = f"SELECT surtido_secuenciado.id_surtido_secuenciado, surtido_secuenciado.primer_secuencia, surtido_secuenciado.ultima_secuencia, surtido_secuenciado.fecha, surtido_secuenciado.hora_secuencia_actual,surtido_secuenciado.hora_secuencia_vacio, surtido_secuenciado.estado, operador.numero_empleado,commoditie.nombre FROM surtido_secuenciado INNER JOIN commoditie ON surtido_secuenciado.id_commoditie = commoditie.id_commoditie INNER JOIN operador ON surtido_secuenciado.id_operador = operador.id_operador WHERE fecha = '2021-05-31'"
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
  writer.writerow(['ID SURTIDO SECUENCIADO', 'PRIMER SECUENCIA', 'ULTIMA SECUENCIA', 'FECHA', 'HORA SECUENCUA ACTUAL', 'HORA SECUENCIA VACIO','ESTADO', 'OPERADOR', 'NOMBRE COMMODITIE'])
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