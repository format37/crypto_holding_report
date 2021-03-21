import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class HodlerBenchmark:

    def __init__(self, df, name):

        self.df = df
        self.name = name

    def fit_unoptimized(self):

        hlp = np.zeros(len(self.df))
        for i in range(len(self.df)):
            investment_price = self.df.price.iloc[i]
            last_lost_date = self.df.date.iloc[i]
            for k in range(i, len(self.df)):
                if investment_price > self.df.price.iloc[k]:
                    last_lost_date = self.df.date.iloc[k]
            hlp[i] = (last_lost_date - self.df.date.iloc[i]).days
        self.df['hodl_period'] = hlp

    def fit(self):

        # convert data to numpy
        a = np.array(self.df.price)

        # upper triangle
        b = np.triu(a)

        # lower trinagle
        c = np.ones(b.shape)
        c = np.tril(c) * (max(a) + 1) * (np.ones(len(a)) - np.eye(len(a)))
        c += b

        # get dates, where prices are less then investing price
        d = pd.DataFrame(np.array(np.where(c.T <= np.diagonal(c))).T)
        d.columns = ['col', 'row']

        # diagonal bias
        bias = pd.DataFrame([i for i in range(len(a))], columns=['bias']).bias
        e = np.array(d.groupby('row').max().col - bias)
        self.df['hodl_period'] = e

    def plot(self, scale=True):

        temp_df = pd.DataFrame(self.df)
        if scale:
            temp_df['price_scaled'] = temp_df.price * max(temp_df.hodl_period) / max(temp_df.price)
        x = temp_df['date'].values.tolist()

        y1 = temp_df['price_scaled'].values.tolist()
        y2 = temp_df['hodl_period'].values.tolist()

        mycolors = ['tab:red', 'tab:blue', 'tab:red']
        columns = ['price_scaled', 'hodl_period']

        fig, ax = plt.subplots(1, 1, figsize=(16, 9), dpi=80)
        ax.fill_between(x, y1=y1, y2=0, label=columns[0], alpha=0.5, color=mycolors[0], linewidth=1)
        ax.fill_between(x, y1=y2, y2=0, label=columns[1], alpha=0.5, color=mycolors[1], linewidth=1)

        ax.set_xticklabels([])

        ax.set_title(self.name, fontsize=18)
        ax.legend(loc='best', fontsize=12)

        plt.show()
