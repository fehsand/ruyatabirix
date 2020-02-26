from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['ruyatabirleri:anasayfa',
                'ruyatabirleri:ruyatabirleri',
                'ruyatabirleri:yildizname',
                'ruyatabirleri:yildizname_nedir',
                'ruyatabirleri:ruyatabirleri_nedir',
                'ruyatabirleri:ruya_nedir',
                'ruyatabirleri:ruya_ile_amel',
                'ruyatabirleri:ruya_hadis',
                'ruyatabirleri:gizlilik',
                ]
    def location(self, item):
        return reverse(item)