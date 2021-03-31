from django.db import models

# Create your models here.
class Todolist(models.Model):
	tasks=models.CharField(max_length=50)

	def __str__(self):
		return self.tasks