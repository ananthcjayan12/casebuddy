# Generated by Django 5.1.6 on 2025-02-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_casequestionnaire_case_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='case_type',
        ),
        migrations.AddField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('CIVIL', 'Civil Law'), ('CRIMINAL', 'Criminal Law'), ('FAMILY', 'Family Law'), ('PROPERTY', 'Property Law'), ('CORPORATE', 'Corporate Law'), ('EMPLOYMENT', 'Employment Law'), ('IMMIGRATION', 'Immigration Law'), ('INTELLECTUAL', 'Intellectual Property'), ('TAX', 'Tax Law'), ('BANKRUPTCY', 'Bankruptcy Law'), ('PERSONAL_INJURY', 'Personal Injury'), ('ESTATE', 'Estate Planning'), ('ENVIRONMENTAL', 'Environmental Law'), ('CONSTITUTIONAL', 'Constitutional Law'), ('OTHER', 'Other')], default='OTHER', max_length=50),
        ),
    ]
