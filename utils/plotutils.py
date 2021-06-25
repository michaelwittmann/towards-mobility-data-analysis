import matplotlib.dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i / inch for i in tupl[0])
    else:
        return tuple(i / inch for i in tupl)


def format_plot_xlabels_days_6H(ax):
    ax.xaxis.set_major_locator(matplotlib.dates.DayLocator())
    ax.xaxis.set_minor_locator(matplotlib.dates.HourLocator(byhour=[6, 12, 18]))
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a'))
    ax.xaxis.set_minor_formatter(matplotlib.dates.DateFormatter('%H'))

def format_plot_xlabels_week_ts(ax):
    ax.xaxis.set_major_locator(matplotlib.dates.DayLocator())
    ax.xaxis.set_minor_locator(matplotlib.dates.HourLocator(byhour=[0, 6, 12, 18]))
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a.'))
    ax.xaxis.set_minor_formatter(matplotlib.dates.DateFormatter('%H:%M'))
    ax.tick_params(axis='x', which='minor', labelsize=6, labelrotation=90)
    ax.tick_params(axis='x', which='major', labelrotation=90)

def plot_cdf(data: pd.Series, ax=None, bins=100, label=None):
    if ax is None:
        fig, ax = new_figure()
    counts, bin_edges = np.histogram(data, bins=100)
    cdf = np.cumsum(counts)
    ax.plot(bin_edges[1:], cdf / cdf[-1], label=label)


tum_colors = [['#0065BD', '#000000', '#ffffff'],
             ['#005293', '#003359', '#333333', '#808080', '#CCCCC6'],
             ['#DAD7CB', '#E37222', '#A2AD00', '#98C6EA', '#64A0C8'],
             ['#69085a', '#0f1b5f', '#00778a', '#007c30', '#679a1d', '#ffdc00', '#f9ba00',
              '#d64c13', '#c4071b', '#9c0d16']]

tumcolors = {'primary_blue':'#0065bd',
            'primaryy_white':'#ffffff',
            'primaryy_black':'#000000',
            'secondary_blue_1':'#005293',
            'secondary_blue_2':'#003359',
            'secondary_grey_1':'#333333',
            'secondary_grey_2':'#808080',
            'secondary_grey_3':'#ccccc6',
            'accent_ivory':'#dad7cb',
            'accent_orange':'#e37222',
            'accent_green':'#a2ad00',
            'accent_blue_1':'#98c6ea',
            'accent_blue_2':'#64a0c8',
            'extended_purple':'#69085a',
            'extended_blue':'#0f1b5f',
            'extended_cyan':'#00778a',
            'extended_green_1':'#007c30',
            'extended_green_1':'#679a1d',
            'extended_yellow':'#ffdc00',
            'extended_mustard':'#f9ba00',
            'extended_orange':'#d64c13',
            'extended_red_1':'#c4071b',
            'extended_red_2':'#9c0d16'}


# Definitions
fig_page_width = cm2inch(16, 8)
fig_size_full_width_3_1 = cm2inch(16, 16 / 3)
fig_size_full_width_2_1 = cm2inch(16, 16/ 2)
fig_size_full_width_1_1 = cm2inch(16, 16)
fig_size_full_width_4_3 = cm2inch(16, 16/4*3)
fig_size_full_width_16_9 = cm2inch(16, 9)
fig_size_half_width_1_1 = cm2inch(8, 8)

fig_size_ppt_full = cm2inch(32, 11)
fig_size_ppt_half = cm2inch(16.3, 11)
fig_size_ppt_half_1_1 = cm2inch(11, 11)


def new_figure(figsize=fig_page_width):
    return plt.subplots(1, 1, figsize=figsize)
