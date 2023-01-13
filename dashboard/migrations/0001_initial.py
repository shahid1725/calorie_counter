# Generated by Django 4.1.5 on 2023-01-13 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foodtracker', '0002_food_food_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('quantity', models.DecimalField(decimal_places=2, default=100.0, max_digits=7)),
                ('calories', models.IntegerField(default=0, null=True)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('food_image', models.ImageField(upload_to='images/')),
                ('category_food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_food', to='foodtracker.foodcategory')),
            ],
        ),
    ]
