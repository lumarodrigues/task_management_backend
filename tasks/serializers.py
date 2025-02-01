from rest_framework_mongoengine import serializers
from mongoengine import ListField, ReferenceField
from .models import Task, Tag


class TagSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TaskSerializer(serializers.DocumentSerializer):
    tags = ListField(ReferenceField(Tag), required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline', 'completed', 'tags']
