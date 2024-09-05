from django.contrib import admin
from.models import Category, Post, Comment, Reyting, Banner, Contact

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'author', 'created_at', 'updated_at', 'description',  ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [ 'content',  'like' ]

@admin.register(Reyting)
class ReytingAdmin(admin.ModelAdmin):
    list_display = [ 'rating' ]

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [ 'image', 'url' ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [ 'telegtam_url', 'instagram_url', 'facebook_url', 'twitter_url' ]
