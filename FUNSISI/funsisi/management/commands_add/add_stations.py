'''
later if need be for adding so many stations we shall be using this script
from django.core.management.base import BaseCommand
from funsisi.models import Station

class Command(BaseCommand):
    help = 'Adds stations to the database manually'

    def handle(self, *args, **options):
        stations = [
            {'name': 'Karen', 'location': 'Nairobi', 'description': 'Description of Karen station.'},
            {'name': 'Runda', 'location': 'Nairobi', 'description': 'Description of Runda station.'},
            # Add more stations as needed when the company gets huge
        ]

        for station_data in stations:
            Station.objects.create(**station_data)

        self.stdout.write(self.style.SUCCESS('Stations added successfully.'))


  # upon success of this code it can be run by the command   python3 manage.py add_stations 

'''