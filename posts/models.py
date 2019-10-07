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
    topic = models.ForeignKey(
        'Topic',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'id':self.pk})

    @property
    def get_markdown(self):
        return mark_safe(markdown(self.content))

class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    @property
    def get_posts(self):
        return Post.objects.filter(topic=self)

    def get_absolute_url(self):
        return reverse('posts:topic', kwargs={'id': self.pk})
