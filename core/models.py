from django.db import models

class Judge(models.Model):
    identifier = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name

class Participant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Score(models.Model):
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.judge} → {self.participant}: {self.points} pts'
