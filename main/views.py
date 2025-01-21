from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import RelationshipDate, Profile, Category, Answer, Question
from django.contrib.auth.models import User
from .forms import LinkProfileForm, AnswerForm


def main_page(request):
    return render(request, 'main.html')

def poems_page(request):
    return render(request, 'poems.html')


def letters_page(request):
    return render(request, 'letters.html')

def map_page(request):
    return render(request, 'map.html')

def questions_page(request):
    return render(request, 'questions.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('main_page')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




@login_required
def link_profile(request):
    if request.method == 'POST':
        form = LinkProfileForm(request.POST)
        if form.is_valid():
            unique_code = form.cleaned_data['unique_code'] 

            try:
                # Пытаемся найти профиль по уникальному коду
                partner_profile = Profile.objects.get(unique_code=unique_code)

                # Проверка, не пытается ли пользователь привязать сам себя
                if partner_profile == request.user.profile:
                    messages.error(request, "You cannot link your profile to yourself.")
                else:
                    # Привязываем партнера к текущему профилю
                    request.user.profile.partner = partner_profile
                    request.user.profile.save()

                    # Отправляем успешное сообщение
                    messages.success(request, "Profiles linked successfully.")
                    return redirect('profile')  # перенаправляем на профиль
            except Profile.DoesNotExist:
                # Если профиль с таким уникальным кодом не найден
                messages.error(request, "No profile found with this code.")
        else:
            messages.error(request, "Please enter a valid unique code.")
    else:
        # Для GET-запроса создаем пустую форму
        form = LinkProfileForm()

    return render(request, 'link_profile.html', {'form': form})
    

@login_required
def profile_view(request):
    # Проверьте, существует ли профиль для текущего пользователя
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if profile.picture:
        picture_url = profile.picture.url  # Путь к изображению
    else:
        picture_url = None  # Если изображения нет

    answers = Answer.objects.filter(user=request.user)
    
    return render(request, 'profile.html', {'profile': profile, 'picture_url': picture_url, 'answers': answers})
    


def category_list(request, category_id):
    categories = Category.objects.all()
    return render(request, 'questions/category_list.html', {'categories': categories})

def question_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    questions = Question.objects.filter(category=category)
    return render(request, 'questions/question_list.html', {'category': category, 'questions': questions})


def answer_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('question_list', category_id=question.category.id)
        else:
            form = AnswerForm()
        return render(request, 'questions/answer_question.html', {'question': question, 'form': form})