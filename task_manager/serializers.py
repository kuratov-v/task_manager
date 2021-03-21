from rest_framework import serializers

from .models import Task, TaskChangeHistory


class TaskChangeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskChangeHistory
        fields = ["datetime", "changed_to"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "date_created",
            "date_end",
        ]


class TaskReadSerializer(serializers.ModelSerializer):
    change_history = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "date_created",
            "date_end",
            "change_history",
        ]

    def get_change_history(self, obj):
        return TaskChangeHistorySerializer(obj.change_history, many=True).data
