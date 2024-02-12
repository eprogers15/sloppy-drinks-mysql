from django.db import models

# Create your models here.
class Ingredient(models.Model):
    """Model representing a drink ingredient"""
    name = models.CharField(max_length=100, primary_key=True, help_text='Enter an ingredient name (e.g. Simple Syrup)')

