from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
#views bizim buraya bir url adresi geldiginde bir fonksiyon calistirmamizi sagliyor bunlar views fonksiyonlari oluyor buradaki
# Create your views here.


def index(request):  #index dısında baska bır ısımde verebılırız yaygın kullanım bu ancak içerisine mutlaka
                    #request değişkenini göndermemiz gerekiyor yani bu değişken gelen requestleri almamızı sağlıyor
                    #bu değişken üzerinden örneğin bu requesti hangi user yaptı veya post/get üzerinden gelen verilerimizi alabiliyoruz
                    #kısacası bir request geliyor biz bu requeste göre bir fonksiyon çalıştırıyoruz o fonksiyon da bir response dönüyor
                    # urls python dosyası içerisinden bu indexi çağıracağız
    context={
        "Hosgeldiniz": "Hoşgeldiniz",
        "Mesaj": "Bu site yapmak istediklerinizi düzenlemenize yardımcı olur"
    }
                    #Aynı zamanda bu template içerisine verilerimizi de gönderebiliiriz bunu da sözlük olarak yapmamız gerekiyor
                    #bunun için context adında bir sözlük ismi verdim hoşgeldiniz ve mesaj anahtarlarımı ve karşılık gelen değerlerini oluşturdum
                    #index html içerisinde bu anahtar isimlerini çağırdım çift süslü parantez kullanarak
    todos = Todo.objects.all() #veritabanındaki tüm görevler liste içerisinde sözlük yapısı şeklinde bu todos içerisine geliyor
    return render(request, "index.html",{"todos":todos})  #bu todos içerisinde bir for döngüsü yardımıyla gezinicez index html 39. satır

def gorevler(request):
    if request.method=="GET":   #burada get veya post request olup olmadığını kontrol etmemiz gerekiyor ikisinde farklı işlemler yapmak için
        return redirect("/")    #ana sayfamıza yönlendirmek için redirect fonksiyonunu kullandık
    else:
        title= request.POST.get("title") #Post'tan gelen bilgileri aldık title adına göre bu title bilgisini aldık
        yeniGorev= Todo(title = title, completed = False) #burada yenigörev adında yeni bir obje oluşturduk Todo classı içerisinde
                                                        #title olarak girilen title ile aynı yaptık, ve default olarak görevi tamamlanmadı şeklinde belirttik
                                                        #burada completed true veya false olarak dönüyor bu html içerisinde if else kullanarak değiştirildi
        yeniGorev.save() # save ile database'e yeni objemizi kaydettik, burada Django içerisindeki ORM yapısını kullandık genel olarak
        return redirect("/") #anasayfaya tekrar yönlendirdik

def update(request,id): #görev id'sini almak için ikinci argüman olarak id verdik django bu id'leri otomatik gönderiyor

    yapilacak=get_object_or_404(Todo,id=id) #id'ye göre filtreleme yapıyoruz eğer bu id varsa obje gelecek yoksa 404 verecek

    yapilacak.completed= not yapilacak.completed #burada görevin yapılıp yapılmadığını tam tersine çeviriyoruz güncellemek için

    yapilacak.save()
    return redirect("/") #anasayfaya tekrar yönlendirdik

def delete(request,id):

    yapilacak=get_object_or_404(Todo,id=id) #yine obje id'sine göre filtreleme yaparak objemizi alıyoruz

    yapilacak.delete() #objemizi yani görevi veritabanından siliyoruz
    return redirect("/")