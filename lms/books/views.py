from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book


def books_list(request):
    books = Book.objects.select_related('author', 'category').all()
    return render(
        request,
        'books/list.html',
        {'books': books}
    )


def book_detail(request, pk):
    book = get_object_or_404(
        Book.objects.select_related('author', 'category'),
        pk=pk
    )
    return render(
        request,
        'books/detail.html',
        {'book': book}
    )


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book created successfully.')
            return redirect('books:detail', pk=book.pk)
    else:
        form = BookForm()

    return render(
        request,
        'books/form.html',
        {
            'form': form,
            'form_title': 'Add Book',
            'submit_label': 'Create Book',
        }
    )


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book updated successfully.')
            return redirect('books:detail', pk=book.pk)
    else:
        form = BookForm(instance=book)

    return render(
        request,
        'books/form.html',
        {
            'form': form,
            'book': book,
            'form_title': 'Edit Book',
            'submit_label': 'Save Changes',
        }
    )


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully.')
        return redirect('books:list')

    return render(
        request,
        'books/confirm_delete.html',
        {'book': book}
    )
