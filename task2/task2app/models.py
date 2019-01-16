from django.db import models

# Create your models here.
class Salary(models.Model):
    workedyears = models.FloatField(db_column='workedYears', blank=True, primary_key=True)  # Field name made lowercase.
    salarybrutto = models.FloatField(db_column='salaryBrutto', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.workedyears}, {self.salarybrutto}'

    class Meta:
        db_table = 'Salary'