import pandas as pd

def codificar_variables(data):
    df = data.copy()

    # Variables binarias
    bin_map = {'yes': 1, 'no': 0}
    for col in ['default', 'housing', 'loan', 'y']:
        df[col] = df[col].astype(str).str.strip().map(bin_map)

    # Codificación ordinal (education)
    edu_map = {'unknown': 0, 'primary': 1, 'secondary': 2, 'tertiary': 3}
    df['education'] = df['education'].map(edu_map)

    # Codificación OneHot
    onehot_cols = ['job', 'marital', 'contact', 'month', 'poutcome']
    df = pd.get_dummies(df, columns=onehot_cols, drop_first=True)

    return df