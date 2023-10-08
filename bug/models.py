from django.db import models

class Bug(models.Model):
    # A textual description of the bug
    description = models.TextField()

    # Choices for bug types
    BUG_TYPES = [
        ('error', 'Error'),
        ('new_feature', 'New Feature'),
        ('enhancement','Enhancement')
    ]
    bug_type = models.CharField(max_length=20, choices=BUG_TYPES)

    # The date when the bug is being registered (automatically set to the current date and time)
    report_date = models.DateTimeField(auto_now_add=True)

    # Choices for bug status
    STATUS_CHOICES = [
        ('unconfirmed', 'Unconfirmed'),   
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'), 
        ('done', 'Done'),
        ('reopened', 'Reopened'),               
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.description
