from django.core.management.base import BaseCommand
from base.models import BlockedIps




class Command(BaseCommand):
    help = "All blocked ips cleaned"


    def handle(self, *args, **options):
        x = BlockedIps.objects.all()
        x.delete()