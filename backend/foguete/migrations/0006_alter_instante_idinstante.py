# Generated by Django 4.1 on 2023-11-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foguete", "0005_alter_voo_idvoo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instante",
            name="idInstante",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
