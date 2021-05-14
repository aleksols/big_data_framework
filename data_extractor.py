import pandas as pd
from os import listdir


class Extractor:
    def __init__(self, csv_folder="csvs"):
        for filename in listdir(csv_folder):
            setattr(self, filename[:-4], pd.read_csv(f"{csv_folder}/{filename}"))

    def merge(self, left, right, on, how="left"):
        return pd.merge(left, right, on=on, how=how)

    def select_rows(self, source, column, condition, operator="=="):
        if isinstance(source, str):
            source = getattr(self, source)
        if operator in ["==", "="]:
            return source[source[column] == condition].copy(deep=True)
        if operator == ">=":
            return source[source[column] >= condition].copy(deep=True)
        if operator == "<=":
            return source[source[column] <= condition].copy(deep=True)

    def select_columns(self, df, *columns):
        return df[list(columns)].copy(deep=True)

    def replace_driverId(self, df):
        return pd.merge(df, self.drivers, how="left", on="driverId")

    def tire_age_vs_lap_time(self, raceId):
        lt = self.select_rows(self.lap_times, "raceId", 1052)
        lt = self.select_columns(lt, "driverId", "lap", "milliseconds")
        lt["seconds"] = lt.milliseconds / 1000
        ps = self.select_rows(self.pit_stops, "raceId", 1052)
        ps = self.select_columns(ps, "driverId", "lap", "stop")
        df = pd.merge(lt, ps, on=["driverId", "lap"], how="left").fillna(0)

        tire_ages = []
        current_driver = None
        tire_age = 0
        for idx, series in df.iterrows():
            if series.driverId != current_driver:
                tire_age = 0
                current_driver = series.driverId
            elif series.stop != 0:
                tire_age = 0
            else:
                tire_age += 1
            tire_ages.append(tire_age)
        df["tire_age"] = tire_ages
        return df





if __name__ == '__main__':
    e = Extractor()
    print(e.tire_age_vs_lap_time(1052).tail(20))


