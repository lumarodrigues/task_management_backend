from mongoengine import Document, StringField, BooleanField, DateTimeField, ListField, ReferenceField
from datetime import datetime


class Tag(Document):
    name = StringField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(Document):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    title = StringField(max_length=100)
    description = StringField()
    priority = StringField(choices=PRIORITY_CHOICES)
    deadline = DateTimeField()
    tags = ListField(ReferenceField(Tag))
    completed = BooleanField(default=False)

    def __str__(self):
        return self.title
