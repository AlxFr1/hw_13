from django.shortcuts import get_object_or_404, render

from .models import Author, Quote


def home(request):
    return render(request, 'index.html')


def authors(request):
    author_list = Author.objects.all()
    return render(request, 'author_list.html', {'author_list': author_list})


def authors_info(request, pk):
    author_info = get_object_or_404(Author.objects, pk=pk)
    return render(request, 'author_info.html', {'author_info': author_info})


def quote(request):
    quote_list = Quote.objects.all()
    return render(request, 'quote_list.html', {'quote_list': quote_list})
