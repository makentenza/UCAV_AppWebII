from django.db import models
from django.core.urlresolvers import reverse


class Task(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks:task_edit', kwargs={'pk': self.pk})