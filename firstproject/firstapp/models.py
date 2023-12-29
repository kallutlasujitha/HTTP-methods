from django.db import models

# Create your models here.
# class emp(models.Model):
#     emp_name=models.CharField(max_length=100)
#     emp_phoneno=models.CharField(max_length=70)
#     emp_mailid=models.CharField(max_length=70)
#     emp_add=models.CharField(max_length=80)
#     emp_sal=models.CharField(max_length=70)


class Emp(models.Model):
    Emp_name=models.CharField(max_length=100)
    Emp_email=models.CharField(max_length=70)
    Emp_message=models.CharField(max_length=80)
    Emp_Gender=models.CharField(max_length=70)






