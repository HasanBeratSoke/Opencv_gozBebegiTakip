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
