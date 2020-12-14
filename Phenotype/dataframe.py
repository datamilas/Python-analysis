# dataframe.py


class ResultsDataFrame:
    def __init__(self, x_name, x_values, sample_size, data, legend):
        self.x_name = x_name
        self.x_values = list(x_values)
        self.sample_size = sample_size
        self.data = data
        self.legend = legend

    def get_sample_size(self, x_value):
        return self.sample_size[self.x_values.index(x_value)]
