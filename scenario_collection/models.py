from django.db import models

class ScenarioCollection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cover_Image = models.ImageField(upload_to='covers/')
    total_Scenarios = models.IntegerField(default=5)

    def calculate_total_scenarios(self):
        total = ScenarioCollection.objects.filter(name=self.name).count()
        return total

    def save(self, *args, **kwargs):
        self.total_Scenarios = self.calculate_total_scenarios()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    



