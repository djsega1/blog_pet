from django.contrib import admin
from homepage.models import Post
from paginator import CachingPaginator


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    paginator = CachingPaginator
    list_display = ('title', )
    show_full_result_count = False
