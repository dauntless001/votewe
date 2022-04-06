# Generated by Django 3.2 on 2022-04-05 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
                ('entered_by', models.CharField(max_length=50)),
                ('ip_address', models.GenericIPAddressField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=15)),
                ('abbreviation', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
                ('entered_by', models.CharField(max_length=50)),
                ('ip_address', models.GenericIPAddressField()),
                ('lga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.lga')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('number', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('entered_by', models.CharField(max_length=40)),
                ('ip_address', models.GenericIPAddressField()),
                ('lga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.lga')),
                ('ward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.ward')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='lga',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.state'),
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.IntegerField()),
                ('polling_unit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='poll.pollingunit')),
            ],
        ),
    ]