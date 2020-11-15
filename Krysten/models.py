from django.db import models
from django.core.exceptions import ValidationError
class Person(models.Model):
    description = models.TextField()
    image_url = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.pk and Person.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Person instance')
        return super(Person, self).save(*args, **kwargs)


class Texts(models.Model):
    title = models.TextField()
    description = models.TextField()
    poem_pdf = models.FileField(upload_to="poems/")

class Music(models.Model):
    title = models.TextField()
    description = models.TextField()
    content_url = models.TextField()

# Create your models here.
