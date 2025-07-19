from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField(blank=True)
    experience_years = models.IntegerField(default=0)
    score = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

