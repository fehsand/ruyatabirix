from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['ruyatabirleri:anasayfa',
                'ruyatabirleri:dua',
                'ruyatabirleri:dua_nedir',
                'ruyatabirleri:yasin',
                'ruyatabirleri:mubin',
                'ruyatabirleri:yasin_arapca',
                'ruyatabirleri:ayetelkursi',
                'ruyatabirleri:ayetelkursi_arapca',
                'ruyatabirleri:dua_ayet',
                'ruyatabirleri:esmaul_husna',
                'ruyatabirleri:tefriciye',
                'ruyatabirleri:tefriciye_arapca',
                'ruyatabirleri:tefeul',
                'ruyatabirleri:tefeul_nedir',
                'ruyatabirleri:iletisim',
                'ruyatabirleri:gizlilik',
                'ruyatabirleri:yildizname',
                'ruyatabirleri:yildizname_nedir',
                'ruyatabirleri:ruyatabirleri',
                'ruyatabirleri:ruyatabirleri_nedir',
                ]
    def location(self, item):
        return reverse(item)