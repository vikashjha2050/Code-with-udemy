import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tasks.settings')
django.setup()

import random
from task1.models import udb,userdb
from faker import Faker

fakeobject=Faker('hi_IN')
def adduserfirstname():
    for i in range(10):
        t=udb.objects.get_or_create(firstname=fakeobject.name())

def adduserdata():
    for i in range(10):
        t=userdb.objects.get_or_create(firstname=fakeobject.name(),lastname=fakeobject.name(),email=fakeobject.email())[0]

if __name__=='__main__':
    adduserdata()
