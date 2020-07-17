from django.contrib import admin
from .models import (
    Ruyatabirleri, ArananKelimeler, yildizname, KuranBilgi, KuranKelime,
    Ruyatabirlerix_sbt, Ruyatabirlerix3, RTXyorum)


admin.site.register(Ruyatabirleri)
admin.site.register(ArananKelimeler)
admin.site.register(yildizname)

admin.site.register(KuranBilgi)
admin.site.register(KuranKelime)
admin.site.register(Ruyatabirlerix_sbt)
admin.site.register(Ruyatabirlerix3)
admin.site.register(RTXyorum)
