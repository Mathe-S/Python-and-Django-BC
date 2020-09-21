from faker import faker
from first_app.models import Topic, Webpage, AccessRecords
import random
import django
import os
os.environ.setdefault('DJANGO_SETTING_MODULE', 'first_project.settings')

django.setup()

# fake pop script

fakegen = faker()

topics = ['Search', 'Social', 'Games', 'News', 'Marketplace']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
