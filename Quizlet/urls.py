from django.urls import path
from django.contrib.sitemaps.views import sitemap
from Quiz.sitemaps import QuizSitemap
from . import views

app_name = 'quizlet'

sitemaps = {
    'posts': QuizSitemap,
}

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detail, name='detail'),
    path('<int:id>', views.post_comment, name='post_comment'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
    
]