import csv
import os
from codepoint.models import CodePoint

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Import OS Code Point Open data"

    def add_arguments(self, parser):
        parser.add_argument('--datadir', nargs=1, required=False)

    def handle(self, *args, **options):

        count = 0
        bulk_insert = 250
        codepoints = []

        if options['datadir']:
            datadir = options['datadir'][0]

        for root, dir, files in os.walk(datadir):
            for file in files:
                if file.endswith(".csv"):
                    with open(os.path.join(root, file), 'r') as csvfile:
                        cpreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                        for cpline in cpreader:
                            if len(cpline) != 10:
                                print("Unknown line (skipped): %s" % cpline)
                                next

                            codepoint = CodePoint(postcode=cpline[0].strip(), pos_quality=cpline[1], eastings=cpline[2], northings=cpline[3], country_code=cpline[4], nhs_regional_ha_code=cpline[5], nhs_ha_code=cpline[6], admin_county_code=cpline[7], admin_district_code=cpline[8], admin_ward_code=cpline[9])
                            codepoints.append(codepoint)

                            if count > bulk_insert:
                                CodePoint.objects.bulk_create(codepoints)
                                codepoints = []
                                count = 0
                            else:
                                count += 1

                        if count > 0:
                                CodePoint.objects.bulk_create(codepoints)
