from django.db import models


class dc_avail(models.Model):
        fullname = models.CharField(max_length=200)
        doctorname = models.CharField(max_length=200)
        timeslot = models.DateTimeField(auto_now_add=True)

