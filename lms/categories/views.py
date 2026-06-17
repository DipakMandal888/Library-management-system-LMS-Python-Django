from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm
from .models import Category


def categories_list(request):
    categories = Category.objects.all()
    return render(
        request,
        'categories/list.html',
        {'categories': categories} # context
    )


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(
        request,
        'categories/detail.html',
        {'category': category}
    )


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Category created successfully.')
            return redirect('categories:detail', pk=category.pk)
    else:
        form = CategoryForm()

    return render(
        request,
        'categories/form.html',
        {
            'form': form,
            'form_title': 'Add Category',
            'submit_label': 'Create Category',
        }
    )


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Category updated successfully.')
            return redirect('categories:detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)

    return render(
        request,
        'categories/form.html',
        {
            'form': form,
            'category': category,
            'form_title': 'Edit Category',
            'submit_label': 'Save Changes',
        }
    )


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully.')
        return redirect('categories:list')

    return render(
        request,
        'categories/confirm_delete.html',
        {'category': category}
    )
