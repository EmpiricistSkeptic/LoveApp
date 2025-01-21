from django.contrib import admin
from .models import Profile, RelationshipDate, Question, Answer, Category

admin.site.register(Profile)
admin.site.register(RelationshipDate)
admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Question)

