import pandas as pd
from sklearn import preprocessing

def load_forest_fires():

    df = pd.read_csv('https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Regression/forest+fires/forestfires.csv')

    cat = df.select_dtypes(exclude='number')
    label_encoder = preprocessing.LabelEncoder()
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])
    

    df = df.to_numpy()
    target = df[:,-1]
    data = df[:,:-1]

    dataset = {'target': target,
            'data': data}
    
    return dataset                    

def load_energy_efficiency_y1():
    df = pd.read_excel('https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Regression/energy+efficiency/ENB2012_data.xlsx')

    df = df.to_numpy()

    target = df[:,8]
    data = df[:,:8]

    dataset = {'target': target,
            'data': data}
    
    return dataset

def load_energy_efficiency_y2():
    df = pd.read_excel('https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Regression/energy+efficiency/ENB2012_data.xlsx')

    df = df.to_numpy()

    target = df[:,9]
    data = df[:,:8]

    dataset = {'target': target,
            'data': data}
    
    return dataset

def load_auto_mpg():
    
    df = pd.read_csv('https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Regression/auto+mpg/auto-mpg.data', sep=',', header = 0,
                     names = ['blank',
                              'mpg',
                              'cylinders',
                              'displacement',
                              'horsepower',
                              'weight',
                              'acceleration',
                              'model year',
                              'origin',
                              'car name'])
    
    dataset = {'target': df['mpg'].to_numpy(),
                'data': df.drop(['blank','car name','mpg'],axis=1).to_numpy()}

    return dataset

def load_wine_quality_red():
    df = pd.read_csv('https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Regression/wine+quality/winequality-red.csv',sep=';')
    dataset = {'target': df['quality'].to_numpy(),
                'data': df.drop(['quality'],axis=1).to_numpy()}
    return dataset

def load_wine_quality_white():

    df = pd.read_csv('https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Regression/wine+quality/winequality-white.csv',sep=';')
    dataset = {'target': df['quality'].to_numpy(),
                'data': df.drop(['quality'],axis=1).to_numpy()}
    return dataset

def load_student_mat():
    label_encoder = preprocessing.LabelEncoder()

    df = pd.read_csv('https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Regression/student/studentmat.csv',sep=';') # Carrega os dados
    df = df.dropna() # Retira valores faltantes

    cat = df.select_dtypes(exclude='number')

    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    dataset = {'target': df['G3'].to_numpy(),
                'data': df.drop(['G1','G2','G3'],axis=1).to_numpy()}
    return dataset

def load_student_por():
    label_encoder = preprocessing.LabelEncoder()

    df = pd.read_csv('https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Regression/student/studentpor.csv',sep=';') # Carrega os dados
    df = df.dropna() # Retira valores faltantes

    cat = df.select_dtypes(exclude='number')

    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    dataset = {'target': df['G3'].to_numpy(),
                'data': df.drop(['G1','G2','G3'],axis=1).to_numpy()}
    return dataset


