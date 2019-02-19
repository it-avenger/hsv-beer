# Generated by Django 2.1.7 on 2019-02-17 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0012_auto_20190217_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeerAlternateName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManufacturerAlternateName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='automatic_updates_blocked',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='automatic_updates_blocked',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manufactureralternatename',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternate_names', to='beers.Manufacturer'),
        ),
        migrations.AddField(
            model_name='beeralternatename',
            name='beer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternate_names', to='beers.Beer'),
        ),
    ]
