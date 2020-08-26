from django.db import models
from django.shortcuts import reverse


LABEL_CHOICES = (
    ('P', 'primary'),
    ('SE', 'secondary'),
    ('S', 'success'),
    ('D', 'danger'),
    ('W', 'warning'),
    ('I', 'info'),
    ('L', 'light'),
    ('DA', 'dark'),
)


class Note(models.Model):

    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_finished_url(self):
        return reverse("finish_item", kwargs={
            'id': self.id
        })

    def get_deleted_url(self):
        return reverse("delete_item", kwargs={
            'id': self.id
        })

    def get_recovered_url(self):
        return reverse("recover_item", kwargs={
            'id': self.id
        })
