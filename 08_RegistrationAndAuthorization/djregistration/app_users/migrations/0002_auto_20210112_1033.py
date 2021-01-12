from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import migrations

USER_GROUPS = ['auth_users', 'verified_users', 'moderators']


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [ migrations.RunPython(create_groups)
    ]
