import pandas as pd

class DataExporter:
    @staticmethod
    def to_csv(data: list, filename="top_movies_imdb.csv"):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding="utf-8-sig")