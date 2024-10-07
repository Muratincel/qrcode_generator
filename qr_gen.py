from urllib.request import Request
from urllib.error import URLError
import qrcode
import qrcode.constants
import keyboard

# we check the validity here first
# httpstat.us nice site, learnt on the way :)
#~ Request: Creates an HTTP request object with customizable parameters.
#~ URLError: Handles exceptions related to URL access issues.

def generate_url_qr_code():
    while True:
        url = input("Enter a URL (http:// or https:// format) you want to turn into a QR code (or press Ctrl+C to exit):")

        try:
            req = Request(url)
            print("URL is valid!")
            return url
        except ValueError as e:
            print(f"Invalid URL format: {e}")
        except URLError as e:
            print(f"URL is invalid. Error: {e.reason}")

def generate_wifi_qr_code():
    ssid = input("Enter the Wi-Fi SSID (Wi-Fi name): ")
    encryption = input("Enter the encryption type (WPA/WEP or leave empty for none): ").upper()
    password = input("Enter the Wi-Fi password: ")
    hidden = input("Is the Wi-Fi hidden? (yes/no): ").lower()

    if hidden == 'yes':
        hidden = True
    else:
        hidden = False

    # Wi-Fi QR Code string
    wifi_data = f"WIFI:T:{encryption};S:{ssid};P:{password};H:{str(hidden).lower()};"
    
    return wifi_data

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)

    print("QR code has been generated and saved as '{filename}'.")

    return img

#! Main program starts here

print("Welcome to the QR Code Generator!")
print("Choose the type of QR code to generate:")
print("1. URL QR Code")
print("2. Wi-Fi Connection QR Code")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    url_data = generate_url_qr_code()
    img = generate_qr_code(url_data, "qrcode_url.png")
elif choice == '2':
    wifi_data = generate_wifi_qr_code()
    img = generate_qr_code(wifi_data, "qrcode_wifi.png")
else:
    print("Invalid choice. please enter 1 or 2")
    exit()


print("If you want to display the QR code, press Enter... (Press Esc to exit)")

while True:
    if keyboard.is_pressed('esc'):
        print("Exiting program...")
        break
    if keyboard.is_pressed('enter'):
        img.show()
        break