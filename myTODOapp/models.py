from django.db import models
# Kullanacagimiz tablo yapilarini modelleri class'lar halinde burada olusturuyoruz
# Create your models here.


class Todo(models.Model): #models icindeki Model'den inherit etmesi gerekiyor model olmasi icin


    title = models.CharField(max_length=50, verbose_name= "Başlık") #veri tabanındaki varcharlara denk gelen bir char
    # field oluşturduk admin banelinde güzel bir şekilde göstermek için buraya Başlık yazdık
    completed = models.BooleanField(verbose_name= "Durum") #yani oluşturacağımız todo_element complete edilmişmi edilmemişmi
    #Şimdi burada bir Id ataması yapmadık zaten Django bir Id ataması yapılmadığı durumda yani primary_key verilmediğinde otomatik olarak
    #bir Id oluşturuyor ve ona primary key özelliği veriyor o yüzden eklemeye gerek duymadım

    def __str__(self):
        return self.title   #bu fonksiyonu yazma sebebimiz todo_
                         #listesinde todo_object şeklinde değil de yazılan başlığın görünmesini istiyor
                         #olmamız, yine aynı şekilde completed döndürseydik false veya true şeklinde dönecekti isimler

    objects = models.Manager()  #pycharm'da class.objects.all() komutunu çalıştırabilmek için bu satırı yazmamız gerekiyor