from django.db import models

class TestModel3(models.Model):
    naam = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = 'seconddbapp'
        managed = True
        db_table = 'otherapp_testmodel3'



class TestModel4(models.Model):
    user = models.OneToOneField(TestModel3, unique=True, blank=True, null=True, on_delete=models.SET_NULL)
    lastpath = models.TextField(blank=True)
    memberstatus = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = 'seconddbapp'
        managed = True
        db_table = 'otherapp_testmodel4'