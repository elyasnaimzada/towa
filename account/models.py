from django.db import models


# Create your models here.


class Jobs(models.Model):
    invoiceno = models.IntegerField()
    transtype = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    ticket = models.IntegerField(blank=True)
    externalno = models.CharField(max_length=200, blank=True)
    cctname = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    sordescription = models.TextField(max_length=None,blank=True )
    qty = models.IntegerField(blank=True)
    rate = models.FloatField(blank=True)
    gst = models.FloatField(blank=True)
    total = models.FloatField(blank=True)

    def __str__(self):
        return self.location
