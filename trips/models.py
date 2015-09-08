from django.db import models
#No imports are needed

# Create your models here.
class Trip(models.Model):
    trip_id = models.CharField(max_length=200)
    #http://stackoverflow.com/questions/323763/foreign-key-from-one-app-into-another-in-django
    # To refer to models defined in another application,
    # you must instead explicitly specify the application label.
    # For example, if the Manufacturer model above
    # is defined in another application called production, you'd need to use:
    #where users = name of app/folder
    #User = name of Class in models.py
    trip_fk = models.ForeignKey('users.User')
