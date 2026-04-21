"""Data migration to copy profiles to the new profiles app."""

from django.db import migrations


def copy_profiles_data(apps, schema_editor):
    """Copy profile data from the old app to the new profiles app.

    Args:
        apps: Django apps registry at migration time.
        schema_editor: Database schema editor provided by Django.
    """
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    NewProfile = apps.get_model("profiles", "Profile")

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            user_id=old_profile.user_id,
            favorite_city=old_profile.favorite_city,
        )


class Migration(migrations.Migration):
    """Migration that copies profile data into the new app."""

    dependencies = [
        ("oc_lettings_site", "0001_initial"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_profiles_data, migrations.RunPython.noop),
    ]
