from django.db import models
from members.models import Member
from books.models import Book
from django.utils import timezone

# Create your models here.
class BorrowRecord(models.Model):
    member      = models.ForeignKey(Member, on_delete=models.CASCADE)
    book        = models.ForeignKey(Book,   on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date    = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    notes       = models.TextField(blank=True)

    def __str__(self):
        return f"{self.member} borrowed '{self.book.title}'"

    def is_overdue(self):
        """Returns True if not returned AND past due date."""
        if self.return_date:
            return False
        return timezone.now().date() > self.due_date


    def calculate_fine(self):
        """Rs. 5 per overdue day."""
        if self.return_date or not self.is_overdue():
            return 0
        overdue_days = (timezone.now().date() - self.due_date).days
        return overdue_days * 5

    def get_unique_id(self):
        """Generate unique 4-digit ID with capital letter suffix (e.g., 0001A)"""
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digit_part = str(self.id).zfill(4)
        letter_index = (self.id - 1) % 26
        letter_part = letters[letter_index]
        return f"{digit_part}{letter_part}"

    class Meta:
        ordering = ['-borrow_date']