#import datetime
from django.db import models
#import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # def _str_(self):
    #     return self.question_text
    pub_date = models.DateTimeField('date published')



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class backup(models.Model):
    # id = models.IntegerField()
    # id = models.AutoField(primary_key=True)
    database_name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    backup_type = models.CharField(max_length=30)
    backup_size_mb = models.FloatField()
    compress_size_mb = models.FloatField()
    physical_device_name = models.CharField(max_length=600)
    user_name = models.CharField(max_length=100)


class backup_test(models.Model):
    # id = models.IntegerField()
    id = models.AutoField(primary_key=True)
    database_name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    backup_type = models.CharField(max_length=30)
    backup_size_mb = models.FloatField()
    compress_size_mb = models.FloatField()
    physical_device_name = models.CharField(max_length=600)
    user_name = models.CharField(max_length=100)


#class Target(models.Model):
    #bak_type = ((1,'mysql'),(2,'sqlserver'));
    #type =  models.IntegerField(null=True,blank=True,choice=bak_type)

