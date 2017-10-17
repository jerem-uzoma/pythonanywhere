from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'part'),
        ('p', 'published'),
    ) 

    title = models.CharField('Title', max_length=100)
    body = models.TextField('Text')

    created_time = models.DateTimeField('created time', auto_now_add=True)
    # auto_now_add : Create timestamps that will not be overwritten

    last_modified_time = models.DateTimeField('change time', auto_now=True)
    # auto_now: Automatically overwrite the time with the current one
	
    objects = EntryQuerySet.as_manager()

    status = models.CharField('Article status', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('Summary', max_length=54, blank=True, null=True,
                                  help_text="Type summary here, not more than 54 characters")
    
    views = models.PositiveIntegerField('Views', default=0)
    
    likes = models.PositiveIntegerField('Likes', default=0)
    # If article should be at the top
    topped = models.BooleanField('Stick top', default=False)
 
    category = models.ForeignKey('Category', verbose_name='classification',
                                 null=True,
                                 on_delete=models.SET_NULL)
   
    tags = models.ManyToManyField('Tag', verbose_name='Label collection', blank=True)


    def __str__(self):
        return self.title

    class Meta:
        # Meta contains a series of options, where ordering represents the sort, - indicates the reverse order
        # that is, when the article from the database, the article to the final revision time in reverse order
        ordering = ['-last_modified_time']

    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'article_id': self.pk})

class Category(models.Model):
    """
    this stores the classification of the article information
    """
    name = models.CharField('Classification name', max_length=20)
    created_time = models.DateTimeField('Time of creation', auto_now_add=True)
    last_modified_time = models.DateTimeField('Last Modified', auto_now=True)

    def __str__(self):
        return self.name

class BlogComment(models.Model):
    user_name = models.CharField('Name', max_length=100)
    body = models.TextField('Comment')
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='Comment on the article', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]

class Tag(models.Model):
    """
    tag(Tag cloud)corresponding to the database
    """
    name = models.CharField('Name', max_length=20)
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    last_modified_time = models.DateTimeField('Modified', auto_now=True)

    def __str__(self):
        return self.name


class Suggest(models.Model):
 
    suggest = models.TextField('suggestion', max_length=200)
    suggest_time = models.DateTimeField('Suggested', auto_now_add=True)

    def __str__(self):
        return self.suggest

class EntryQuerySet(models.QuerySet):
    def published_aritcles(self):
	    return filter(self.published = True)