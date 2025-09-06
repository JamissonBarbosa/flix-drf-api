import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):
    help = "Import actors from an external source"

    def add_arguments(self, parser):

        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do Arquivo csv com os atores',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nacionality = row['nationality']

                self.stdout.write(self.style.NOTICE(f"Importing actor: {name})"))

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nacionality=nacionality,
                )
        self.stdout.write(self.style.SUCCESS('Actors imported successfully.'))
        #self.stdout.write(f"Importing actor: {row['name']}, Birthday: {row['birthday']}, Nationality: {row['nationality']}")