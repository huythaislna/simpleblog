from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from markdown_deux import markdown

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE,
    )
    timestamp = models.DateField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'id':self.pk})

    @property
    def get_markdown(self):
        return mark_safe(markdown(self.content))