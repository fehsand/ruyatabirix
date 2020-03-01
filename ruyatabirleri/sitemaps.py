from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['ruyatabirleri:anasayfa',
                'ruyatabirleri:iletisim',
                'ruyatabirleri:gizlilik',
                'ruyatabirleri:yildizname',
                'ruyatabirleri:yildizname_nedir',
                'ruyatabirleri:ruyatabirleri',
                'ruyatabirleri:ruyatabirleri_nedir',
                ]
    def location(self, item):
        return reverse(item)