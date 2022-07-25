from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from todos.sitemaps import TodoSitemap
from todos.views import home, todos, todo

sitemaps = {"todos": TodoSitemap,}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todos/<int:todoId>/", todo, name="todo"),
    path("todos/", todos, name="todos"),
    path("", home),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
