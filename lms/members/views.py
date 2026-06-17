from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .forms import MemberForm
from .models import Member


def members_list(request):
    members = Member.objects.select_related('user').all()
    search_query = request.GET.get('search', '')
    
    if search_query:
        members = members.filter(
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query) |
            Q(user__username__icontains=search_query) |
            Q(phone__icontains=search_query)
        )
    
    return render(
        request,
        'members/list.html',
        {
            'members': members,
            'search_query': search_query,
        }
    )


def member_detail(request, pk):
    member = get_object_or_404(
        Member.objects.select_related('user'),
        pk=pk
    )
    borrow_records = member.borrowrecord_set.select_related('book').all()
    return render(
        request,
        'members/detail.html',
        {
            'member': member,
            'borrow_records': borrow_records,
        }
    )


def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            messages.success(request, 'Member created successfully.')
            return redirect('members:detail', pk=member.pk)
    else:
        form = MemberForm()

    return render(
        request,
        'members/form.html',
        {
            'form': form,
            'form_title': 'Add Member',
            'submit_label': 'Create Member',
        }
    )


def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save()
            messages.success(request, 'Member updated successfully.')
            return redirect('members:detail', pk=member.pk)
    else:
        form = MemberForm(instance=member)

    return render(
        request,
        'members/form.html',
        {
            'form': form,
            'member': member,
            'form_title': 'Edit Member',
            'submit_label': 'Save Changes',
        }
    )


def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        member.delete()
        messages.success(request, 'Member deleted successfully.')
        return redirect('members:list')

    return render(
        request,
        'members/confirm_delete.html',
        {'member': member}
    )
