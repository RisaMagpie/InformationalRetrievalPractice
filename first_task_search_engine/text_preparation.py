import pandas as pd


def tokenize(df: pd.DataFrame(columns=["Text"])):
    df["Text"].replace(r"(<[^>]*>|\W)", " ", regex=True, inplace=True)
    df["Text"].replace(r" +", " ", regex=True, inplace=True)
    df["Text"] = df["Text"].astype(str).str.lower()
    df["Text"] = df["Text"].apply(lambda x: x.split(" "))
    return df
