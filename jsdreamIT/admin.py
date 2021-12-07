from django.contrib import admin
from.models  import  Testimonial,Proud,Experience,Service,Technology,Awards,Appointment,Contact,Banner,Design,Contactus,Post,Comment


@admin.register(Testimonial)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','designation','image'
    ]


@admin.register(Proud)
class ProudModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','designation','image'
    ]



@admin.register(Experience)
class ExperienceModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','designation','image','social_facebook'
    ]



@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image'
    ] 


@admin.register(Technology)
class TechnologyModelAdmin(admin.ModelAdmin):
    list_display=[
        'image'
    ]    

@admin.register(Awards)
class AwardsModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image'
    ] 

@admin.register(Appointment)
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display=[
        'name','email'
    ] 

    
@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=[
        'name','email'
    ] 


@admin.register(Banner)
class BannerdModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image',
    ] 

@admin.register(Design)
class DesignModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image',
    ]       


@admin.register(Contactus)
class ContactusModelAdmin(admin.ModelAdmin):
    list_display=[
        'name','email',
    ]

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image','description',
    ]
    

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'body','email'
    ]
    