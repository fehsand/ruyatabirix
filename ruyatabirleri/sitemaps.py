from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['ruyatabirleri:ruyatabirleri',
                'ruyatabirleri:ruya_nedir',
                'ruyatabirleri:ruya_ile_amel',
                'ruyatabirleri:ruya_hadis',
                'ruyatabirleri:gizlilik',
                ]
    def location(self, item):
        return reverse(item)