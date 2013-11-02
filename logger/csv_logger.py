from logger import Logger
from collections import defaultdict

extra_labels = defaultdict(str,	{	'string'	:	'S',
                                  'datetime'	:	'T'})


class CsvLogger(Logger):

    def __init__(self, config):
        self.file_path = config['path']
        if not self.file_path:
            self.is_valid = False
            return

        self.is_valid = True
        self.config = config
        self.labels = config['labels']
        self.types = config['types']
        self.file = open(self.file_path, 'w+')
        self.write_headers()

    def log(self, state, action, prediction):
        if not self.is_valid:
            return

        self.file.write(list_to_csv(
            dict_to_list(state, self.config['keys']['state']) +
            dict_to_list(action, self.config['keys']['action']) +
            prediction.values()
        ))

    def write_headers(self):
        self.file.write(list_to_csv(self.labels))
        self.file.write(list_to_csv(self.types))
        self.file.write(list_to_csv(
            map((lambda x: extra_labels[x]), self.types))
        )


def list_to_csv(lst):
    return ','.join(map(str, lst)) + '\n'


def dict_to_list(dict, keys):
    return map((lambda x: dict[x]), keys)
