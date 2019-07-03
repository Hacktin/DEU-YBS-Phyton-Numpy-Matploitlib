
import numpy as np 

#tek boyutlu dizi olusturmak icin array fonksiyonu içinde tek bir liste oluşturuyoruz
firstarray=np.array([1,2,3,4])

size_firstarray=np.ndim(firstarray)
#dizimiz kaç boyutlu olduğunu döndürmek için ndim fonksiyonunu kullanıyoruz

print("Array:  "+str(firstarray)+"\nSize of Array:  "+str(size_firstarray))


secondarray=np.array(([1,2,3,4],[5,6,7,8]))
#İki  boyutlu bir dizi oluşturmak için birden fazla listeyi bir tuple içine ya da
#JavaScript bilen arkadaşlarımız varsa onların tabirleri ile bir object türünde bir veri tipi içine
#içine yerleştireceğimiz listeleri koyuyoruz

size_secondarray=np.ndim(secondarray)

print("Array:   "+str(secondarray)+"\nSize of Array:   "+str(size_secondarray))


#****************************************************************************#



secondArrayShaping=np.reshape(secondarray,[8,1])
#İkinci dizimiz ya da matrisimizde 2,4 e bir yapı vardı biz şimdi bu satır ve sutünlarını
#yeniden düzenlemek istediğimizde reshape komutunu kullanabiliriz ve parametreler olarak
#ikinci dizimiz ve satır ve sutün şeklini belirtiyoruz.Dikkat edin satır ve sutün belirlerken
#dizimiz normal de satır ve sutün olmassa dizinin uzunluğu 8'dir.Şimdi bu açıdan satır ve sutünları
#oluştururken de 8'in çarpanları olacak şekilde satır ve sutün değerleri vermemiz gerekir.
print("Shaping version Second Array:   ",secondArrayShaping)
print("")
print("Shaping version Second Array:  ",secondArrayShaping.ndim)

print("")
print("")

firstArrayShaping=np.reshape(firstarray,[2,2])

print("Shaping version First Array:   ",firstArrayShaping)
print("")
print("Shaping version First Array Size:  "+str(firstarray.ndim))

print("")
print("")

#Shapledikten sonra çıktıya aldığınız zaman dizinin boyutları değişmiyor dikkat edin

for a in secondarray:
    print(a)
    #dizi içinde kaç tane liste varsa listeleri liste şeklinde bize döndürüyor
    for b in a:
        print(b)
        #dizi içindeki listenin içine yerleşiyoruz bu sefer ve diyelim ki 1.liste 
        #içine vardı işte 1.listedeki tüm elemanları yazdıracaktır ta ki 
        #dizi içindeki birinci listeyi dolaşmayi bitirene kadar.Birinci listede
        #dolaşma bittikten sonra bu sefer ikinci listede dolaşmaya başlayacak



#***************************************************************************************#

print("")
print("")

fourthArray=np.arange(1,100,2)
#arange fonksiyonu bir başlangıç değerinden bitiş değerine kadar bitiş değeri dahil olmayacak şekilde
#fonksiyonumuzda son parametrede belirlediğimiz(her bir sayı arasındaki fark ya da artış mikarı)
#değer ile bize 1'den 100'e kadar 100 dahil olmayacak 2'şer artacak şekilde bize bir dizi döndürecektir

print("Fourth Array: ",fourthArray)

print("Fourth Array size:  "+str(fourthArray.ndim))

#Dizi içinde elemanları seçme ya da alma yöntemleri

First_Value_of_FourthArray=fourthArray[0]
print("First Value of Fourth Array:  ",First_Value_of_FourthArray)
#Dizinin bir tek eleman erişeceğimiz dizinin isminin yanına kapalı parantez içinde bir sayı giriyoruz.
#Bu sayı dizi için bir indekstir.Zaten bu yöntem de de dizinin bir indeksi ile erişme yöntemidir.
#Dizinin uzunluğu neyse dizideki en son indeks numarası da dizinin uzunluğunun 1 eksisidir.
#Çünkü biliyorsunuz ki indeksler her zaman sıfırdan başlar.

