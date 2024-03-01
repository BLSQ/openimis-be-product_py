# Generated by Django 3.0.14 on 2021-11-03 10:46

from django.db import migrations
from core.models import RoleRight, Role


def forwards_func(apps, schema_editor):
    # Add enrollment officer right to read location data
    # Enrollment officer is predefined system role with id 1
    eo_roles = Role.objects.filter(is_system=1, validity_to__isnull=True)
    # Required Role ID is gql_query_products_perm (121001)
    right_id = 121001
    for eo_role in eo_roles:
        RoleRight(
            role_id=eo_role.id,
            right_id=right_id,
            audit_user_id=None,
        ).save()
        
        



def reverse_func(apps, schema_editor):
    # Same data as in forward function
    eo_roles = Role.objects.filter(is_system=1, validity_to__isnull=True)
    right_id = 121001
    RoleRight.objects.filter(role__in=eo_roles, right_id=right_id, validity_to__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_productmutation"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
