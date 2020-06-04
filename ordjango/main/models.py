# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TestDjango(models.Model):
    adapter = models.TextField(db_column='ADAPTER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    data_load = models.TextField(db_column='DATA_LOAD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sender = models.TextField(db_column='SENDER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    receiver = models.TextField(db_column='RECEIVER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    interface_name = models.TextField(db_column='INTERFACE_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type_error = models.TextField(db_column='TYPE_ERROR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    msg_id = models.TextField(db_column='MSG_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    error_text = models.TextField(db_column='ERROR_TEXT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    update_status = models.TextField(db_column='UPDATE_STATUS')  # Field name made lowercase. This field type is a guess.
    update_user = models.TextField(db_column='UPDATE_USER')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TEST_DJANGO'