from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from task_manager.models import Task, TaskChangeHistory
from task_manager.serializers import TaskSerializer

from .services import task_change_history


@receiver(pre_save, sender=Task)
def task_pre_save(sender, instance, **kwargs):
    if instance.pk is not None:
        previous = Task.objects.get(pk=instance.pk)
        task_change_history(new_task=instance, old_task=previous)


@receiver(post_save, sender=Task)
def task_post_save(sender, instance, created, **kwargs):
    if created:
        task_change_history(new_task=instance)