#Eğer uzunluğu aşan bir indeks numarası girersiniz program çalıştığında Boundary(sınırı) aşıldığı
#Exception(hata) fırlatacaktır.


Some_Values_of_FourthArray=fourthArray[2:9]
print("Some Values of Fourth Array:  ",Some_Values_of_FourthArray)
#[2:9] diyerek de dizimizdeki 2.indeksteki değerden başlayıp 9. indeksteki değer dahil olmayacak şekilde
#aradaki tüm değerleri alıp bize bir liste döndürecektir


Some_Values_of_FourthArray1=fourthArray[4:]
#[4:] şu demek oluyor dizideki 4.indeksteki elemandan başla 
#son indeksteki değere kadar tüm değerleri al ve bir liste şekilde bize sonucu döndür demek oluyor
print("Some values of Fourth Array: ",Some_Values_of_FourthArray1)

Some_Values_of_FourthArray2=fourthArray[:4]
print("Some values of Fourth Array:   ",Some_Values_of_FourthArray2)
#[:4] da aslında yukarıdaki tersi yani bu sefer ilk indeks yani 0.indeksteki değerden
#başlayıp 4.indeksteki değer dahil olmayacak şekilde 4.indekse kadar tüm elemanları dolaşıp
#bize sonuç olarak bir liste döndürüyor

#[:,4] , [4,:] vb. kullanımlar da da satır ve sutünları olan dizilerde kullanabiliyoruz
#çünkü bunlar satır ve sutünlardaki değerleri döndürüyor.Tabi bu liste 1 boyutlu olduğu için
#satır ve sutün olmassı söz konusu değil.Peki biz bu listeyi satırli ve sutünlü hale getiremez miyiz?
#Tabiki getirebiliriz reshape() fonksiyonu ile yine bildiğiniz gibi yapabiliriz

#Bu fonksiyonda bildiğiniz iki parametre alıyor birinci aldığı parametre değeri
#sutün(aşağı doğru dizilim) değeridir , ikinci değer ise sutündür(yana doğru dizilim)


#**Reshape yaparken de dizi uzunluğu neyse satır ve sutün değerlerin çarpımı da
#dizi uzunluğuna eşit olacaktır.Aksi durumda programımızda hata fırlatacaktır**

shapeFourthArray=np.reshape(fourthArray,[10,5])

print("Shaping version of Fourth Array:  ",shapeFourthArray)

#fourthArray değerimizi reshape fonksiyonu içinde parametre kullandık ve aynı zamanda
# 10 diyerek aşağı doğru 10 tane sayı yazdıracak(sutün değeri) ve 5 diyerek yan yana 5 tane(satır değeri)
#yazdıracaktır.fourthArray değerimizde değişiklik olmaması için de reshape de parametre olarak kullandık ki
#bu fonksiyonun yani reshape fonksiyonun döndürdüğü sonucu yeni bir değişkene atadık

print("")

fourth_column=shapeFourthArray[:,4]

print("Fifth column of Fourth Array:   ",fourth_column)

#[:,4] diyerek 1. satırı yine indeks olarak baz alarak yani 0.indeks diyerek
#Biz bu komutta 4.indeks olan satırı yani dizimizdeki 5.satırımızdaki değerleri
#bize sonuç olarak döndürecektir 

#Görsel olarak satırları indeks numaraları gösterecek olursak

