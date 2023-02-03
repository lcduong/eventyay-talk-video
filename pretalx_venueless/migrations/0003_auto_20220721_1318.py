# Generated by Django 3.2.10 on 2022-07-21 13:18

from django.db import migrations, models
import i18nfield.fields


class Migration(migrations.Migration):
    dependencies = [
        ("pretalx_venueless", "0002_data"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="venuelesssettings",
            name="return_url",
        ),
        migrations.AddField(
            model_name="venuelesssettings",
            name="audience",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="venuelesssettings",
            name="issuer",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="venuelesssettings",
            name="join_start",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="venuelesssettings",
            name="join_text",
            field=i18nfield.fields.I18nTextField(null=True),
        ),
        migrations.AddField(
            model_name="venuelesssettings",
            name="join_url",
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name="venuelesssettings",
            name="secret",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="venuelesssettings",
            name="show_join_link",
            field=models.BooleanField(default=False),
        ),
    ]
