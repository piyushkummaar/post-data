from django.db.models.signals import (
                                        pre_save,
                                        post_save,
                                        post_delete,
                                        pre_delete)
from django.db import models
import uuid
from django.dispatch import receiver
from allaboutmodels.vaildators import email_vaildator, domain_vaildator
from django.utils.encoding import smart_text
from django.utils.text import slugify
from django.utils.timesince import timesince
# from django.db.models import Model

''' 
python manage.py makemigrations
    everytime change in models.py 

python manage.py migrate

'''
# class Post(Model):
    # pass

GENDER_CHOICS = (
    ('none','None'),
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
    )

class PersonModelQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class PersonModelManager(models.Manager):
    def get_queryset(self):
        return PersonModelQuerySet(self.model,using=self._db)

    def all(self, *args, **kwargs):
        # qs = super(PersonModelManager, self).all(*args,**kwargs).active() #.filter(active=True)
        qs = self.get_queryset.active()
        return qs

class Person(models.Model):
    id        = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    active    = models.BooleanField(default=True)
    name      = models.CharField(
                                max_length=30,
                                unique=True, 
                                verbose_name='Person Name',
                                help_text='Must be a unique Name.'
                                )
    email = models.CharField(max_length=240, validators=[email_vaildator, domain_vaildator], null=True, blank=True,verbose_name='Person Email',help_text='Must be a unique email.')
    bio = models.TextField(null=True, blank=True, verbose_name='About Yourself')
    gender    = models.CharField(max_length=120,choices=GENDER_CHOICS,default='none')
    number    = models.IntegerField(default=0,verbose_name='Phone Number')
    slug      = models.SlugField(null=True,blank=True)
    # status    = models.ManyToManyField()
    updated   = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects   = PersonModelManager()
    piyush    = PersonModelManager()
    # its work deu to this above connection to the model Peson.piyush.all() 
    
    
    def save(self,*args,**kwargs):
        # if not self.slug:
        #     self.slug = slugify(self.name) 
        super(Person,self).save(*args,**kwargs,)
        
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
    
    def __str__(self):
        return smart_text(self.name)
    
    def age(self):
        return "{t} ago".format(t=timesince(self.timestamp))
        


@receiver(pre_save, sender=Person)
def person_pre_save_receiver(sender, instance,  *args, **kwargs):
    print('before save')
    if not instance.slug and instance.name:
        instance.slug = slugify(instance.name)



@receiver(post_save, sender=Person)
def person_post_save_receiver(sender, instance,  *args,**kwargs):
    print("aftersave")
    if not instance.slug and instance.name:
        instance.slug = slugify(instance.name)
        instance.save()
        
