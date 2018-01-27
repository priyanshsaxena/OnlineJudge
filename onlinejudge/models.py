from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	user_name = models.CharField(max_length=100)
	user_rating = models.IntegerField(default=0)
	def __str__(self):
		return self.user_name

class Question(models.Model):
	question_name = models.CharField(max_length=100)
	question_description = models.CharField(max_length=10000)
	question_input_file = models.CharField(max_length=200)
	question_output_file = models.CharField(max_length=200)
	def __str__(self):
		return self.question_name

class Submission(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	submission_file = models.FileField(upload_to='documents/', default='background.gif')
	submission_status = models.CharField(max_length=50)
	submission_language = models.CharField(max_length=50)
	submission_time = models.FloatField(default=100.00)