from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=255, blank=False, null=False)
	price = models.FloatField()
	image = models.URLField()
	createdAt = models.DateTimeField(auto_now_add=True)
	updtedAt = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
