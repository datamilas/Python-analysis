import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


def find_min_distance(df, ref):
    '''
    Takes panda dataframe with X and Y columns and reference coordinates,
    Returns index of the row containing coordinates closest to the reference coordinates
    '''
    return np.argmin([np.sum([(a - b)**2 for a, b in zip(ref, row)]) for row in df.values])


def create_fig(COLOR="black", plot_size="big", xlabel="Time (s)", ylabel="Intensity", square_fig=True, fig_width=False, fig_height=False):

    if plot_size == "small":
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.linewidth'] = 0.5
        if not fig_width:
            if square_fig:
                fig_width = 2
                fig_height = 2
            else:
                fig_width = 2
                fig_height = 1.5
        tick_size = 3

    else:
        plt.rcParams['font.size'] = 18
        plt.rcParams['axes.linewidth'] = 1
        if not fig_width:
            if square_fig:
                fig_width = 5
                fig_height = 5
            else:
                fig_width = 5
                fig_height = 4
        tick_size = 7

    mpl.rcParams['font.family'] = 'Arial'
    mpl.rcParams['text.color'] = COLOR
    mpl.rcParams['axes.labelcolor'] = COLOR
    mpl.rcParams['axes.edgecolor'] = COLOR
    mpl.rcParams['xtick.color'] = COLOR
    mpl.rcParams['ytick.color'] = COLOR

    # Make text editable in illustrator
    mpl.rcParams['pdf.fonttype'] = 42
    mpl.rcParams['ps.fonttype'] = 42

    # Create figure object and store it in a variable called 'fig'
    fig = plt.figure(figsize=(fig_width, fig_height))

    # Add axes object to the figure that takes up entire figure
    ax = fig.add_axes([0, 0, 1, 1])

    # Edit the major and minor ticks of the x and y axes
    ax.xaxis.set_tick_params(which='major', size=tick_size,
                             width=plt.rcParams['axes.linewidth'], direction='in', top='on')
    ax.xaxis.set_tick_params(which='minor', size=tick_size,
                             width=plt.rcParams['axes.linewidth'], direction='in', top='on')
    ax.yaxis.set_tick_params(which='major', size=tick_size,
                             width=plt.rcParams['axes.linewidth'], direction='in', right='on')
    ax.yaxis.set_tick_params(which='minor', size=tick_size,
                             width=plt.rcParams['axes.linewidth'], direction='in', right='on')

    # Add the x and y-axis labels
    ax.set_xlabel(xlabel, labelpad=10)
    ax.set_ylabel(ylabel, labelpad=10)

    return fig, ax
