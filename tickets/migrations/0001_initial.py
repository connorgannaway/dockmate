# Generated by Django 3.1 on 2021-01-06 00:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=4)),
                ('slip', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField(default=0)),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('timeDue', models.DateTimeField()),
                ('completed', models.BooleanField()),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.boat')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.customer')),
            ],
        ),
        migrations.CreateModel(
            name='TicketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=25)),
                ('description', models.TextField(blank='true')),
                ('completed', models.BooleanField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
            ],
        ),
        migrations.AddField(
            model_name='boat',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.customer'),
        ),
    ]
