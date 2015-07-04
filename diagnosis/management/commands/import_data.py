import csv
from diagnosis.models import AdmissionsByGender, AdmissionsByAge, SurgeryByGender

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Import yearly stats"

    def add_arguments(self, parser):
        parser.add_argument('--gender_primary_file', nargs=1, required=False)
        parser.add_argument('--gender_secondary_file', nargs=1, required=False)
        parser.add_argument('--age_primary_file', nargs=1, required=False)
        parser.add_argument('--age_secondary_file', nargs=1, required=False)
        parser.add_argument('--surgery_stats_file', nargs=1, required=False)

    def handle(self, *args, **options):

        if options['gender_primary_file']:
            csvfilename = options['gender_primary_file'][0]

            if csvfilename.endswith(".csv"):
                with open(csvfilename, 'r') as csvfile:
                    statsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    headers = next(statsreader)
                    for statsline in statsreader:
                            diagnosis = AdmissionsByGender(year=statsline[0], gender='M', admissions=statsline[2], diagnosis=AdmissionsByGender.PRIMARY)
                            diagnosis.save()
                            diagnosis = AdmissionsByGender(year=statsline[0], gender='F', admissions=statsline[3], diagnosis=AdmissionsByGender.PRIMARY)
                            diagnosis.save()
                            diagnosis = AdmissionsByGender(year=statsline[0], gender='U', admissions=statsline[4], diagnosis=AdmissionsByGender.PRIMARY)
                            diagnosis.save()

        if options['gender_secondary_file']:
            csvfilename = options['gender_secondary_file'][0]

            if csvfilename.endswith(".csv"):
                with open(csvfilename, 'r') as csvfile:
                    statsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    headers = next(statsreader)
                    for statsline in statsreader:
                            diagnosis = AdmissionsByGender(year=statsline[0], gender='M', admissions=statsline[2], diagnosis=AdmissionsByGender.SECONDARY)
                            diagnosis.save()
                            diagnosis = AdmissionsByGender(year=statsline[0], gender='F', admissions=statsline[3], diagnosis=AdmissionsByGender.SECONDARY)
                            diagnosis.save()

        if options['age_primary_file']:
            csvfilename = options['age_primary_file'][0]

            if csvfilename.endswith(".csv"):
                with open(csvfilename, 'r') as csvfile:
                    statsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    next(statsreader)
                    for statsline in statsreader:
                            diagnosis = AdmissionsByAge(year=statsline[0], total=statsline[1], age_under_16=statsline[2], age_16_to_24=statsline[3], age_25_to_34=statsline[4], age_35_to_44=statsline[5], age_45_to_54=statsline[6], age_55_to_64=statsline[7], age_65_to_74=statsline[8], age_75_and_over=statsline[9], age_unknown=statsline[10], diagnosis=AdmissionsByAge.PRIMARY)

                            diagnosis.save()

        if options['age_secondary_file']:
            csvfilename = options['age_secondary_file'][0]

            if csvfilename.endswith(".csv"):
                with open(csvfilename, 'r') as csvfile:
                    statsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    next(statsreader)
                    for statsline in statsreader:
                            diagnosis = AdmissionsByAge(year=statsline[0], total=statsline[1], age_under_16=statsline[2], age_16_to_24=statsline[3], age_25_to_34=statsline[4], age_35_to_44=statsline[5], age_45_to_54=statsline[6], age_55_to_64=statsline[7], age_65_to_74=statsline[8], age_75_and_over=statsline[9], age_unknown=0, diagnosis=AdmissionsByAge.SECONDARY)

                            diagnosis.save()

        if options['surgery_stats_file']:
            csvfilename = options['surgery_stats_file'][0]

            if csvfilename.endswith(".csv"):
                with open(csvfilename, 'r') as csvfile:
                    statsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#                    headers = next(statsreader)
                    for statsline in statsreader:
                        surgery = SurgeryByGender(code=statsline[0], year=statsline[1], gender='M', admissions=statsline[3])
                        surgery.save()

                        surgery = SurgeryByGender(code=statsline[0], year=statsline[1], gender='F', admissions=statsline[4])
                        surgery.save()

                        surgery = SurgeryByGender(code=statsline[0], year=statsline[1], gender='U', admissions=statsline[5])
                        surgery.save()
