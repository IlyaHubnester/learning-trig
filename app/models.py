from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=500)
    difficulty = models.IntegerField()

    def get_answers(self):
        return Answer.objects.filter(question=self)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text



