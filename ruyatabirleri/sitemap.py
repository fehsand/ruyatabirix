from django.contrib.sitemaps import Sitemap
from qartez.sitemaps import StaticSitemap, RelAlternateHreflangSitemap
from ruyatabirleri.models import Ruyatabirlerix5, Ruyatabirlerix_sbt

# ---------------------- Static sitemap part ---------------------------
# Sitemap for service pages like welcome and feedback.
foo_static_sitemap = StaticSitemap(priority=0.7, changefreq='monthly')
foo_static_sitemap.add_named_pattern('ruyatabirleri:anasayfa')

# ---------------------- Static PAge Normal sitemap part ---------------------------
# Static PAge_Normal Foo items sitemap.
class FooItemAlternateHreflangSitemap2(RelAlternateHreflangSitemap):
    changefreq = "monthly"
    priority = 0.7

    def alternate_hreflangs(self, item):
        return [('en', item.altr_en_url),
                ('ar', item.altr_ar_url),
                ('es', item.altr_es_url),
                ('ru', item.altr_ru_url),
                ('zh-hans', item.altr_ch_url),
                ]

    def items(self):
        return Ruyatabirlerix_sbt._default_manager.exclude(altr_en_url=None).exclude(altr_ar_url =None).exclude(altr_es_url =None).exclude(altr_ru_url =None).exclude(altr_ch_url =None).order_by('id')

# ---------------------- Alternate hreflang sitemap part ---------------
# Alternate hreflang sitemap.
class FooItemAlternateHreflangSitemap(RelAlternateHreflangSitemap):
    changefreq = "weekly"
    priority = 1.0
    #protocol = 'https'
    def alternate_hreflangs(self, item):
        return [('en', item.altr_en_url),
                ('es', item.altr_es_url),
                ('ru', item.altr_ru_url),
                ('ar', item.altr_ar_url),
                ('zh-hans', item.altr_ch_url),
                ]

    def items(self):
        return Ruyatabirlerix5._default_manager.exclude(altr_en_url=None).exclude(altr_es_url =None).exclude(altr_ru_url =None).exclude(altr_ar_url =None).exclude(altr_ch_url =None).order_by('id')
