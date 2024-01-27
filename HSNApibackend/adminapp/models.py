from django.db import models

# Create your models here.

class Hsn(models.Model):
    hsncode= models.CharField(max_length=255)
    hsndescription=models.CharField(max_length=255)


class Meta:
    db_name = 'hsn_db'
