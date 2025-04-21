import qrcode

code=qrcode.make("https://google.com")
code.save(f"1.png")