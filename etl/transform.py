from etl.extract import extraer_data
import pandas as pd


def transformar_data(df):

    df.columns = df.columns.str.strip()
    df['Volumen'] = df['Volumen'].str.replace(',','.').astype(float)
    df['USD FOB'] = df['USD FOB'].str.replace(',','.').astype(float)
    df['Fecha'] = pd.to_datetime(df['Anio'].astype(str) + '-' + df['Mes'].astype(str) + '-01')

    df = df.rename(columns={
        'Codigo producto': 'Codigo_Producto',
        'ID region':'ID_Region',
        'Region origen':'Region_Origen',
        'Pais destino':'Pais_Destino',
        'USD FOB': 'USD_FOB'
    })

    return df

if __name__ == '__main__':
    data = extraer_data('data/raw/comex_exportacion_publico_2010-2019.csv')
    clean_data = transformar_data(data) 
    
    print(clean_data.head())
    print(clean_data.info())


