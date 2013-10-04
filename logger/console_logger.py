from logger import Logger
from collections import defaultdict


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
