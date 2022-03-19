from django.db import models

# Model used for game related to each game
class Game(models.Model):
    BGGId = models.IntegerField()
    Name = models.CharField(max_length=200)
    AvgRating = models.FloatField()
    Ratings = models.IntegerField()
    ComMinPlaytime = models.IntegerField()
    Thematic = models.BooleanField()
    Strategy = models.BooleanField()
    War = models.BooleanField()
    Family = models.BooleanField()
    CGS = models.BooleanField()
    Abstract = models.BooleanField()
    Party = models.BooleanField()
    Child = models.BooleanField()

    def __str__(self):
        return self.Name


