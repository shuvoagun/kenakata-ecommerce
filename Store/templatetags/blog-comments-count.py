from django import template
from Store.models import blog, BlogComment

register = template.Library()

@register.filter
def blog_comments_count(blog_id):
    blogs = blog.objects.get(id=blog_id)
    comments = BlogComment.objects.filter(blog=blogs).count()
    if comments in [1, 2, 4, 5, 6, 7, 8, 9]:
        count = f'0{comments}'
        return count
    else:
        return comments