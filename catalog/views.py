from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    
    return render(request, template_name='home.html')

def contacts(request):
    if request.method == 'POST':
        # Обработка формы
        name = request.POST.get('name', '')      # Получаем поле name
        phone = request.POST.get('phone', '')    # Получаем поле phone
        message_text = request.POST.get('message', '') # Получаем поле message
        
        print(f"Django получил: Имя={name}, Телефон={phone}, Текст={message_text}")

        messages.success(request, f"Спасибо, {name}! Ваше сообщение отправлено.")
        return redirect('catalog:contacts') # Возвращаемся на ту же страницу, но через GET

     
    # Для GET возвращаем страницу контактов
    return render(request, 'contacts.html')

