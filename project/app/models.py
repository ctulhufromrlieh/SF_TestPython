from django.db import models

# Create your models here.
# class Word(models.Model):
#     value = models.CharField(max_length=255, unique=True)

#     def __str__(self):
#         return self.value.name

class WordFile(models.Model):
    file = models.FileField()
    search_word = models.CharField(max_length=255, default="")
    word_count = models.IntegerField(default=-1)
