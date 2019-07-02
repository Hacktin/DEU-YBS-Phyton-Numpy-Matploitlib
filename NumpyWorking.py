
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

#Komut satir

print("")

print(shapeFourthArray[::-3])
print("")
print(shapeFourthArray[::-4])
print("")
print(shapeFourthArray[::-5])

      

