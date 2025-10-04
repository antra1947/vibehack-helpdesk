from django.db import models
from django.utils import timezone
from datetime import timedelta

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    due_by = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # set due_by automatically based on priority if not set
        if not self.due_by:
            now = timezone.now()
            if self.priority == 'high':
                delta = timedelta(hours=4)
            elif self.priority == 'medium':
                delta = timedelta(hours=24)
            else:
                delta = timedelta(hours=72)
            self.due_by = now + delta
        super().save(*args, **kwargs)

    @property
    def is_overdue(self):
        return self.status != 'resolved' and self.due_by and timezone.now() > self.due_by

    def __str__(self):
        return f"{self.title} ({self.get_priority_display()})"

class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.ticket}"
