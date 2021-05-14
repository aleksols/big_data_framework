import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns


class Plotter:
    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        raise NotImplementedError()


class BarPlotter(Plotter):
    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns
        df.plot(
            x=columns[0],
            y=columns[1],
            kind="bar",
            xlabel=x_label,
            ylabel=y_label,
            title=title,
            legend=True
        )
        # plt.show()


class LinePlotter(Plotter):
    def plot(self, df, columns, x_label, y_label, title, bin_size=1, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns

        ax = df[::bin_size].plot(
            x=columns[0],
            y=columns[1],
            xlabel=x_label,
            ylabel=y_label,
            title=title,
            legend=True
        )
        if "int" in str(df[columns[0]].dtype):
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        # plt.show()


class ScatterPlotter(Plotter):
    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns
        df.plot(
            x=columns[0],
            y=columns[1],
            xlabel=x_label,
            ylabel=y_label,
            kind="scatter",
            title=title,
            legend=True
        )
        # plt.show()


class HistogramPlotter(Plotter):
    def __init__(self):
        sns.set()

    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns
        alpha = 1 / len(columns)
        for col in columns:
            print(col)
            # sns.histplot(data=df[col])
            plt.hist(df[col], density=True, alpha=alpha, label=col)
            plt.legend()
            plt.gca().set_title(title)
        # plt.show()


class CorrelogramPlotter(Plotter):
    def __init__(self):
        sns.set()

    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns
        sns.pairplot(df[columns], kind="scatter").fig.suptitle(title, y=1.001)
        # plt.show()


class BoxPlotter(Plotter):
    def __init__(self):
        sns.set()

    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns
        sns.boxplot(data=df[columns]).set_title(title)
        # plt.show()


class DensityPlotter(Plotter):
    def __init__(self):
        sns.set()

    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns[:1]
        sns.kdeplot(data=df[columns]).set_title(title)
        # plt.show()


class ViolinPlotter(Plotter):
    def __init__(self):
        sns.set()

    def plot(self, df, columns, x_label, y_label, title, *args, **kwargs):
        if columns is None or columns == []:
            columns = df.columns
        sns.violinplot(data=df[columns]).set_title(title)
        # plt.show()


if __name__ == '__main__':
    import pandas as pd
    import numpy as np

    x = np.random.normal(0, 1, 1000)
    y = x + np.random.normal(0, 3, 1000)
    dummy_df = pd.DataFrame({
        "x": x,
        "y": y,
        "z": x + np.random.poisson(0.1, 1000),
        "w": np.random.chisquare(4, 1000)
    })

    s = DensityPlotter()
    s.plot(dummy_df, ["x"], "", "", "")
    plt.show()
