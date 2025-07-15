import os
import subprocess

WINE_DIR = "../wine-9.12"
BUILD_DIR = "../build/wine-arm64"
os.makedirs(BUILD_DIR, exist_ok=True)

env = os.environ.copy()
env["CC"] = "clang"
env["CFLAGS"] = "-target arm64-apple-macos11"

subprocess.run(["../wine-9.12/configure", "--enable-win64", f"--prefix={BUILD_DIR}"], cwd=WINE_DIR, env=env)
subprocess.run(["make", "-j8"], cwd=WINE_DIR)
subprocess.run(["make", "install"], cwd=WINE_DIR)
