import csv
from health.models import HealthWeight, HealthBMI

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Import HSE Health stats"

    def add_arguments(self, parser):
        parser.add_argument('--hse_bmi', nargs=1, required=False)
        parser.add_argument('--hse_weight', nargs=1, required=False)

    def handle(self, *args, **options):

        if options['hse_bmi']:
            csvfilename = options['hse_bmi'][0]

            if csvfilename.endswith(".csv"):
                with open(csvfilename, 'rb') as csvfile:
                    statsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    headers = statsreader.next()
                    for statsline in statsreader:
                        if statsline[0] == 'M':
                            gender = HealthBMI.MALE
                        elif statsline[0] == 'W':
                            gender = HealthBMI.FEMALE
                        elif statsline[0] == 'A':
                            gender = HealthBMI.ALL
                        else:
                            print("PARSE ERROR - UNKNOWN GENDER")
                            exit(1)

                        if statsline[1] == '16-24':
                            age = HealthBMI.AGE_16_TO_24
                        elif statsline[1] == '25-34':
                            age = HealthBMI.AGE_25_TO_34
                        elif statsline[1] == '35-44':
                            age = HealthBMI.AGE_35_TO_44
                        elif statsline[1] == '45-54':
                            age = HealthBMI.AGE_45_TO_54
                        elif statsline[1] == '55-64':
                            age = HealthBMI.AGE_55_TO_64
                        elif statsline[1] == '65-74':
                            age = HealthBMI.AGE_65_TO_74
                        elif statsline[1] == '75+':
                            age = HealthBMI.AGE_75_PLUS
                        elif statsline[1] == 'All':
                            age = HealthBMI.AGE_ALL
                        else:
                            print("PARSE ERROR - Unknown age")
                            exit(1)

                        if statsline[2] == 'Underweight':
                            bmi = HealthBMI.BMI_UNDERWEIGHT
                        elif statsline[2] == 'Normal':
                            bmi = HealthBMI.BMI_NORMAL
                        elif statsline[2] == 'Overweight':
                            bmi = HealthBMI.BMI_OVERWEIGHT
                        elif statsline[2] == 'Obese':
                            bmi = HealthBMI.BMI_OBESE
                        elif statsline[2] == 'Morbidly obese':
                            bmi = HealthBMI.BMI_MORBIDLY_OBESE
                        elif statsline[2] == 'Overweight including obese':
                            bmi = HealthBMI.BMI_OVERWEIGHT_OBESE
                        elif statsline[2] == 'Mean':
                            bmi = HealthBMI.BMI_MEAN
                        elif statsline[2] == 'Standard error of the mean':
                            bmi = HealthBMI.BMI_STDERR
                        elif statsline[2] == 'Base':
                            bmi = HealthBMI.BMI_BASE
                        elif statsline[2] == 'All':
                            bmi = HealthBMI.BMI_ALL
                        else:
                            print("PARSE ERROR - Unknown BMI: ", statsline[2])
                            exit(1)

                        print "Parsing line - ", statsline

                        year = 1993
                        for year_val in statsline[3:]:
                            if year_val == '-':
                                year_val = 0
                            health = HealthBMI(year=year, gender=gender, age=age, bmi=bmi, percentage=year_val)
                            year += 1
                            health.save()
