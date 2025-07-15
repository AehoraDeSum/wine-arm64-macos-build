import os
import urllib.request
import tarfile

WINE_VERSION = "9.12"
URL = f"https://dl.winehq.org/wine/source/9.x/wine-{WINE_VERSION}.tar.xz"
DEST = f"wine-{WINE_VERSION}.tar.xz"

print(f"[+] Downloading Wine {WINE_VERSION}...")
urllib.request.urlretrieve(URL, DEST)

print("[+] Extracting archive...")
with tarfile.open(DEST, "r:xz") as tar:
    tar.extractall("../")
print("[+] Done.")
