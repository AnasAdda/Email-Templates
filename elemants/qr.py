import qrcode

websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    # Add more websites as needed
]

for url in websites:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".png"
    img.save(filename)
    print(f"QR code saved as {filename}")