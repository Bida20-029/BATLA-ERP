# Generated by Django 4.1.7 on 2023-06-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Approval_Signature_1',
            field=models.FileField(blank=True, default='NULL', null=True, upload_to='pdfs/'),
        ),
        migrations.AddField(
            model_name='payment',
            name='Approval_Signature_2',
            field=models.FileField(blank=True, default='NULL', null=True, upload_to='pdfs/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default=1, max_length=10, primary_key=True, serialize=False),
        ),
    ]
