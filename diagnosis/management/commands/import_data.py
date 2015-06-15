import csv
from diagnosis.models import Admissions, AdmissionsByAge

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Import yearly stats"

    def add_arguments(self, parser):
        parser.add_argument('--yearly_stats_file', nargs=1, required=False)
        parser.add_argument('--age_stats_file', nargs=1, required=False)

    def handle(self, *args, **options):

        if options['yearly_stats_file']:
            csvfilename = options['yearly_stats_file'][0]

            if csvfilename.endswith(".csv"):
                with open(csvfilename, 'rb') as csvfile:
                    statsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#                    headers = statsreader.next()
                    for statsline in statsreader:
                            diagnosis = Admissions(year=statsline[0], gender='M', admissions=statsline[2])
                            diagnosis.save()
                            diagnosis = Admissions(year=statsline[0], gender='F', admissions=statsline[3])
                            diagnosis.save()
                            diagnosis = Admissions(year=statsline[0], gender='U', admissions=statsline[4])
                            diagnosis.save()

        if options['age_stats_file']:
            csvfilename = options['age_stats_file'][0]

            if csvfilename.endswith(".csv"):
                with open(csvfilename, 'rb') as csvfile:
                    statsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    statsreader.next()
                    for statsline in statsreader:
                            diagnosis = AdmissionsByAge(year=statsline[0], total=statsline[1], age_under_16=statsline[2], age_16_to_24=statsline[3], age_25_to_34=statsline[4], age_35_to_44=statsline[5], age_45_to_54=statsline[6], age_55_to_64=statsline[7], age_65_to_74=statsline[8], age_75_and_over=statsline[9], age_unknown=statsline[10])

                            diagnosis.save()
