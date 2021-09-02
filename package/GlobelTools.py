from PIL import Image
import qrcode
import os
import time
import datetime


from webpack.settings import BASE_DIR


class GlobelTools:
    def __init__(self):
        pass

    def generateQrcode(self,data,icon=os.path.join(BASE_DIR,'static','img','Jason_Xue','default.png')):
        t = time.time()

        qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image()
        img = img.convert("RGB")


        icon = Image.open(icon)

        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
        # img.show()
        img_name = 'Qrcode'+str(int(t))+'.jpg'
        img.save(os.path.join(BASE_DIR,'static','img','Jason_Xue','Qrcode',img_name))

        return img_name

# GlobelTools().generateQrcode('www.baidu.com')
# print(BASE_DIR)