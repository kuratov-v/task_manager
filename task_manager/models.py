from django.db import models

from django.contrib.auth import get_user_model


class Task(models.Model):
    STATUS = (
        ("new", "Новая"),
        ("planned", "Запланированная"),
        ("in_work", "в Работе"),
        ("done", "Завершённая"),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk} | {self.title}"
