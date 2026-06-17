from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AuthorForm
from .models import Author


def authors_list(request):
    authors = Author.objects.all()
    return render(
        request,
        'authors/list.html',
        {'authors': authors}
    )


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(
        request,
        'authors/detail.html',
        {'author': author}
    )


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            messages.success(request, 'Author created successfully.')
            return redirect('authors:detail', pk=author.pk)
    else:
        form = AuthorForm()

    return render(
        request,
        'authors/form.html',
        {
            'form': form,
            'form_title': 'Add Author',
            'submit_label': 'Create Author',
        }
    )


def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            messages.success(request, 'Author updated successfully.')
            return redirect('authors:detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)

    return render(
        request,
        'authors/form.html',
        {
            'form': form,
            'author': author,
            'form_title': 'Edit Author',
            'submit_label': 'Save Changes',
        }
    )


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        author.delete()
        messages.success(request, 'Author deleted successfully.')
        return redirect('authors:list')

    return render(
        request,
        'authors/confirm_delete.html',
        {'author': author}
    )
