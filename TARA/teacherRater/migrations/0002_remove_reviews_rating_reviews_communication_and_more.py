# Generated by Django 4.0.3 on 2022-04-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherRater', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='rating',
        ),
        migrations.AddField(
            model_name='reviews',
            name='communication',
            field=models.PositiveSmallIntegerField(choices=[(1, '1|Really bad communication'), (2, '2|Bad communication'), (3, '3|Communicates well'), (4, '4|Communicates really well'), (5, '5|Communicates clearly and often')], default=1),
        ),
        migrations.AddField(
            model_name='reviews',
            name='teachingMethod',
            field=models.PositiveSmallIntegerField(choices=[(1, '1|Horrible'), (2, '2|Bad'), (3, '3}Average'), (4, '4|Good'), (5, '5|Amazing')], default=1),
        ),
        migrations.AddField(
            model_name='reviews',
            name='understandability',
            field=models.PositiveSmallIntegerField(choices=[(1, '1|Very hard to understand'), (2, '2|Hard to understand'), (3, '3|Understandable'), (4, '4|Easy to understand'), (5, '5|I understand everything')], default=1),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='grade',
            field=models.IntegerField(choices=[(7, 'Grade 7'), (8, 'Grade 8'), (9, 'Grade 9'), (10, 'Grade 10'), (11, 'Grade 11'), (12, 'Grade 12'), (0, 'Other')], default=0),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='comment',
            field=models.TextField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='subjects',
            field=models.CharField(choices=[('ACC', 'Akuntansi'), ('ART', 'Art'), ('BI', 'Bahasa Indonesia'), ('BS', 'Biblical Studies'), ('BIO', 'Biologi'), ('CIV', 'Civics'), ('ECO', 'Ekonomi'), ('ENG', 'English'), ('PHYS', 'Fisika'), ('GEO', 'Geologi'), ('CHEM', 'Kimia'), ('COMP', 'Komputer'), ('MAN', 'Mandarin'), ('MATH', 'Math'), ('MUS', 'Music'), ('HIS', 'Sejarah'), ('SOS', 'Sosiologi'), ('IDK', 'Other')], default='IDK', max_length=4),
        ),
    ]