#0.indeks(1.satır)      #1.indeks(2.satır)         #2.indeks(3.satır)      #3.indeks(4.satır)      #4.indeks(5.satır)
#1   |                  3    |                     5    |                  7    |                  9    |
#11  |                  13   |                     15   |                  17   |                  19   |
#21  |                  23   |                     25   |                  27   |                  29   |
#31  |                  33   |                     35   |                  37   |                  39   |
#41  |                  43   |                     45   |                  47   |                  49   |
#51  |                  53   |                     55   |                  57   |                  59   |
#61  |                  63   |                     65   |                  67   |                  69   |
#71  |                  73   |                     75   |                  77   |                  79   |
#81  |                  83   |                     85   |                  87   |                  89   |
#91  |                  93   |                     95   |                  97   |                  99   |

#Satırların indeksleri gördüğünüz gibi böyle olunca yukarıda yazdığımız [:,4] komutu ile bu satırlardan
#4.indeks olan satıra yani 5.satıra bakacaktır 5.satırdaki tüm değerler üzerinden dolaşacaktır.
#Yani burda yapılan şey önce aranan indeks bulunana kadar satıra ait indeks incelenir burda
#bir doğrusal arama yapılıyor gibi düşünelebilir Big(O)=n gibi.Sonra aranan indeks bulunduktan sonra
#Satırlar arasında seçilen satırın içine girilip her bir değer üzerinden tek tek dolaşılacaktır.Burda da n gibi
#Big o söz konusu.Ama iç içe geçen bir listeler söz konusu bu n'ler çarpılıp n*n gibi bir Big O değeri
#döndürecektir.İç içe yapılar olduğu için çarpım olacaktır

print("")

fourth_row=shapeFourthArray[4,:]

print("Fifth row of Fourth Array:  ",fourth_row)

#Yukarıdaki komutun tersi olacaktır yani bu sefer gidecek dizi içinde 4.indeksi yani 5.satırı arayıp 5.satırı bulduktan
#sonra 5.satırdaki tüm değerleri bize sonuç olarak döndürecektir.

#Görsel olarak şöyle gösterebiliriz

# 0.indeks(1.satır)->1  - 3  - 5  - 7  - 9
# 1.indeks(2.satır)->11 - 13 - 15 - 17 - 19
# 2.indeks(3.satır)->21 - 23 - 25 - 27 - 29
# 3.indeks(4.satır)->31 - 33 - 35 - 37 - 39
# 4.indeks(5.satır)->41 - 43 - 45 - 47 - 49
# 5.indeks(6.satır)->51 - 53 - 55 - 57 - 59
# 6.indeks(7.satır)->61 - 63 - 65 - 67 - 69
# 7.indeks(8.satır)->71 - 73 - 75 - 77 - 79
# 8.indeks(9.satır)->81 - 83 - 85 - 87 - 89
#9.indeks(10.satır)->91 - 93 - 95 - 97 - 99

#Şimdi bu görsel de görüldüğü gibi satırlardan indeksi 4 olanı bulana kadar tek tek satırların indekslerine
#bakacak tabi burda yine tek tek arayacağı için doğrusal arama yapacaktır ki o da Big(o)=n olacaktır
#Tabi aradığımız indeks 0.indeks olsaydı durum değişirdi Big(o)=1 olurdu çünkü tek seferde satıra erişecektir
#Öte yandan biz devam edelim satır ait indekse eriştikten sonra bu sefer satırın içine girecez ve her bir değerini
#yazdıracaz tabiki burda kesinlikle hepsinin üzerinden geçerek yazdıracağımız için burda Big(o)=n olacaktır.Ama tüm
#işlemin Big(o)=n^2 olacaktır.Çünkü bir indeksi araması n bir de tek tek elemanları yazdırması n ikisinin çarpımı söz konusu
#İki olaydan ikincisi birincisi içinde yer aldığı için biz bu arada çarpım yapmaktayız.Tabi eğer biz indeksi tek seferde
#bulsaydık bu sefer 1*n den n olacaktı Big(o).

