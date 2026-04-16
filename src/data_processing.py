import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    # Select important columns
    df = df[['Country', 'Age', 'LanguageHaveWorkedWith']]
    
    # Drop missing values
    df = df.dropna()
    
    return df

def explode_languages(df):
    # Split multi-select values
    df['LanguageHaveWorkedWith'] = df['LanguageHaveWorkedWith'].str.split(';')
    
    # Convert list into rows
    df = df.explode('LanguageHaveWorkedWith')
    
    return df

def get_language_counts(df):
    return df['LanguageHaveWorkedWith'].value_counts()

def get_country_counts(df):
    return df['Country'].value_counts().head(10)