from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ships(BaseModel):
    imo = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.imo)

    class Meta:
        db_table = 'ships'


class Positions(BaseModel):
    imo_number = models.ForeignKey(Ships, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()
    latitude = models.DecimalField(max_digits=50, decimal_places=7)
    longitude = models.DecimalField(max_digits=50, decimal_places=7)

    def __str__(self):
        return str(self.imo_number)

    class Meta:
        db_table = 'positions'