#Satırı ve sutünü olan bir dizinin içinden tek bir eleman erişmek istersek ne yapacaz?Yine indeks yöntemi kullanacaz
#ama bu sefer iki tane indeks kullanacaz 1. kullanacağımız indeks sutündan bir indeksten olacak,2. kullanacağımız indeks
# ise satırdan gelecektir.Örneğe bakalım

FifthRow_FourthColumn=shapeFourthArray[3,4]
print("Fifth Row and Fourth Column Value:  ",FifthRow_FourthColumn)
#[3,4] diyerek dizimizde sutün olarak 3.indeksin yani 4.sutündan olup
#satır olarak da 4.indeksin yani 5.satırında olan değeri yani kısacası 4.sutünün ve 5.satırın kesişiminde olan değeri 
#döndürecektir.

SeventhColumn_FifthRow=shapeFourthArray[6,4]
print("Seventh Column and Fifth Row Value:  ",SeventhColumn_FifthRow)

FourthColumn_ThirdRow=shapeFourthArray[3,2]
print("Fourth Column and Third Row Value:  ",FourthColumn_ThirdRow)


#Dizimiz ters çevirmek istersek nasıl bir şey yapabiliriz.Aşağıdaki kullanımla bu mümkün

reverse_fourth_array=shapeFourthArray[::-1]

print("Normal version:   ",shapeFourthArray)
print("")
print("Reverse version: ",reverse_fourth_array)

#[::-1] aslında böyle bir kullanımda aslında yapılan işlem şu
# bu listelerde dikkat edin ortada yer bir liste ve yeri reverse olsa bile yeri değişmemiş
# İşte orası orta değer olarak baz alınır ve şu yapılır o orta değerin indeksi neyse o orta değeri ulaşana
# iki uç indeks değerleri arasında yer değişikliği olur.Bu her değiştirilen uç indeks sayıların ortalaması orta değer ya da
# orta indeks sayısını döndürüyor ve tabi yer değişirme sürerken arka planda biz iterasyon yapacak her seferinde bir sayı
# tanımlayıp her bir yer değiştirmede o iterasyon olacak değeri 1'er er artırırız.Bu iterasyon olan değeri ta ki orta indeks
# sayısına eşit olduğunda sayılar arasında yer değiştirme olmayacaktır ki zaten orta değeri gelinecektir zaten yer değiştirildiğinde
# yine kendisi olacaktır.Görselle açıklamak gerekirse

#  0.indeks 
#  1.indeks
#  2.indeks
#  3.indeks
#  4.indeks|--> orta
#  5.indeks|--> değer ya değerler
#  6.indeks
#  7.indeks
#  8.indeks
#  9.indeks 

#orta indeks=(0+9)/2=4.5  yaklaşık 5 denilebilir

#i=0 ==> 4.5 indeks ya da yaklaşık olarak ya 4 ya da 5 değerine ulaşana kadar 1'er 1'er artarak iterasyon yapacak değişken

#Part-1
#Şimdi yer değişimine başlacağımız zman sıfırıncı indeksten başlayacaz ve 0 la neyi toplayip ortlaması alırsak 4.5 elde ederiz
#9 demi o zaman 0.indeks ile 9. indeks arasında yer değişikliği olacak ve i değeri de 1 artırılarak 1 olacak

#Part-2
#Bir eleman kayıyoruz ve bu sefer 1.indeks olan elemana geliyoruz şimdi elemanın indeks sayısı 1.Biri neyle ortalama almaya
#kalkarsak 4.5 değerini elde ederiz 8 ile ortalama alırsak.O zaman 1.indeks olan elemanla 8.indeks olan eleman yer değiştirecek
#i değerimizde 1 artırılarak 2 değeri olacaktır 2 halan orta indeks değerinden küçük o zaman devam demi :) Tabiki

#.
#.
#.

