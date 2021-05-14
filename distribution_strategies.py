import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()


class Dist:
    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        raise NotImplementedError()


class HistogramPlotter(Dist):
    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns
        alpha = 1 / len(columns)
        for col in columns:
            print(col)
            plt.hist(df[col], density=True, alpha=alpha)
            plt.gca().set_title(title)
        plt.show()


class CorrelogramPlotter(Dist):
    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns
        sns.pairplot(df[columns], kind="scatter").fig.suptitle(title, y=1.001)
        plt.show()


class BoxPlotter(Dist):
    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns
        sns.boxplot(data=df[columns]).set_title(title)
        plt.show()


class DensityPlotter(Dist):
    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns[0]
        sns.kdeplot(df[columns]).set_title(title)
        plt.show()


class ViolinPlotter(Dist):
    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns
        sns.violinplot(data=df[columns]).set_title(title)
        plt.show()
