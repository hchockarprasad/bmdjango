from django.db import models


# Configuration
class CoreConf(models.Model):

    particulars = models.CharField(max_length=100)

    flag_1 = models.BooleanField()

    class Meta:
        db_table = 'tbl_core_conf'

    def __unicode__(self):
        return str(self.particulars)

    def __str__(self):
        return str(self.particulars)
