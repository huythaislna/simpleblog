from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from markdown_deux import markdown
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
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
    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug':self.slug})

    @property
    def get_markdown(self):
        return mark_safe(markdown(self.content))

class Topic(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    @property
    def get_posts(self):
        return Post.objects.filter(topic=self)

    def get_absolute_url(self):
        return reverse('posts:topic', kwargs={'slug': self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-pk")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)