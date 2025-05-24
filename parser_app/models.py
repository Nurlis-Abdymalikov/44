from django.db import models

class Parser_Movie(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
