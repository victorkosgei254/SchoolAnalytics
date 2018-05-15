from django.db import models

# Create your models here.
'''Designing the DB
Seperating each subjects and in each have a season
Any class here represents a Table in the Database
'''

class Students():
    #this class is to be used during registering new students to database,can be done by mini-admin or public given
    #special access by mini admin through a generated url.
    #inputting names can be automated where user can choose to upload a text file
    firstname = models.CharField(max_length = 20)
    lastname  = models.CharField(max_length = 20)
    # graduation_date = models.
    #id to be generated automatically


    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return "{}".format(self.firstname)

class School():
    school_name = models.CharField(max_length = 144)
    school_email = models.CharField(max_length =144 )
    school_address =models.CharField(max_length = 144)
    school_website = models.CharField(max_length = 144 )
    school_telephone = models.CharField(max_length = 12 )
    # school_admin_signature = models.CharField(max_length =  ) an image upload{to be used while generating school ID}
    #school_logo = image upload
    class Meta:
        verbose_name_plural = 'School'

    def __str__(self):
        return "{}".format(self.school_name)

class Course():
    def __init__(self,course_name):
        self.course_name = course_name
        #here an algo to check if the course is already available
        # if course_name.upper() #is in :
            #call a function to add the student to the already Table
        # else:
            #call a function to create a table and add students to it
