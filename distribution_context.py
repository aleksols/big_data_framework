class Distribution:
    def __init__(self):
        self.strategy = None

    def plot(self, df, columns=None, x_label="", y_label="", title="", alpha=0.5, *args, **kwargs):
        if self.strategy is None:
            raise AssertionError("The strategy has not been set")

        self.strategy.plot(df, columns, x_label, y_label, title, alpha, *args, **kwargs)
