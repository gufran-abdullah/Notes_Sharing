from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserSignup(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	mobile = models.CharField(max_length=15,null=True)
	branch = models.CharField(max_length=50)
	role = models.CharField(max_length=20)

	def __str__(self):
		return self.user.username


class Notes(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	upload_date = models.CharField(max_length=30)
	branch = models.CharField(max_length=50)
	subject = models.CharField(max_length=30)
	notesfile = models.FileField(null=True)
	filetype = models.CharField(max_length=30)
	description = models.CharField(max_length=300,null=True)
	status = models.CharField(max_length=15)

	def __str__(self):
		return self.user.username+" ("+self.status+") "
