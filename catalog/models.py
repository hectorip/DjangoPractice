from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=500, blank=True, null=True)
    pages = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(
        'Author',
        on_delete=models.PROTECT,
        related_name='books'
    )

    def __str__(self):
        return "Título: %s, p. %s" % (self.title, self.pages)


class Author(models.Model):
    name = models.CharField(max_length=140)
    biography = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
