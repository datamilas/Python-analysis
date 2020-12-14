from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import Legend


def make_stacked_plot(results_object, use_percentages=False, x_order=None, xlabel=None, title=None, legend_order=None, colors=None):

    output_file("stacked.html")
    x_labels = list(results_object.x_values)
    all_data = list(results_object.data)
    sample_size = list(results_object.sample_size)
    legend = list(results_object.legend)

    if x_order:
        # reorder data:
        new_indices = [x_labels.index(o) for o in x_order]
        for ind, d in enumerate(all_data):
            all_data[ind] = [d[i] for i in new_indices]
        # reorder sample size:
        sample_size = [sample_size[i] for i in new_indices]
        # reorder labels:
        x_labels = x_order

    if legend_order:
        all_data = [all_data[legend.index(label)] for label in legend_order]
        legend = legend_order

    if not xlabel:
        xlabel = results.x_name

    x_labels = [l+'(n='+str(n)+')' for l, n in zip(x_labels, sample_size)]

    legend_list = []
    for l in legend:
        legend_label = ""
        for key, value in l.items():
            try:
                legend_label += (str(phenotype_dict[key]
                                     )+":"+str(value) + ", ")
            except:
                legend_label += (str(key)+":"+str(value) + ", ")
        legend_list.append(legend_label)

    if use_percentages:
        all_data = [[d/sample_size[ind]*100 for ind,
                     d in enumerate(data)] for data in all_data]
    data = {x_label: x_labels}

    phenotypes = [str(l) for l in legend]
    for k, d in zip(phenotypes, all_data):
        data[k] = d

    p = figure(x_range=x_labels, plot_height=250, plot_width=1000, title=title,
               toolbar_location=None, tools="")

    if not colors:
        colors = ["red", "blue", "green", "yellow",
                  "purple", "orange", "magenta", "black"]*100
        colors = colors[:len(phenotypes)]
        r = p.vbar_stack(phenotypes, x=x_label, width=0.9,
                         color=colors, source=data)

    # legend
    legend = Legend(items=[(str(l), [i])
                           for l, i in zip(legend_list, r)], location="center")
    p.add_layout(legend, 'right')

    # y axis
    p.y_range.start = 0
    if use_percentages:
        p.yaxis.axis_label = '% of oocytes'
        p.y_range.end = 100
    else:
        p.yaxis.axis_label = 'Number of oocytes'

    # x axis
    p.xaxis.axis_label = xlabel
    p.x_range.range_padding = 0.05
    p.axis.minor_tick_line_color = None

    show(p)
