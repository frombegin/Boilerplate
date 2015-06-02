from django.db import models

# Create your models here.
class Item(models.Model):

    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, default="unnamed")
    description = models.TextField()

    def __unicode__(self):
        return u'[Item: %s, %s]' % (self.description, self.name)


class Detail(models.Model):

    num_of_pages = models.IntegerField()
    author = models.CharField(max_length=64, blank=True)

    def __unicode__(self):
        return u'[Detail: %d, %s]' % (self.num_of_pages, self.author)