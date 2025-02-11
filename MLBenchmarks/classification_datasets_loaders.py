import pandas as pd
from sklearn import preprocessing
import openml
import numpy as np

def load_breast_cancer_wisconsin():
    label_encoder = preprocessing.LabelEncoder()
    df = pd.read_csv(
        'https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Classification/breast+cancer+wisconsin+diagnostic/wdbc.data',
        header=None)
    df = df.dropna()

    cat = df.select_dtypes(exclude=['number'])

    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, 1]
    data = df[:, 2:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic',
               'date_access': '2023-10-19'}

    return dataset


def load_soybean_large():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Classification/soybean%2Blarge/soybean-large.data',
        header=None, na_values='?')
    df = df.dropna()

    cat = df.select_dtypes(exclude='number')
    label_encoder = preprocessing.LabelEncoder()
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()

    target = df[:, 0]
    data = df[:, 1:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://archive.ics.uci.edu/dataset/90/soybean+large',
               'date_access': '2023-09-20'}

    return dataset


def load_spect():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Classification/spect%2Bheart/SPECT_all.csv',
        header=None)

    df[df.columns] = df[df.columns].apply(pd.to_numeric)

    df = df.to_numpy()

    target = df[:, 0]
    data = df[:, 1:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://archive.ics.uci.edu/dataset/95/spect+heart',
               'date_access': '2023-09-20'}

    return dataset


def load_spectf():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Classification/spect%2Bheart/SPECTF_all.csv',
        header=None)

    df = df.to_numpy()

    target = df[:, 0]
    data = df[:, 1:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://archive.ics.uci.edu/dataset/95/spect+heart',
               'date_access': '2023-09-20'}

    return dataset


def load_obesity_eating_habits():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Classification/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition/ObesityDataSet_raw_and_data_sinthetic.csv')
    df = df.dropna()

    cat = df.select_dtypes(exclude='number')
    label_encoder = preprocessing.LabelEncoder()
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()

    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition',
               'date_access': '2023-09-20'}

    return dataset


def load_wine():
    file_path = 'https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Classification/wine/wine.data'

    df = pd.read_csv(file_path, sep=',', header=None)
    df = df.dropna()
    df = df.to_numpy()

    target = df[:, 0]
    data = df[:, 1:]

    dataset = {'target': target,
               'data': data,
               'info': 'https://archive.ics.uci.edu/dataset/109/wine',
               'date_access': '2023-09-12'}

    return dataset


def load_spambase():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Classification/spambase/spambase.data',
        sep=',', header=None)
    df = df.dropna()
    df = df.to_numpy()

    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://archive.ics.uci.edu/dataset/94/spambase',
               'date_access': '2023-09-12'}

    return dataset


def load_student_dropout():
    label_encoder = preprocessing.LabelEncoder()
    df = pd.read_csv(
        'https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Classification/predict+students+dropout+and+academic+success/data.csv',
        sep=';')

    df = df.dropna()

    target = 'Target'

    df[target] = label_encoder.fit_transform(df[target])

    dataset = {'target': df[target].to_numpy(),
               'data': df.drop([target], axis=1).to_numpy(),
               'info': 'https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success',
               'date_access': '2023-09-12'}

    return dataset


def load_dry_bean():
    label_encoder = preprocessing.LabelEncoder()

    df = pd.read_excel(
        'https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Classification/dry+bean+dataset/DryBeanDataset/Dry_Bean_Dataset.xlsx')

    df['Class'] = label_encoder.fit_transform(df['Class'])

    dataset = {'target': df['Class'].to_numpy(),
               'data': df.drop(['Class'], axis=1).to_numpy(),
               'info': 'https://archive.ics.uci.edu/dataset/602/dry+bean+dataset',
               'date_access': '2023-09-12'}

    return dataset


def load_mushroom():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/rcpsilva/MLBenchmarks/main/MLBenchmarks/datasets/Classification/mushroom/agaricus-lepiota.data',
        sep=',', header=0,
        names=['class',
               'cap-shape',
               'cap-surface',
               'cap-color',
               'bruises',
               'odor',
               'gill-attachment',
               'gill-spacing',
               'gill-size',
               'gill-color',
               'stalk-shape',
               'stalk-root',
               'stalk-surface-above-ring',
               'stalk-surface-below-ring',
               'stalk-color-above-ring',
               'stalk-color-below-ring',
               'veil-type',
               'veil-color',
               'ring-number',
               'ring-type',
               'spore-print-color',
               'population',
               'habitat'])

    label_encoder = preprocessing.LabelEncoder()
    cat = df.select_dtypes(exclude='number')

    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    dataset = {'target': df['class'].to_numpy(),
               'data': df.drop(['class'], axis=1).to_numpy(),
               'info': 'https://archive.ics.uci.edu/dataset/73/mushroom',
               'date_access': '2023-09-12'}

    return dataset


def load_drugs():
    label_encoder = preprocessing.LabelEncoder()

    df = pd.read_csv('MLBenchmarks/datasets/Classification/drug+classification/drug200.csv')
    df = df.dropna()

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, 5]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.kaggle.com/datasets/prathamtripathi/drug-classification',
               'date_access': '2023-10-29'}

    return dataset


def load_gender_classification():
    label_encoder = preprocessing.LabelEncoder()

    df = pd.read_csv('MLBenchmarks/datasets/Classification/gender+classification/genderClass.csv')
    df = df.dropna()

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, 4]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.kaggle.com/datasets/hb20007/gender-classification',
               'date_access': '2023-11-07'}

    return dataset


