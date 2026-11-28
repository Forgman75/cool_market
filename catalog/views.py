from django.contrib import messages
from django.shortcuts import redirect, render


def home(request):
    """Обработка запроса GET, возвращающего страницу home.html"""
    return render(request, template_name='home.html')


def contacts(request):
    """Обработка запроса GET для страницы contacts.html и отправка
    формы обратной связи методом POST.
    """
    if request.method == 'POST':
        # Обработка формы
        name = request.POST.get('name', '')  # Получаем поле name
        phone = request.POST.get('phone', '')  # Получаем поле phone
        message_text = request.POST.get('message', '')  # Получаем поле message

        print(
            f"Django получил: Имя={name}",
            f"Телефон={phone}, Текст={message_text}"
        )

        messages.success(
            request,
            f"Спасибо, {name}! Ваше сообщение отправлено."
        )
        return redirect('catalog:contacts')

    # Для GET возвращаем страницу контактов
    return render(request, 'contacts.html')

