# Renk Bulma ile Fare Hareketi

Bu Python programı, bir renk aralığına sahip bir ekran görüntüsü yakalar ve o renk aralığına sahip kontur bölgelerinin merkez noktalarını bulur. Ardından fare, bulunan en yakın merkez noktasına taşınır ve tıklama işlemi gerçekleştirilir. Caps Lock tuşuna basarak program kapatılabilir.

Bu projede kullanılan kütüphaneler:

- threading: Çoklu iş parçacıkları oluşturmak için kullanılır.
- time: Zamanla ilgili işlemler yapmak için kullanılır.
- numpy: Bilimsel hesaplamalar ve diziler üzerinde çalışmak için kullanılır.
- cv2: Görüntü işleme işlemleri yapmak için kullanılır.
- keyboard: Tuş basımını izlemek için kullanılır.
- win32api: Windows API işlemleri yapmak için kullanılır.
- win32con: Windows API işlemleri yapmak için kullanılır.
- PIL: Görüntü işleme işlemleri yapmak için kullanılır.
- scipy: Bilimsel hesaplamalar ve matematiksel işlemler yapmak için kullanılır.

## Kod Açıklaması

### Fonksiyonlar

1. `ekran_goruntusu_cek(isim='ekran_goruntusu.jpg')`: Ekran görüntüsü alır ve belirtilen dosya adı ile kaydeder.
2. `fare_hareketi(x, y)`: Fareyi belirtilen x ve y koordinatlarına taşır ve tıklama işlemini gerçekleştirir.
3. `script_kapat()`: Caps Lock tuşuna basıldığında programı kapatır.
4. `renk_bulma(boyut=1)`: Renk aralığına sahip kontur bölgelerinin merkez noktalarını bulur ve fareyi en yakın merkez noktasına taşır ve tıklama işlemini gerçekleştirir.

### Ana Kod

1. `if __name__ == '__main__':`: Ana kodun başlangıcını belirler.
2. `threading.Thread(target=script_kapat).start()`: `script_kapat()` fonksiyonunu başka bir iş parçacığında çalıştırır.
3. `renk_bulma()`: `renk_bulma()` fonksiyonunu çağırır.
