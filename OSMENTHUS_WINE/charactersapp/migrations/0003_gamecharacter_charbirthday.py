# Generated by Django 3.2.9 on 2022-03-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charactersapp', '0002_alter_gamecharacter_charactername'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamecharacter',
            name='charBirthday',
            field=models.DateField(default='1984-05-05'),
        ),
    ]
