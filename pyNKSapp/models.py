from django.db import models

# Create your models here.

class signupdetails(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    dob=models.CharField(max_length=30)
    password=models.CharField(max_length=50)
    reenterpassword=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    class Meta:
        db_table="signupdetails"
    
class todo_list(models.Model):
    user=models.ForeignKey(signupdetails,on_delete=models.CASCADE)
    heading=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    comments=models.CharField(max_length=300)
    start_date=models.CharField(max_length=20)
    end_date=models.CharField(max_length=20)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="todo_list"

class trash(models.Model):
    user=models.ForeignKey(signupdetails,on_delete=models.CASCADE)
    heading=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    comments=models.CharField(max_length=300)
    start_date=models.CharField(max_length=20)
    end_date=models.CharField(max_length=20)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="trash"



class enrolled(models.Model):
    user=models.ForeignKey(signupdetails,on_delete=models.CASCADE)
    institute=models.CharField(max_length=25)
    course=models.CharField(max_length=25)
    class Meta:
        db_table="enrolled"

class number_of_students(models.Model):
    no_of_students=models.IntegerField()
    class Meta:
        db_table="number_of_students"



class staff_details(models.Model):
    staff_name=models.CharField(max_length=25)
    subject=models.CharField(max_length=25)
    class Meta:
        db_table="staff_details"

class student_enroll(models.Model):
    institute=models.CharField(max_length=25)
    course=models.CharField(max_length=25)
    class Meta:
        db_table="student_enroll"




