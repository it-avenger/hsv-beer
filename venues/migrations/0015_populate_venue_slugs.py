# Generated by Django 2.2 on 2019-04-26 17:00

from django.db import migrations
from django.db.models import Q


def populate_slugs(apps, schema_editor):
    slugs = {
        'Straight to Ale': 'straight-to-ale',
        'Wish You Were Beer Campus 805': 'wish-you-were-beer',
        'Old Town Beer Exchange': 'otbx',
        'Rocket City Craft Beer': 'rocket-city-craft-beer',
        'Whole Foods': 'whole-foods-hsv',
        'Liquor Express': 'liquor-express',
        'Wagon Wheel': 'wagon-wheel',
        'The Open Bottle': 'open-bottle',
        'The Nook': 'nook',
        'Das Stahl Bierhaus': 'das-stahl-bierhaus',
        'The Casual Pint - Providence': 'casual-pint-hsv',
        'Yellowhammer Brewery': 'yellowhammer',
        'Madison Taproom': 'madison-taproom',
        'Mad Malts Brewing': 'mad-malts',
        'The Stem and Stein': 'stem-and-stein',
        'Blue Pants Brewery': 'blue-pants',
    }
    venues = apps.get_model('venues.Venue').objects.filter(
        Q(slug__isnull=True) | Q(slug=''),
        name__in=slugs.keys(),
    )
    for venue in venues:
        venue.slug = slugs[venue.name]
        print(f'setting {venue.name} to {venue.slug}')
        venue.save()


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0014_venue_slug'),
    ]

    operations = [
        migrations.RunPython(populate_slugs, migrations.RunPython.noop),
    ]