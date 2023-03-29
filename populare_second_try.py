import os 
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
 
import django
django.setup()
 
import random
from second_try.models import AccessRecord, Topic, Webpage
from faker import Faker
 


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]


