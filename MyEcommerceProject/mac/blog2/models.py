from datetime import timedelta, datetime, date

from django.db import models
from django.utils import timezone
from .custom_validators import validate_author_email, validate_school_email
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.timesince import timesince


# Create your models here.
class Post2Model(models.Model):

    PUBLISH_CHOICES = [
        ('draft', 'Draft'),
        ('publish', 'Publish'),
        ('private', 'Private'),
    ]

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(
        max_length=240,
        error_messages = {
            "blank": "This field is not full pelase. give some title.",
            "unique": "This title is not unique, please try again.",
            "null": "This field is not full pelase. give some title."
        },
        unique= True,
        help_text = "Must be a unique Title.",
        verbose_name="Post Title"
                            )
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default="publish")
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.CharField(null=True, blank=True, max_length=240, validators=[validate_school_email, validate_author_email])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print("Calling save Method")
        # if not self.slug and self.title and self.title is not None:
        #     self.slug = slugify(self.title)
        super(Post2Model, self).save(*args, **kwargs)

    @property
    def age(self):
        if self.publish == 'publish':
            now = datetime.now()
            publish_time = datetime.combine(
                self.publish_date,
                datetime.now().min.time()
            )
            try:
                difference = now - publish_time
            except:
                return "Unknown"
            if difference <= timedelta(minutes=1):
                return 'just now'
            return '{time} ago'.format(time=timesince(publish_time).split(', ')[0])
        return "Not published"

    def age2(self):
        if self.publish:
            now = datetime.now()
            publish_time = datetime.combine(
                self.publish_date,
                datetime.now().min.time()
            )
            return "publish time"+publish_time
        return "Not published"

    class Meta:
        verbose_name = "post2"
        verbose_name_plural = "posts2"

    def __str__(self):
        return self.title


def blog_post_pre_save(sender, instance, **kwargs):
    print("pre save process")
    # if not instance.slug and instance.title:
    #     instance.slug = slugify(instance.title)

pre_save.connect(blog_post_pre_save, sender=Post2Model)

def blog_post_post_save(sender, instance, **kwargs):
    print("post save process")
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)
        instance.save()
post_save.connect(blog_post_post_save, sender=Post2Model)