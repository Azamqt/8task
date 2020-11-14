from django.shortcuts import render
from .models import Book, Author, BookInstance
from django.contrib.auth.decorators import login_required
# from django.views import generic
# from django.conf.urls import url

@login_required
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.
    

# class BookListView(generic.ListView):
#     model = Book

# class BookListView(generic.ListView):
#     model = Book
#     paginate_by = 2
#     context_object_name = 'my_book_list'   # ваше собственное имя переменной контекста в шаблоне
#     queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
#     template_name = 'books/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположения

# Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    print('num_visits')
    
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'catalog/index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
            'num_visits':num_visits,} # num_visits appended

    )
