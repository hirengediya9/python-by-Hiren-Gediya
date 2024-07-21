'''import qrcode as qr
img = qr.make("https://www.myfxbook.com/forex-economic-calendar")
img.save("Myfxbook.png")'''

import qrcode

# QR code ke liye data
data = "https://www.example.com"

# QR code object create karo
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Data add karo QR code mein
qr.add_data(data)
qr.make(fit=True)

# QR code image create karo
img = qr.make_image(fill_color="black", back_color="white")

# QR code image save karo
img.save("qrcode_example.png")
