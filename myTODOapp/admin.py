from django.contrib import admin
from .models import Todo      # .models yazma sebebimiz aynı klasör altındaki models dosyasını kullanıyor olmamızdı
# Uygulamamizda olsuturdugumuz modelleri admin panelinde gostermemiz icin yani oradan kontrol etmemiz icin burada bu modelleri register etmemiz gerekli
# Register your models here.

admin.site.register(Todo)