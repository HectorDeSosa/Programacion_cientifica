import sqlite3
from sqlite3 import Error


#definicion de tabla
create_tabla_client = """
CREATE TABLE CLIENTE
(
  NumCliente INT NOT NULL,
  nombre CHAR(20) NOT NULL,
  direccion VARCHAR(50) NOT NULL,
  PRIMARY KEY (NumCliente)
);
"""

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("\nConexion SQLite DB exitosa")
    except Error as e:
        print(f"Ocurrio un error'{e}'")
    return connection
#funcion para ejecutar consultas
def execute_query(connection, consulta):
    cursor = connection.cursor()
    try:
        cursor.execute(consulta)
        connection.commit()
        print("Consulta ejecutada exitosamente")
    except Error as e:
        print(f"Ocurrio un error'{e}'")
#crear conexion
connection = create_connection("ejercicio1db.sqlite")
#ejecutar una consulta o un comando
execute_query(connection, create_tabla_client)

create_client = """
INSERT INTO
  CLIENTE (NumCliente, nombre, direccion)
VALUES
  (1, 'juan', 'USA'),
  (2, 'luis', 'AR'),
  (3, 'pedro', 'BR'),
  (4, 'tito', 'MX')
"""

execute_query(connection, create_client)