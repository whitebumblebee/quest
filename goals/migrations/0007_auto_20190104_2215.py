# Generated by Django 2.1.4 on 2019-01-04 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_remove_goal_percentage_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the goal', max_length=255)),
                ('url', models.URLField(help_text='The URL of this task')),
            ],
        ),
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.TextField(blank=True, help_text='The description of the goal', null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.Goal'),
        ),
    ]
