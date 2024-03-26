import qrcode

#code = qrcode.make('https://github.com/KaanKadirGokcek')
#code.save('vol1.png')

code = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 50,
    border = 5
)

code.add_data('https://github.com/KaanKadirGokcek')
code.make(fit=True)

image = code.make_image(fill_color="black",back_color="red")
image.save('vol2.png')