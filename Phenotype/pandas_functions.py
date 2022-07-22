import itertools


def filter_df(df, colnames, filters, filter_out=False):
    '''

    Filter panda dataframe

    Arguments
    ----------
    df: panda dataframe
    colnames: list or str 
        list or str with name(s) of column(s)
    filters: list or str 
        list or str with name(s) of value(s) in column, or list of lists if more than one column is to be considered
    filter_out: bool
        filter out rows containing specified values in specified columns, default=False

    Returns
    ---------
    filtered panda dataframe

    Examples of usage
    ---------
    filter_df(df, "Col1", "A")
    filter_df(df, "Col1", ["A"])
    filter_df(df, "Col1", ["A", "B"])
    filter_df(df, ["Col1", "Col2"], [["A"], [1]])
    filter_df(df, ["Col1", "Col2"], [["A", "B", "C"], [1, 2, 3]])
    filter_df(df, ["Col1", "Col2"], [["A", "B", "C"], [1, 2, 3]], filter_out=False)
    '''

    if type(colnames) != list:
        colnames = [colnames]
    if type(filters) != list:
        filters = [filters]

    if len(colnames) > 1:
        if filter_out:
            for index, colname in enumerate(colnames):
                if type(filters[index]) == list:
                    df = df[~df[colname].isin(filters[index])]
                else:
                    df = df[df[colname] != filters[index]]
        else:
            for index, colname in enumerate(colnames):
                if type(filters[index]) == list:
                    df = df[df[colname].isin(filters[index])]
                else:
                    df = df[df[colname] == filters[index]]

    elif len(colnames) == 1:
        if filter_out:
            df = df[~df[colnames[0]].isin(filters)]
        else:
            df = df[df[colnames[0]].isin(filters)]

    return df


def possible_combinations(df, colnames):
    '''
    Get possible combinations of values that occur in colnames columns

    Arguments
    ----------
    df: panda dataframe
    colnames: list
        list with names of columns

    Returns
    ---------
    list of dictionaries each containing one possible combination of values

    Examples of usage
    ---------
    possible_combinations(df, ["Col1", "Col2"])

    '''
    unique_values = [df[colname].unique() for colname in colnames]
    unique_values_iterator = itertools.product(*unique_values)
    combinations_dict_list = [dict(zip(colnames, i))
                              for i in unique_values_iterator]

    return combinations_dict_list
