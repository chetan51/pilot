from logger import Logger
import os


class CsvLogger(Logger):

    def __init__(self, config, path=None):
        Logger.__init__(self, config)

        if not path:
            self.is_valid = False
            return

        self.file_path = os.path.abspath(path)
        self.is_valid = True
        self.file = open(self.file_path, 'w+')
        self.write_headers()

    def log(self, state, action, prediction):
        if not self.is_valid:
            return

        self.file.write(list_to_csv(
            dict_to_list(state, self.keys['state']) +
            dict_to_list(action, self.keys['action']) +
            prediction.values()
        ))

    def write_headers(self):
        self.file.write(list_to_csv(self.labels))
        self.file.write(list_to_csv(self.types))
        self.file.write(list_to_csv(
            map((lambda x: ""), self.types))
        )


def list_to_csv(lst):
    return ','.join(map(str, lst)) + '\n'


def dict_to_list(dict, keys):
    return map((lambda x: dict[x]), keys)
