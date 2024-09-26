from Functions.CSV import open_csv


class WordGroup:
    def __init__(self, name:str):
        self.word_data = open_csv(f'data/words/{name}.csv')