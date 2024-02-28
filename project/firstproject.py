import qrcode as qr

img = qr.make("https://youtu.be/ERCMXc8x7mc?si=AV5uiHv1qH0ewW7v")
img.save("youube_qr.png")