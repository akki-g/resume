from django.contrib import admin

from . models import (
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Lifting,
    Portfolio,
    Certificate,
    Skill,
    Education,
    LiftingGallery
)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'timestamp', 'name')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Lifting)
class LifitngAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields=('slug',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificatonAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=('id','name','score')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'is_active')
    readonly_fields= ('slug',)

@admin.register(LiftingGallery)
class LiftingGalleryAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'is_active')