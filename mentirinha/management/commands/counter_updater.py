import time
from django.core.management.base import BaseCommand, CommandError
from mentirinha import tasks

class Command(BaseCommand):
    help = 'Update url accesses counter'

    def add_arguments(self, parser):
        parser.add_argument('--interval', type=int, default=60)

    def handle(self, *args, **options):
        while True:
            self.stdout.write(self.style.SUCCESS('Running counter updater'))
            tasks.consume_counter()
            time.sleep(options['interval'])
