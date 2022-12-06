# Generated by Django 4.1.3 on 2022-11-20 14:05

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=25),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='cc_exp_month',
            field=models.CharField(choices=[('Month', 'Month'), ('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='Month', max_length=25),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='cc_exp_year',
            field=models.CharField(choices=[('Year', 'Year'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029')], default='Month', max_length=25),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='Unites States Of America', max_length=2),
        ),
    ]
