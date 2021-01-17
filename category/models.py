from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)

class Category(models.Model):
    category = models.CharField(max_length=30, blank=True, null=True)
    Task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
