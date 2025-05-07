import pandas as pd
from utils.db_conection import connection
from etl.extract import extraer_data
from etl.transform import transformar_data

def create_table(conn):
    create_table_query="""
    CREATE TABLE IF NOT EXISTS exportaciones(
    id SERIAL PRIMARY KEY,
    anio INT,
    mes INT,
    codigo_producto INT,
    producto TEXT,
    id_region INT,
    region_origen TEXT,
    pais_destino TEXT,
    unidad TEXT,
    volumen FLOAT,
    usd_fob FLOAT,
    fecha DATE
    )
    """

    cursor = conn.cursor()
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    print("Tabla exportaciones creada")

def insertar_data(conn, df):
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO exportaciones (
    anio, mes, codigo_producto, producto, id_region, region_origen,
    pais_destino, unidad, volumen, usd_fob, fecha) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    data_to_insert = [
        (
            row['Anio'],
            row['Mes'],
            row['Codigo_Producto'],
            row['Producto'],
            row['ID_Region'],
            row['Region_Origen'],
            row['Pais_Destino'],
            row['Unidad'],
            row['Volumen'],
            row['USD_FOB'],
            row['Fecha']
        )
        for index, row in df.iterrows()
    ]

    cursor.executemany(insert_query, data_to_insert)
    conn.commit()
    cursor.close()
    
if __name__ == "__main__":
    conn = connection()

    if conn:
        df = extraer_data('data/raw/comex_exportacion_publico_2010-2019.csv')
        clean_df = transformar_data(df)

        create_table(conn)
        insertar_data(conn, clean_df)

        conn.close()
        print("Conexion Cerrada")
    else:
        print("No se pudo establecer conexion con la base de datos")