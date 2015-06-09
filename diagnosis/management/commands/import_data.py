import csv
from diagnosis.models import Admissions 

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Import yearly stats"

    def add_arguments(self, parser):
        parser.add_argument('--stats_file', nargs=1, required=True)

    def handle(self, *args, **options):

        if len(options['stats_file']) > 0:
            csvfilename = options['stats_file'][0]

            if csvfilename.endswith(".csv"):
                with open(csvfilename, 'rb') as csvfile:
                    statsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    headers = statsreader.next()
                    for statsline in statsreader:
                            diagnosis = Admissions(year=statsline[0], gender='M', admissions=statsline[2])
                            diagnosis.save()
                            diagnosis = Admissions(year=statsline[0], gender='F', admissions=statsline[3])
                            diagnosis.save()
                            diagnosis = Admissions(year=statsline[0], gender='U', admissions=statsline[4])
                            diagnosis.save()
