from django.contrib.sitemaps import Sitemap
from Quizlet.models import Quiz


class QuizSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Quiz.objects.all()