#En sonunda i değeri orta değerden küçük olmadığından normalde orta noktada artık ilerlemeyi durduracaktır.Fakat
#tabi tam bölünemediği için ortadan aslında ortada 4 ile 5 değeri var ki 4.5 değeri de bu iki sayının arasında
#hatta ortasında hatta hatta da 4 ile 5 in ortalaması.O zaman halan bir kere daha ortalamaları 4.5 indeksini döndüren
#iki uç nokta ya da indeks olan elemanların yer değiştirilmesi lazım ki bunlarda 4.indeks eleman ile 5.indeks eleman arasında
#gerçekleşecektir.Artık iterasyon değeri olan i değeri de orta değerden büyük olacak ki bu andan itibaren çalışan
#algoritma duracaktır.Evet [::-1] bu komut aslında elemanlarda kaydırma gibi dense de aslında orta kısımdan bölünüp
#uç değerler arasında yer değiştirme söz konusu ki binary search gibi bir mantık var burda.O açıdan bu komutun aslında
#big(o) suna bakıldığında n/2 ya da logn diyebiliriz.





print("")
print(shapeFourthArray[::-2])
#Bu sefer bu diziyi ters çevirmede sayıları dizerken 2'şer 2'şer ya da 2 nin katlarınca adım sayısı ile
#dizilecektir 

print("")

print(shapeFourthArray[::-3])
#Diziyi tersine çevirirken 3'er 3'er ya da 3'ün katları kadar adım sayısı ile tersten dizilecektir
print("")

print(shapeFourthArray[::-4])

print("")

print(shapeFourthArray[::-5])


print(shapeFourthArray[::1])
#Bu komutta -1 aksine tersten adım sayısı 1 er 1 er yapmak yerine tersi olmayan şekilde 1'er 1'er adımla
#diziliş yapacaktır

print(shapeFourthArray[::2])
#::2 dediğimiz de tersten olmayıp yine bu sefer 2'şer 2'şer ya da 2 in katları şekilde adım sayısıyla
#bir diziliş yapacaktır

#*****************************************#

#Bir dizide belirli adım belirleyerek belirlediğimiz sınırlarda bize yeni bir dizi döndürmesini yaparsak
#nasıl bir şey yapabiliriz.Tabi biz bunu düz bir liste üzerinden size gösterecem.Demek istediğimi bir basit
#örnek üzerinden gösterelim

newList=np.arange(1,50,2)
#1'den 50'ye kadar 50 dahil olmayacak şekilde yeni bir dizi oluşturuyoruz önce

#Diyelim ki bu listenin 3.indexinden 11.indexine kadar 3'er adımla yeni bir dizi almak isteyelim.O zaman şöyle
#bir şey yapacaz.Gelin görelim kullanımı

newlittleList=newList[3:11:3]
#yeni listeden şöyle bir alt küme olacak şekilde yeni değerleri alıp bir liste oluşturduk.
#newList diyip kapalı parantez 3 diyip elemanların alınmaya başlanacağı ilk indexi belirledik,
#ikinci sayı yani 11'de hangi indexe kadar değerler alınacağı söylüyor ve son sayı yani 3 de
#kaçar adımla ilerleyerek her bir sayı değerini alacağını söylüyoruz.
#Görselle gösterecek olursak

#İndexler       0 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
#Normal Küme=> (1 3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49)
#Yeni alt kümemiz(      7_ _ _  13_ _  _  19)
#_ ifadesi adımı ifade eder
#7 de başlangıç olarak belirlediğimiz indexin değeridir
#11 index de 21'dir ama tabi o dahil olmayacağı için ve artış miktarı 3'er 3'er olduğu için en son 19 u alt kümeye
#eleman olacaktır

#Yeni oluşturulan dizi ilk oluşturduğumuz dizinin alt kümesi gibi düşenebilirsiniz.Görselde gerçekleşen olay
#yukarıda yazdığımız komutun yaptığı şeydir
 
print(newList)
print("")
print(newlittleList)

print("")

#***********************************************************#

#Gelelim iki diziyi ya da matrisi birleştirme

