# Opencv ile göz bebeği takibi
---
![demo](https://github.com/HasanBeratSoke/Opencv_gozBebegiTakip/blob/main/readmeData/goztest.gif)
---
## Araçlar
```
Numpy
Opencv
```
---

### Sistemin Önemli Aşamaları
1- Sistemdeki görültülerden kurtulmak için görüntümüze blur ulgulandı.
```Python
gray_roi_blur = cv.GaussianBlur(gray_roi, (3, 3), 7)
```
![demo](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Halftone%2C_Gaussian_Blur.jpg/220px-Halftone%2C_Gaussian_Blur.jpg)

2- Göz bebeğin içerindeki siyah noktayı ayırt etmek için, görüntümüze threshold uygulandı.
  * 0-255 arasında degerler verilebilir. 0 en koyu 255 ise en aydınlık şeklindedir.
  * threshold methodu olarak  `cv.THRESH_BINARY_INV` methodu kullanıldı. Yani koyu verdiğimiz değerdeki kısımlar beyaz diğer kısımlar ise siyah şeklinde gösterilecektir.
```Python
_, threshold = cv.threshold(gray_roi_blur, 3, 255,
                                cv.THRESH_BINARY_INV)
                                
                               
```

![demo](https://929687.smushcdn.com/2633864/wp-content/uploads/2021/04/opencv_thresholding_coins02.jpg?lossy=1&strip=1&webp=1)

3- Bulunana beyaz kısımları tespit edilmesi ve koordinatlarının alınması için Contours methodu kullanıldı.
```Python
contours, _ = cv.findContours(threshold, cv.RETR_TREE,
                                  cv.CHAIN_APPROX_SIMPLE)
```
  * contourslari yazdirildigi zaman bize maskelediğimiz yerlerin koordinatlerını verir.
  * eğer bunları çizdirmek içinde `cv.drawContours(frame, i, -1, (0, 0, 255), 4)` fonk. kullanabiliriz.
  - ama burada hala bi problem mevcuttur, resmimizde hala görültüler mevcuttur ve bunları gideremedik
  - ![demo](https://github.com/HasanBeratSoke/Opencv_gozBebegiTakip/blob/main/readmeData/ss.png)
  
   burada contour ları sıralayıp sadece en büyüğünü yazdırarak propbleme gecici cözüm üretebiliriz.
   ```Python
   contours = sorted(contours, key=lambda x: cv.contourArea(x),
                      reverse=True)
   ``` 
   buradakı contoru belirledikden sonra isterseniz yuvarlak içine istersenizde kare içine alabilirsiniz. 
   ```Python
       for i in contours:
        # cv.drawContours(frame, i, -1, (0, 0, 255), 4)
        (x, y, w, h) = cv.boundingRect(i)
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv.line(frame, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
        cv.line(frame, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)
        break  # breakinamaci sadece birinci counteri cizmek ve donguden cikmak icin
   ```
---
#### yararlandigim rehberler
+ https://www.youtube.com/watch?v=z7fiml2iZzo
+ https://learnopencv.com/opencv-threshold-python-cpp/
+ https://docs.opencv.org/4.x/df/d0d/tutorial_find_contours.html
  
   
