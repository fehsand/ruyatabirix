from django.contrib import admin
from .models import (
    Ruyatabirleri, ArananKelimeler, yildizname, KuranBilgi, KuranKelime,
    Ruyatabirlerix_sbt, RTXyorum, Rtx_iletisim, Ruyatabirlerix5)


admin.site.register(Ruyatabirleri)
admin.site.register(ArananKelimeler)
admin.site.register(yildizname)

admin.site.register(KuranBilgi)
admin.site.register(KuranKelime)
admin.site.register(Ruyatabirlerix_sbt)
admin.site.register(RTXyorum)
admin.site.register(Rtx_iletisim)
admin.site.register(Ruyatabirlerix5)