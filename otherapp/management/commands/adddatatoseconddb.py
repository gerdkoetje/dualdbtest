from django.core.management.base import BaseCommand, CommandError
from otherapp.models import TestModel9, TestModel8
from seconddbapp.models import TestModel3


class Command(BaseCommand):

    def handle(self, *args, **options):


        # TESTING ON default db

        testing1 = TestModel8.objects.all()
        print(testing1)

        testing = TestModel8.objects.values('testmodel9__lastpath')
        print(testing)


        # TESTING ON seconddb

        testing1 = TestModel3.objects.all()
        print(testing1)

        testing = TestModel3.objects.values('testmodel4__lastpath')
        print(testing)




