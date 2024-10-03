from urllib.request import Request, urlopen
from urllib.error import URLError

# we check the validity here first

url = input("Enter a URL you want to turn into a QR code: ")

try:
    req = Request(url)
    response = urlopen(req)
    print("URL is valid!")
except ValueError as e:
    print(f"Invalid URL format: {e}")
except URLError as e:
    print(f"URL is invalid. Error: {e.reason}")
