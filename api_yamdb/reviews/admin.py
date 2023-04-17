from django.contrib import admin

from reviews.models import Comment, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'title', 'text', 'score',
    )
    search_fields = (
        'author', 'title', 'text', 'pub_date',
    )
    list_filter = ('title', 'pub_date', )
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'review', 'text', 'pub_date',
    )
    search_fields = ('author', 'text', 'pub_date',)
    list_filter = ('review', )
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
