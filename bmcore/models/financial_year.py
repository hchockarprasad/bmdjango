from django.db import models


# Financial year
class FinancialYear(models.Model):

    name = models.CharField(max_length=20)

    fn_begin = models.DateField()

    book_begin = models.DateField()

    active = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_financial_year'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
