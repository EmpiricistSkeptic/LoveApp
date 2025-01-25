from django.contrib import admin
from .models import Profile, RelationshipDate, Question, Answer, Category

admin.site.register(Profile)
admin.site.register(RelationshipDate)
admin.site.register(Answer)

class AnswerInline(admin.TabularInline):  # Или StackedInline для вертикального отображения
    model = Answer
    extra = 4

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('text', 'category')
    list_filter = ('category',)