# Generated by Django 5.1.5 on 2025-02-27 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_coursetag_enrollment_lesson_studentperformance_tag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='submitted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
