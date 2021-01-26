from django.db import models

# Create your models here.
class Bookmark(models.Model):
    url = models.TextField()
    tags = models.ManyToManyField("Tag")

    class Meta:
        db_table = 'bookmark'

    def __str__(self):
        return self.url

class Tag(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name
