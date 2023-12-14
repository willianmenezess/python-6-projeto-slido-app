from django.db import models


class Visitor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    question = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.question}"
