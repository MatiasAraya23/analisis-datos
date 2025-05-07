import pandas as pd


def extraer_data(filepath):
    data = pd.read_csv(filepath, encoding='utf-8-sig')
    return data

if __name__ == "__main__":
    data = extraer_data('data/raw/comex_exportacion_publico_2010-2019.csv')
    print(data.info())
    print(data.head())