from util.filename import uncamel
from logger import Logger
from collections import defaultdict

extra_labels = defaultdict(str,	{	'string'	:	'S',
                                  'datetime'	:	'T'})


class CsvLogger(Logger):

    def __init__(self, world, file_path, labels, example_data):
        if file_path == None:
            self.valid = False
        else:
            self.valid = True
            self.world = world
            self.file_path = file_path + \
                uncamel(self.world.__class__.__name__) + '_logger.csv'
            self.labels = labels
            self.example_data = example_data
            self.set_meta_data()

    def log(self, data):
        if self.valid:
            file = open(self.file_path, 'a')
            file.write(list_to_csv(data))
            file.close()

    # """Private"""
    def set_meta_data(self):
        file = open(self.file_path, 'w+')
        file.write(list_to_csv(self.labels))
        types = map((lambda x: type(x).__name__), self.example_data)
        file.write(list_to_csv(types))
        file.write(list_to_csv(map((lambda x: extra_labels[x]), types)))
        file.close()


def list_to_csv(lst):
    return ','.join(map(str, lst)) + '\n'
