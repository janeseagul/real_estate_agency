# Generated by Django 2.2.24 on 2023-03-26 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]
    def define_new_buildings(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        for flat in Flat.objects.all().iterator():
            flat.new_building = flat.construction_year >= 2015
            flat.save()

    operations = [
        migrations.RunPython(define_new_buildings)
    ]