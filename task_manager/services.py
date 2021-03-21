from .models import TaskChangeHistory, Task
from .serializers import TaskSerializer


def task_change_history(new_task: Task, old_task: Task = None) -> None:
    changed_data = {}
    if not old_task:
        changed_data.update(TaskSerializer(new_task).data)
    else:
        for field in old_task._meta._get_fields():
            field_name = field.name
            if getattr(old_task, field_name) != getattr(new_task, field_name):
                changed = {field_name: TaskSerializer(new_task).data.get(field_name)}
                changed_data.update(changed)
    TaskChangeHistory.objects.create(task=new_task, changed_to=changed_data)