#Matris yapı varsa zaten iki farklı şekilde birleştirme vardır.Satır ya da sutün bazlı olacaktır

#O zaman aşağıda  iki matris oluşturalım ve birleştirmeleri yapalim ve nasıl yapildiğini görelim

unReshapeMatrix1=np.array([1,3,5,7,9,11,13,15,17,19])
unReshapeMatrix2=np.arange(1,20,2)

print(unReshapeMatrix1)
print("")
print(unReshapeMatrix2)

print("")

ReshapeMatrix11=unReshapeMatrix1.reshape(5,2)    
ReshapeMatrix21=unReshapeMatrix2.reshape(5,2)

print(ReshapeMatrix11)
print("")
print(ReshapeMatrix21)

print("")

JoiningMatrix1=np.concatenate([ReshapeMatrix11,ReshapeMatrix21],axis=0)
#iki diziyi birleştirmek için numpy kütüphanesindeki
#concatenate fonksiyonu kullanıyoruz ve parametre olarak ilk önce bir liste yapısı alacak ki
#bu liste içinde de listeleri tanımlıyoruz ve diğeri parametremiz ise axis diye bir değerdir
#axis e biz eğer sıfır dersek bize birleştirmeyi satır bazlı yapacaktır.Bi diğer seçeneği
#1'dir ki o da sutün bazlı yapacaktır.

JoiningMatrix2=np.concatenate([ReshapeMatrix11,ReshapeMatrix21],axis=1)


#Satır ya da sutün bazli birleştirmeler yapılacağı zaman matrixlerin boyutları eşit olması gerektiğini bilmelisiniz
#Farklı boyutlardaki iki matrixi birleştirmeye kalktığınız zaman program exception(hata) fırlatacaktır.
#Hata da iki matrisin eksenleri birbiriyle eşleşmesi gerektiğidir.
#Hatta tavsiyem farklı boyutta iki matrisi birleştirmeyi deneyin ve hatayı görün bence bu şekilde kafanıza daha çok yerleşecektir



#Yine ayrıca birleştirme esnasında birleştirecek iki matrisin satır ve sutün sayıları birbiriyle eşleşebilmesi lazım
#yani eşit sayıda olmassı lazım aksi takdirde yine bir hata alacaktır.Hatamızda eşleşme alakalı bir hata olacaktır
#Hatta hatamızın tam ingilizcesi şu şekilde:
#all the input array dimensions except for the concatenation axis must match exactly
#Yani hatanın dediği şey:Dizi için birleştirecek inputlar yani dizilerin eksenleri birbiriyle eşleşmesi gerekiyor

print(JoiningMatrix1)
print("")
print(JoiningMatrix2)

print("")

JoiningMatrix3=np.concatenate([unReshapeMatrix1,unReshapeMatrix2],axis=0)
print(JoiningMatrix3)
#Tek boyutlu dizilerde satır bazlı bir birleştirme yapabiliyoruz gördüğünüz gibi.Axis sıfır dediğimizde satır bazlı
#iki tane tek boyutlu diziyi gayet güzel bir şekilde birleştirecektir.Peki sutün bazlı denersek ne olur :)
print("")
#JoiningMatrix4=np.concatenate([unReshapeMatrix1,unReshapeMatrix2],axis=1)
#Eğer 1 boyutlu matrislerde sutün bazlı bir birleştirme yapmaya kalkarsınız tabiki tek boyutlu olduğu için
#sutünla birleştirmeyecek çünkü bir index yapısı içinde iki sayı yer almamakta.O zaman bir tek satırlar olacaktır
#sutünlar olmayacaktır.O yüzden bu şekilde bir birleştirme yapmaya kalkınca hata verecektir.

#******************************************************#

#Matrislerde Transpoz alma 

#Transpoz alma bir matriste satır olan kısmı sutün yapma,sutünü da satır yapmadır.

#Çok basit bir şekilde bunu yapabilmekteyiz gelin bir örnek yapalim

