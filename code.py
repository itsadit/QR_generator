import qrcode

def gen_qr(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="purple", back_color="black")
    img.save(file_name)

text = "https://www.google.com/"
file_name = "qrcode.png"
gen_qr(text, file_name)
print(f"QR code saved as {file_name}")
