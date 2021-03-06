# Generated by Django 3.2.10 on 2022-01-02 11:13

from django.db import migrations

def load_categories(apps,schema_editor):
    Cat= apps.get_model('auctions','Categories')
    categories=['Books','Electronics','Fashion','Accessories','Tools','Toys','Others']
    for category in categories:
        c= Cat(category_name=category)
        c.save()

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_user_first_name'),
    ]

    operations = [
        migrations.RunPython(load_categories)

    ]
