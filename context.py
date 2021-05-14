import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self, show=False):
        self.strategy = None
        self.show = show

    def plot(self, df, columns=None, x_label="", y_label="", title="", *args, **kwargs):
        if self.strategy is None:
            raise AssertionError("The strategy has not been set")

        self.strategy.plot(df, columns, x_label, y_label, title, *args, **kwargs)
        if self.show:
            plt.show()
