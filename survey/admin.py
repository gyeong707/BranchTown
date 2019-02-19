from django.contrib import admin
from .models import Survey, Field, MultipleChoice, TextAnswer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['type', 'question']


@admin.register(MultipleChoice)
class MultipleChoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(TextAnswer)
class TextAnswerAdmin(admin.ModelAdmin):
    pass
