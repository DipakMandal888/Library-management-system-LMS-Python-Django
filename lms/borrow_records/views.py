from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .forms import BorrowRecordForm
from .models import BorrowRecord


def borrow_records_list(request):
    borrow_records = BorrowRecord.objects.select_related(
        'member__user',
        'book',
        'book__author',
    ).all()
    search_query = request.GET.get('search', '')
    
    if search_query:
        borrow_records = borrow_records.filter(
            Q(member__user__first_name__icontains=search_query) |
            Q(member__user__last_name__icontains=search_query) |
            Q(member__user__username__icontains=search_query) |
            Q(book__title__icontains=search_query)
        )
    
    return render(
        request,
        'borrow_records/list.html',
        {
            'borrow_records': borrow_records,
            'search_query': search_query,
        }
    )


def borrow_record_detail(request, pk):
    borrow_record = get_object_or_404(
        BorrowRecord.objects.select_related(
            'member__user',
            'book',
            'book__author',
        ),
        pk=pk
    )
    return render(
        request,
        'borrow_records/detail.html',
        {'borrow_record': borrow_record}
    )


def borrow_record_create(request):
    if request.method == 'POST':
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            borrow_record = form.save()
            messages.success(request, 'Borrow record created successfully.')
            return redirect('borrow_records:detail', pk=borrow_record.pk)
    else:
        form = BorrowRecordForm()

    return render(
        request,
        'borrow_records/form.html',
        {
            'form': form,
            'form_title': 'Add Borrow Record',
            'submit_label': 'Create Borrow Record',
        }
    )


def borrow_record_update(request, pk):
    borrow_record = get_object_or_404(BorrowRecord, pk=pk)

    if request.method == 'POST':
        form = BorrowRecordForm(request.POST, instance=borrow_record)
        if form.is_valid():
            borrow_record = form.save()
            messages.success(request, 'Borrow record updated successfully.')
            return redirect('borrow_records:detail', pk=borrow_record.pk)
    else:
        form = BorrowRecordForm(instance=borrow_record)

    return render(
        request,
        'borrow_records/form.html',
        {
            'form': form,
            'borrow_record': borrow_record,
            'form_title': 'Edit Borrow Record',
            'submit_label': 'Save Changes',
        }
    )


def borrow_record_delete(request, pk):
    borrow_record = get_object_or_404(BorrowRecord, pk=pk)

    if request.method == 'POST':
        borrow_record.delete()
        messages.success(request, 'Borrow record deleted successfully.')
        return redirect('borrow_records:list')

    return render(
        request,
        'borrow_records/confirm_delete.html',
        {'borrow_record': borrow_record}
    )