UnTranspozeMatrix=np.arange(1,15,1)
ReshapeUnTranspoze=UnTranspozeMatrix.reshape(2,7)
print(UnTranspozeMatrix)
print("")
print(ReshapeUnTranspoze)

print("")
ReshapeTranspoze=ReshapeUnTranspoze.T
print(ReshapeTranspoze)

#14 uzunluğuna sahip dizimizin 2 sutün 7 satır şekilde yaptıktan 
#T ifadesi kullandık dikkat edin.Bu Transpoze ifadesini söyleriz aslında ve
#bu 2 sutün olan yapı 2 satır haline döner 7 satır olan da 7 sutüna döner.

#************************************************#

#Matrisler üzerinde dört ya da aritmetik işlemler
#İki matris ile bildiğimiz dört işlemleri gerçekleştirebiliriz.Gelin iki matris oluşturalım ve ardından
#dört işlemleri gerçekleştirelim
print("")
print("1.0 İki matris arasında toplama")


a1=np.arange(1,11,1)

a11=a1.reshape(5,2)

print(a11)

print("+")

print(a11)

print("=")

print(a11+a11)
#İki matrisi toplamak normal toplama gibi toplam operatörünü kullandık gördüğünüz gibi
#Bir de ilk reshape etmediğimiz 1 boyutlu matrisi kendisiyle toplayalım
print("")
print("1.1 İki matrisin toplamı(Tek boyutlu matris)")
print(a1)
print("+")
print(a1)
print("=")
print(a1+a1)

print("")

#Peki şimdi şöyle yapalim boyutları ama dizinin içinde farklı elemanları ile olan şekilde toplama yapalim

#Şimdi aynı boyutta ve uzunlukta fakat dizinin içinde birbirinden farklı elemanlar var.
a2=np.arange(2,12,1)
a3=np.arange(10,20,1)

print("")
print("1.2 İki tek boyutlu matrisin toplami(İçindeki elemanlar farklı bir çoğunun)")
print("")
print(a2)
print("+")
print(a3)
print("=")
print(a2+a3)

#Şimdi bi de a2 ve a3 ün reshape li versiyonu yapıp bir de o şekilde toplamı görelim

a21=a2.reshape(5,2)
a31=a3.reshape(5,2)

print("")
print("1.3 İki tane iki boyutlu matrisin toplami(Eleman içerikleri farkli birçoğunun)")
print("")
print(a21)
print("+")
print(a31)
print("=")
print(a21+a31)
print("")

#*****************************************************************************************#
#Şimdi şöyle bir şekilde toplama yapmaya kalkalım
#Yukarıda reshape yaparken her ikisinin satır ve sutün sayılarına aynı vermiştik
#bir tanesinde Transpoz yapalım yani satırları sutün , sutünları satır yapalım bakalım
#ne olacak???

#Transpoze_a31=a31.T

#print(a21)
#print("+")
#print(Transpoze_a31)
#print("=")
#print(a21+Transpoze_a31)
#Programı çalıştırdığımız da şu şekilde hata alacaz=>operands could not be broadcast together with shapes (5,2) (2,5) 
#Yani operatörler yaptığımız shapeler ile birlikte yayınlanmış olamaz ya da kısaca farklı eksen değerleri ile 
#kullanılamaz ve çalıştırılmaz diyor

#******************************************************************************************************************#


#Çıkarma da ve bölme de yine mantıkla ilerleyebilirsiniz ama çarpım söz konusu olduğunda şöyle bir durum var
#1.matrisin satır sayısı 2.matrisin sutün sayısına eşit olacak ve aynı şekilde
#1.matrisin sutün sayısı da 2.matrisin satır sayısına eşit olmalı.

numpy_array = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_array1 = numpy_array.reshape(5,2)
numpy_array2 = numpy_array.reshape(2,5)

print(numpy_array1)
print(numpy_array2)



