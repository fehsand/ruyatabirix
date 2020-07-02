from django.contrib import admin
from .models import (
    Ruyatabirleri, ArananKelimeler, yildizname, iletisim, KuranBilgi, KuranKelime,
    Ruyatabirlerix)


admin.site.register(Ruyatabirleri)
admin.site.register(ArananKelimeler)
admin.site.register(yildizname)
admin.site.register(iletisim)
admin.site.register(KuranBilgi)
admin.site.register(KuranKelime)
admin.site.register(Ruyatabirlerix)
