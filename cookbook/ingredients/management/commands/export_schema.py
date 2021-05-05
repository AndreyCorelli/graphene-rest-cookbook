from django.core.management import BaseCommand
from graphql.utils import schema_printer

from cookbook.schema import schema


class Command(BaseCommand):
    help = 'Export GraphQL schema'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            type=str)

    def handle(self, *args, **options):
        my_schema_str = schema_printer.print_schema(schema)
        path = options.get('output', 'schema.json')
        with open(path, 'w') as fp:
            fp.write(my_schema_str)
            fp.close()
