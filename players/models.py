from django.db import models


# Create your models here.
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    setNo = models.PositiveIntegerField(null=False, blank=False)
    name = models.CharField(blank=False, null=False, max_length=200)
    img = models.ImageField(null=False, blank=False)
    country = models.CharField(blank=False, null=False, max_length=200)
    prev_team = models.CharField(blank=False, null=False, max_length=4)
    basePrice = models.PositiveIntegerField(null=False, blank=False)
    age = models.PositiveSmallIntegerField(null=False, blank=False)
    numMatches = models.PositiveIntegerField(null=True, blank=False)
    numRuns = models.PositiveIntegerField(null=True, blank=True)
    battingAvg = models.FloatField(null=True, blank=True)
    strikeRate = models.FloatField(null=True, blank=True)
    numWickets = models.PositiveIntegerField(null=True, blank=True)
    bowlingAvg = models.FloatField(null=True, blank=True)
    bowlingEconomy = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
