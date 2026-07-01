from django.core.management.base import BaseCommand
from dealers.models import Dealer


class Command(BaseCommand):
    help = 'Seed sample dealers'

    def handle(self, *args, **options):
        Dealer.objects.all().delete()
        dealers = [
            {'name': 'Kings Auto', 'state': 'Kansas', 'city': 'Wichita', 'address': '120 Main St', 'phone': '316-555-1100', 'email': 'sales@kingsauto.com'},
            {'name': 'Blue River Motors', 'state': 'Kansas', 'city': 'Overland Park', 'address': '400 Oak Ave', 'phone': '913-555-2200', 'email': 'contact@blueriver.com'},
            {'name': 'Sunset Auto Plaza', 'state': 'Missouri', 'city': 'Kansas City', 'address': '980 Sunset Blvd', 'phone': '816-555-3300', 'email': 'info@sunsetauto.com'},
        ]
        for item in dealers:
            Dealer.objects.create(**item)
        self.stdout.write(self.style.SUCCESS('Seeded dealers'))
