import cv2 as cv
import numpy as np

cap = cv.VideoCapture('test_data/test3.mp4')

while True:
    ret, frame = cap.read()
    if ret is False:
        break

    # roi = frame[269:795, 537:1416]  # ilgilenen bolge

    rows, cols, _ = frame.shape
    gray_roi = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_roi = cv.equalizeHist(gray_roi)

    gray_roi_blur = cv.GaussianBlur(gray_roi, (3, 3), 7)  # gurultuyu azalmak icin uygulandi

    _, threshold = cv.threshold(gray_roi_blur, 3, 255,
                                cv.THRESH_BINARY_INV)  # bozbegindeki siyah kismi one cikarmak icin thershol kullanildi
    # goz bebegi beyaz diger kisimlar siyah olarak g,zukmesi lazim (THRESH_BINARY_INV)

    contours, _ = cv.findContours(threshold, cv.RETR_TREE,
                                  cv.CHAIN_APPROX_SIMPLE)  # beyaz ggorunen yerlerin koordinatlari  aliyoruz

    contours = sorted(contours, key=lambda x: cv.contourArea(x),
                      reverse=True)  # veride bulunan bazi gorultuleri sistem goz bebegi aliglamamasi icin conturleri siralandi

    for i in contours:
        # cv.drawContours(frame, i, -1, (0, 0, 255), 4)
        (x, y, w, h) = cv.boundingRect(i)
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv.line(frame, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
        cv.line(frame, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)
        break  # breakinamaci sadece birinci counteri cizmek ve donguden cikmak

    cv.imshow('gray_blur', gray_roi_blur)
    cv.imshow('thr', threshold)
    cv.imshow('frame', frame)

    key = cv.waitKey(30)
    if key == 27:  # esc tusu
        break

cv.destroyAllWindows()
