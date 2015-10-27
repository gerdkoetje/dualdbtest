from django.db import models

class TestModel8(models.Model):
    naam = models.CharField(max_length=255, blank=True)

class TestModel9(models.Model):
    user = models.OneToOneField(TestModel8, unique=True, blank=True, null=True, on_delete=models.SET_NULL)
    lastpath = models.TextField(blank=True)
    memberstatus = models.CharField(max_length=255, blank=True)
