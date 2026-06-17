from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    MEMBERSHIP_CHOICES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('public',  'Public'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    membership_type = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_CHOICES,
        default='student'
    )
    phone            = models.CharField(max_length=15, blank=True)
    address          = models.TextField(blank=True)
    membership_date  = models.DateField(auto_now_add=True)
    is_active        = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.membership_type})"

    def active_borrows(self):
        return self.borrowrecord_set.filter(return_date__isnull=True).count()

    def get_unique_id(self):
        """Generate unique 4-digit ID with capital letter suffix (e.g., 0001A)"""
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digit_part = str(self.id).zfill(4)
        letter_index = (self.id - 1) % 26
        letter_part = letters[letter_index]
        return f"{digit_part}{letter_part}"

    class Meta:
        ordering = ['user__last_name']
