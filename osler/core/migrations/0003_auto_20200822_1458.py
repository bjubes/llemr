# Generated by Django 3.0.5 on 2020-08-22 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import osler.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200806_1411'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'permissions': [('case_manage_Patient', 'Can act as a case manager.'), ('activate_Patient', 'Can in/activate patients')]},
        ),
        migrations.AlterField(
            model_name='historicalpatient',
            name='city',
            field=models.CharField(default='Kansas City', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalpatient',
            name='zip_code',
            field=models.CharField(default='64106', max_length=5, validators=[osler.core.validators.validate_zip]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(default='Kansas City', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='zip_code',
            field=models.CharField(default='64106', max_length=5, validators=[osler.core.validators.validate_zip]),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=100, validators=[osler.core.validators.validate_name])),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Gender')),
                ('languages', models.ManyToManyField(help_text='Specify here languages that are spoken at a level sufficient to be used for medical communication.', to='core.Language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]