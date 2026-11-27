from django.shortcuts import render


def home(request):
    
    return render(request, template_name='home.html')

def contacts(request):
    if request.method == 'POST':
        # Обработка формы (см. пункт 3 ниже)
        pass 
    
    # Для GET возвращаем страницу контактов
    return render(request, 'contacts.html')

