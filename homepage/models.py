from django.db import models


class DiaryEntry(models.Model):

    text = models.TextField(max_length=150)
    happiness = models.IntegerField()
    stress = models.IntegerField()
    energy = models.IntegerField()


class MinorUser(models.Model):

    name = models.TextField(max_length=20)
