import tkinter as tk
from tkinter import messagebox
from urllib.request import Request
from urllib.error import URLError

# we check the validity here first
# httpstat.us nice site, learnt on the way :)
#~ Request: Creates an HTTP request object with customizable parameters.
#~ URLError: Handles exceptions related to URL access issues.

def generate_url_qr_code():
    
    url = entry_url.get()

    try:
        req = Request(url)
        print("URL is valid!")
        generate_qr_code(url, "qrcode_url.png")

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid URL format, dont forget http:// or https:// : {e}")

    except URLError as e:
        messagebox.showerror("Error", f"URL is invalid. Error: {e.reason}")

def generate_wifi_qr_code():

    ssid = entry_ssid.get()
    encryption = entry_encryption.get().upper()
    password = entry_password.get()
    hidden = entry_hidden.get().lower()

    if not ssid or not password:
        messagebox.showerror("Error", "SSID and Password cannot be empty.")
        return
    
    hidden = hidden == 'yes'

    wifi_data = f"WIFI:T:{encryption};S:{ssid};P:{password};H:{str(hidden).lower()};"
    
    generate_qr_code(wifi_data, "qrcode_wifi.png")

# Common QR code generation function
def generate_qr_code(data, filename):

    from qrcode import QRCode
    import qrcode.constants  

    qr = QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)

    messagebox.showinfo("success", f"QR code saved as {filename}.")

#! set up the main window

app = tk.Tk()
app.title("QR Code Generator")
app.geometry("600x400")

# URL QR Code Entries
tk.Label(app, text="Enter URL:").pack(pady=5)
entry_url = tk.Entry(app, width=50)
entry_url.pack(pady=5)

url_button = tk.Button(app, text="Generate URL QR Code", command=generate_url_qr_code)
url_button.pack(pady=10)

# Wi-Fi QR Code Entries
tk.Label(app, text="Enter SSID:").pack(pady=5)
entry_ssid = tk.Entry(app, width=50)
entry_ssid.pack(pady=5)

tk.Label(app, text="Enter Encryption (WPA/WEP):").pack(pady=5)
entry_encryption = tk.Entry(app, width=50)
entry_encryption.pack(pady=5)

tk.Label(app, text="Enter Password:").pack(pady=5)
entry_password = tk.Entry(app, width=50)
entry_password.pack(pady=5)

tk.Label(app, text="Is the Wi-Fi hidden? (yes/no):").pack(pady=5)
entry_hidden = tk.Entry(app, width=50)
entry_hidden.pack(pady=5)

wifi_button = tk.Button(app, text="Generate Wi-Fi QR Code", command=generate_wifi_qr_code)
wifi_button.pack(pady=10)

app.mainloop()
