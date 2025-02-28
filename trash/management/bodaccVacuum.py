
import os
import re
import shutil
import tarfile
import xml.etree.ElementTree as ET

import requests

from mighty.functions import get_logger
from mighty.management import ModelBaseCommand

logger = get_logger()


class Command(ModelBaseCommand):
    directory = '/tmp/bodacc/'
    urls = {
        'base': 'https://echanges.dila.gouv.fr/OPENDATA/BODACC/',
        'history': 'https://echanges.dila.gouv.fr/OPENDATA/BODACC/FluxHistorique/'
    }

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--date', default=None)
        parser.add_argument('--history', default=None)

    def handle(self, *args, **options):
        self.date = options.get('date')
        self.history = options.get('history')
        super(ModelBaseCommand, self).handle(*args, **options)

    def do(self):
        if self.history: self.get_history(self.history)

    def get_files(self, directory):
        for file in os.listdir(directory):
            if os.path.isdir(file):
                self.get_files(directory + file)
            self.extract_tazfile(file, directory)

    def extract_tarfile(self, fil, year):
        logger.info(f'Extraction to: {fil}')
        tf = tarfile.open(fil)
        tf.extractall(self.directory)
        self.get_files(f'{self.directory + year}/')

    def extract_tazfile(self, fil, directory):
        logger.info(f'Extraction to: {directory}' + fil)
        os.system(f'tar -C {self.directory} -xf {directory + fil}')
        self.read_xmlfiles()
        os.remove(directory + fil)

    def read_xmlfiles(self):
        for file in os.listdir(self.directory):
            if file[-3:] == 'xml':
                filxml = self.directory + file
                logger.info(f'Read xml: {filxml}')
                tree = ET.parse(filxml)
                tree.getroot()
                os.remove(filxml)

    def get_file(self, fileurl, year):
        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)
        if not os.path.isdir(self.directory + year):
            os.mkdir(self.directory + year)
        logger.info(f'Downloading: {fileurl}')
        r = requests.get(fileurl)
        fil = fileurl.split('/')[-1]
        filepath = self.directory + fil
        open(filepath, 'wb').write(r.content)
        if fileurl[-3:] == 'tar': self.extract_tarfile(filepath, year)
        elif fileurl[-3:] == 'taz':  self.extract_tazfile(fil, self.directory)
        shutil.rmtree(self.directory)

    def get_subdir(self, subdir, year):
        logger.info(f'Browse: {subdir}')
        response = requests.get(subdir).text
        histories = re.compile(r'href="(.+taz)"').findall(response)
        for history in histories:
            logger.info(f'Downloading: {history}')
            self.get_file(subdir + history, year)

    def get_history(self, history):
        response = requests.get(self.urls['history']).text
        histories = re.compile(r'href="(.+tar|\d+/)"').findall(response)
        history = history.split('-')
        for h in range(int(history[0]), int(history[1])):
            for history in histories:
                if str(h) in history:
                    logger.info(f'Treat year: {h}')
                    if 'bodacc' in history.lower(): self.get_file(self.urls['history'] + history, str(h))
                    else: self.get_subdir(self.urls['history'] + history, str(h))
                    break
