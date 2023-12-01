from django.db import models

# Create your models here.
class Visual(models.Model):
    prompt = models.CharField(max_length=120, null=False)
    def __str__(self) -> str:
        return self.prompt