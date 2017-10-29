from os import walk

from django.core import management

# Utility functions for testing


def load_initial_data():

    f = []

    for (dir_path, dir_name, file_name) in walk('bmcore/fixtures/'):
        f.extend(file_name)

        break

    f.sort(key=lambda x: x.split()[-1])

    for item in f:
        management.call_command('loaddata', 'bmcore/fixtures/{0}'.format(item))