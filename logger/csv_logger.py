from util.filename import uncamel
from logger import Logger
from collections import defaultdict

extra_labels = defaultdict(str,	{	'string'	:	'S',
                                  'datetime'	:	'T'})


class CsvLogger(Logger):

    def __init__(self, config):
        if config['path'] == None:
            print 'No path Set'
            self.valid = False
        else:
            self.valid = True
            self.file_path = config['path']
            self.labels = config['labels']
            self.types = config['types']
            self.set_meta_data()

    def log(self, data):
        if self.valid and len(data) == len(self.labels):
            file = open(self.file_path, 'a')
            file.write(list_to_csv(data))
            file.close()

    # """Private"""
    def set_meta_data(self):
        file = open(self.file_path, 'w+')
        file.write(list_to_csv(self.labels))
        file.write(list_to_csv(self.types))
        file.write(list_to_csv(map((lambda x: extra_labels[x]), self.types)))
        file.close()


def list_to_csv(lst):
    return ','.join(map(str, lst)) + '\n'
