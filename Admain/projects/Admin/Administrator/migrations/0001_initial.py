from django.db import migration, models

class Migration(migrations.Migration):

    initial =True

    dependencies = [

    ]
    operation = [
        migrations.CreateModel(
            name ='Administrator'
            fiels=[
               ('sId',models.IntegerField()),
                ('f_name',models.CharField(max_length=100))'
                ('l_name'models.EmailField(max_length=100)),
                ('email',models.CharField(max_length=100)),

            ],

        ),

    ]