from django.db import models


class SqlServerConn(models.Model):
    Empname = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    salary = models.IntegerField()
