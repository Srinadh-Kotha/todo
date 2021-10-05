# Generated by Django 3.2.5 on 2021-10-05 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='number_of_students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_students', models.IntegerField()),
            ],
            options={
                'db_table': 'number_of_students',
            },
        ),
        migrations.CreateModel(
            name='signupdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('reenterpassword', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'signupdetails',
            },
        ),
        migrations.CreateModel(
            name='staff_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=25)),
                ('subject', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'staff_details',
            },
        ),
        migrations.CreateModel(
            name='student_enroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=25)),
                ('course', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'student_enroll',
            },
        ),
        migrations.CreateModel(
            name='trash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=300)),
                ('start_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.signupdetails')),
            ],
            options={
                'db_table': 'trash',
            },
        ),
        migrations.CreateModel(
            name='todo_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=300)),
                ('start_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.signupdetails')),
            ],
            options={
                'db_table': 'todo_list',
            },
        ),
        migrations.CreateModel(
            name='enrolled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=25)),
                ('course', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.signupdetails')),
            ],
            options={
                'db_table': 'enrolled',
            },
        ),
    ]
