import pandas as pd
import numpy as np

# a) Carga de archivos (csv, xlsx, html y json) a dataframes
def load_file(file_path, file_type):
    if file_type == 'csv':
        return pd.read_csv(file_path)
    elif file_type == 'xlsx':
        return pd.read_excel(file_path)
    elif file_type == 'html':
        return pd.read_html(file_path)
    elif file_type == 'json':
        return pd.read_json(file_path)
    else:
        raise ValueError("Tipo de archivo no soportado. Use 'csv', 'xlsx', 'html' o 'json'.")

# b) Sustitución de valores nulos con el método de “ffill”
def fill_na_ffill(df):
    return df.fillna(method='ffill')

# c) Sustitución de valores nulos con el método de “bfill”
def fill_na_bfill(df):
    return df.fillna(method='bfill')

# d) Sustitución de valores nulos con un “string concreto”
def fill_na_with_string(df, string):
    return df.fillna(string)

# e) Sustitución de valores nulos con el método de “promedio”
def fill_na_with_mean(df):
    return df.fillna(df.mean())

# f) Sustitución de valores nulos con el método de “mediana”
def fill_na_with_median(df):
    return df.fillna(df.median())

# g) Sustitución de valores nulos con el método de “constante”
def fill_na_with_constant(df, constant):
    return df.fillna(constant)

# i) Identificación de valores nulos por columna y por dataframe
def identify_na(df):
    na_per_column = df.isna().sum()
    na_total = df.isna().sum().sum()
    return na_per_column, na_total