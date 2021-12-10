from django.contrib import admin

from app.models import Question, Answer


class AnswerAdmin(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin, ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
