# Generated by Django 5.0.1 on 2024-02-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("issues_tracking", "0002_rename_project_id_contributor_project_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="description",
            field=models.CharField(max_length=1000),
        ),
    ]