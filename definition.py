import pandas as pd


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        data_path = r"C:\Users\aayus\Desktop\Secrets-of-the-Universe\Instant-Dictionary\data.csv"
        df = pd.read_csv(data_path)
        return tuple(df.loc[df['word'] == self.term]['definition'])
