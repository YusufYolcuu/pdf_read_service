************************************************************
pdfquery -> xml olarak döndürerek konumundan değerlere ulaşılınabiliyor.
Main.py içerisinde pdfquery kütüphanesi kullanıldı beyanname_page1.xml içindeki dataların bbox değeri pushdata fonksiyonu içerisine 
atıldığında textini veriyor.
****************************************************************************************************


tika ->  Değerlerin büyük oranını doğru veriyor ama bazı noktalarda karışıyor.




*********** İstenildiği gibi çalışmayanlar
tabula.py->tabula sadece tabloları okuyan bir kütüphane convertte hata veriyor, foo.pdf dosyasını düzgün okuyor. beyannamelerdeki tabloları algılamıyor
cemalot-> sadece tabloları dönen bir kütüphane. boş tablo dönüyor
pypdf2 -> text olarak okuyor. yazıları sırasız döndürüyor
pdfminer -> text olarak okuyor.  yazıları sırasız döndürüyor. 


pypdfium2 -> documantasyonunu anlayalmadım. kaynakyok. text ayırma performansı iyiymiş.(-* Test edilecek *-)
             https://pypdfium2.readthedocs.io/en/stable/readme.html#usage


excalibur ->  uygulama olarak indirip denedim. cemalot kütüphanesini kullanıyor beyannameleri algılamıyor.


aspose.pdf for python -> download: https://docs.aspose.com/pdf/java/download-and-configure-aspose-pdf-in-python/



***********************************************************************************************************
api: ücretli https://pdftables.com/