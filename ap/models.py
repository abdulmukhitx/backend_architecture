from django.db import models

# Create your models here.
class Jobs(models.Model) :
    title= models.CharField(max_length=255, db_index=True)
    company= models.CharField(max_length=255, db_index=True)
    salary=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ["title"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["company"]),
        ]
        
    def __str__(self):
        return f"{self.title} at {self.company}"
        

