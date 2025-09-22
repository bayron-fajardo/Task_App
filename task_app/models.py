from django.db import models

class TaskData(models.Model):
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.data} - {self.created_at.strftime('%d-%m-%Y %H:%M')}"
