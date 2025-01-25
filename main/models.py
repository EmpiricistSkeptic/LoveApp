from django.db import models
from django.contrib.auth.models import User
import uuid

class RelationshipDate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()  

    def __str__(self):
        return f"Start date of relationship for {self.user.username}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    mood = models.CharField(max_length=100, blank=True, null=True)
    unique_code = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
    partner = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    
    def __str__(self):
        return self.name

class Question(models.Model):
    QUESTION_TYPES = (
        ('text', 'Текстовый ответ'),
        ('single', 'Один вариант'),
        ('multiple', 'Несколько вариантов'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name="Текст вопроса")
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default='text')
    
    def __str__(self):
        return f"{self.text[:50]}..."
    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    text_answer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text[:30]}"