def load_happy_detector():
    label_encoder = preprocessing.LabelEncoder()

    df = pd.read_csv('MLBenchmarks/datasets/Classification/happy+detection/happy_unhappy.csv')
    df = df.dropna()

    # The data is already normalized

    # cat = df.select_dtypes(exclude=['number'])
    # for col in cat.columns:
    #     df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, 6]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.kaggle.com/datasets/priyanshusethi/happiness-classification-dataset',
               'date_access': '2023-10-29'}

    return dataset

def load_type_customer():

    label_encoder = preprocessing.LabelEncoder()

    df = pd.read_csv('MLBenchmarks/datasets/Classification/type+customer/type_customer.csv')
    df = df.dropna()

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, 11]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.kaggle.com/datasets/prathamtripathi/customersegmentation',
               'date_access': '2023-10-29'}

    return dataset

def load_paris_housing_classification():

    label_encoder = preprocessing.LabelEncoder()

    df = pd.read_csv('MLBenchmarks/datasets/Classification/paris+housing+class/ParisHousingClass.csv')
    df = df.dropna()

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, 17]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.kaggle.com/datasets/mssmartypants/paris-housing-classification',
               'date_access': '2023-10-29'}

    return dataset


def load_CSGO_round_winner():

    label_encoder = preprocessing.LabelEncoder()

    df = pd.read_csv('MLBenchmarks/datasets/Classification/csgo+round+winner/csgo_round_snapshots.csv')
    df = df.dropna()

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, 96]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.kaggle.com/datasets/christianlillelund/csgo-round-winner-classification',
               'date_access': '2023-11-08'}

    return dataset

def load_heart_disease_classification():

    label_encoder = preprocessing.LabelEncoder()

    df = pd.read_csv('MLBenchmarks/datasets/Classification/heart+disease+classification/heart_disease_classification.csv')
    df = df.dropna()

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.kaggle.com/datasets/sumaiyatasmeem/heart-disease-classification-dataset/data',
               'date_access': '2023-10-29'}

    return dataset

def load_pokemon_species():

    label_encoder = preprocessing.LabelEncoder()


    dataset_id = 43749
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&id=43749',
               'date_access': '2023-12-16'}

    return dataset

def load_chronic_kidney_disease():

    label_encoder = preprocessing.LabelEncoder()


    dataset_id = 42972
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&id=42972',
               'date_access': '2023-12-16'}

    return dataset


def load_breast_cancer_coimbra():

    label_encoder = preprocessing.LabelEncoder()


    dataset_id = 42900
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    # display(df)
    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&id=42900',
               'date_access': '2023-12-16'}

    return dataset

def load_autoML_selector_multiclass():
    label_encoder = preprocessing.LabelEncoder()

    dataset_id = 44200
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    # display(df)

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&id=44200',
               'date_access': '2023-12-16'}

    return dataset


def load_conference_attendance():
    label_encoder = preprocessing.LabelEncoder()

    dataset_id = 41538
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    # display(df)

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, 3]
    data = np.concatenate((df[:, :3], df[:, 3 + 1:]), axis=1)

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&id=41538',
               'date_access': '2023-12-16'}

    return dataset


def load_credit_score():
    label_encoder = preprocessing.LabelEncoder()

    dataset_id = 31
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    # display(df)

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&sort=runs&id=31',
               'date_access': '2023-12-16'}

    return dataset


def load_blood_transfusion_service_center():
    label_encoder = preprocessing.LabelEncoder()

    dataset_id = 1464
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    # display(df)

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&sort=runs&id=1464',
               'date_access': '2023-12-16'}

    return dataset

def load_monks_problems():
    label_encoder = preprocessing.LabelEncoder()

    dataset_id = 334
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    # display(df)

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, 0]
    data = df[:, 1:]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&sort=runs&id=334',
               'date_access': '2023-12-16'}

    return dataset


def load_tic_tac_toe():
    label_encoder = preprocessing.LabelEncoder()

    dataset_id = 50
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    #display(df)

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&sort=runs&id=50',
               'date_access': '2023-12-16'}

    return dataset


def load_diabetes_classification():
    label_encoder = preprocessing.LabelEncoder()

    dataset_id = 37
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    # display(df)

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&sort=runs&id=37',
               'date_access': '2023-12-16'}

    return dataset


def load_KC2_software_defect_prediction():
    label_encoder = preprocessing.LabelEncoder()

    dataset_id = 1063
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    # display(df)

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&sort=runs&id=1063',
               'date_access': '2023-12-17'}

    return dataset


def load_eucalyptus_soil_conservation():
    label_encoder = preprocessing.LabelEncoder()

    dataset_id = 188
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    # display(df)

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&sort=runs&id=188',
               'date_access': '2023-12-17'}

    return dataset


def load_contraceptive_method_choice():
    label_encoder = preprocessing.LabelEncoder()

    dataset_id = 23
    df, *_ = openml.datasets.get_dataset(dataset_id).get_data()
    df = df.dropna()
    # display(df)

    cat = df.select_dtypes(exclude=['number'])
    for col in cat.columns:
        df[col] = label_encoder.fit_transform(df[col])

    df = df.to_numpy()
    target = df[:, -1]
    data = df[:, 0:-1]

    dataset = {'target': target,
               'data': data,
               'info': 'https://www.openml.org/search?type=data&status=active&sort=runs&id=23',
               'date_access': '2023-12-17'}

    return dataset