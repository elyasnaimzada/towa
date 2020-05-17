from django.db import models


# Create your models here.


class Jobs(models.Model):
    invoiceno = models.IntegerField()
    transtype = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    ticket = models.IntegerField()
    externalno = models.CharField(max_length=200)
    cctname = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    sordescription = models.TextField(max_length=None)
    qty = models.IntegerField()
    rate = models.FloatField()
    gst = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return self.location
