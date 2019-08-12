# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Topstoryinfo(models.Model):
    story_id = models.CharField(unique=True, max_length=10)
    username = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    score = models.CharField(max_length=10, blank=True, null=True)
    story_desc = models.CharField(max_length=245, blank=True, null=True)
    story_type = models.CharField(max_length=10, blank=True, null=True)
    time = models.CharField(max_length=10, blank=True, null=True)
    sentiment = models.CharField(max_length=10, blank=True, null=True)
    istrending = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topstoryinfo'
