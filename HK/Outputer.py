import re
import csv

class Outputer(object):
    def output_csv(self, data, year):
        name = '{}.csv'.format(year)
        with open(name, 'wb') as f:
            writer = csv.writer(f)
            for i in range(0, len(data)):
                writer.writerow(re.split(re.compile(r','), data[i]))