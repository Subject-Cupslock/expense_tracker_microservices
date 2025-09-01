from django.db import models

# Create your models here.
class Report(models.Model):
    user_id = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=20, default='monthly')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'reports'