from django.contrib.auth.models import User, Group, Permission
from django.db import migrations

GROUPS_PERMISSIONS = {'auth_users': [],
                      'verified_users': ['add_newsitem', 'change_newsitem', 'delete_newsitem', 'can_view_unverified'],
                      'moderators': ['change_newsitem', 'can_publish', 'can_verified_users', 'can_view_unverified']}


def create_groups_and_permissions(apps, schema_editor):
    for group, group_permissions in GROUPS_PERMISSIONS.items():
        new_group, created = Group.objects.get_or_create(name=group)
        for permission_code in group_permissions:
            permission = Permission.objects.get(codename=permission_code)
            new_group.permissions.add(permission)


class Migration(migrations.Migration):
    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [migrations.RunPython(create_groups_and_permissions),
                  ]



