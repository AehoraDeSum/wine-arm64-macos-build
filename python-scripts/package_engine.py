import shutil
print("[+] Packaging Wine engine to .engine bundle...")
shutil.copytree("../build/wine-arm64", "../build/WSCustomARM64.engine", dirs_exist_ok=True)
print("[+] .engine created at ../build/WSCustomARM64.engine")
