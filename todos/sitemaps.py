from django.contrib.sitemaps import Sitemap
from .models import Todo


class TodoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Todo.objects.all()

    def lastmod(self, obj):
        return obj.updated
