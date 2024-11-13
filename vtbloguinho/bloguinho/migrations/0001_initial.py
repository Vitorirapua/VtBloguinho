# Generated by Django 5.1.3 on 2024-11-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('title', models.CharField(max_length=127)),
                ('content', models.TextField()),
                ('expires', models.DateTimeField()),
                ('status', models.CharField(choices=[('on', 'Online'), ('off', 'Offline'), ('del', 'Apagado')], default='on', max_length=10)),
            ],
        ),
    ]
