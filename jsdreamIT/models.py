from django.core.checks import messages
from django.urls import reverse
from django.db import models

# Create your models here.

class Testimonial(models.Model):
    title = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='testimonial')

    def __str__(self):
        return self.title


        
class Proud(models.Model):
    title = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Proud')

    def __str__(self):
        return self.title  


class Experience(models.Model):
    title = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='experience')
    social_facebook = models.URLField()
    social_github = models.URLField()

    def __str__(self):
        return self.title 

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service')

    def __str__(self):
        return self.title

class Technology(models.Model):
    image = models.ImageField(upload_to='technology')
    hover_image = models.ImageField(upload_to='technology')


                 
class Awards(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service')

    def __str__(self):
        return self.title

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Banner(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title 

class Design(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='design')

    def __str__(self):
        return self.title                                                    


class Contactus(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name        

class Post(models.Model):
    title=models.CharField(max_length=100)
    slug = models.SlugField()
    description=models.TextField()
    image=models.ImageField(upload_to='blog')
    creation=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jsdreamIT:details", kwargs={
            "slug": self.slug
            })
    
    
    
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()
        
class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    body = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    