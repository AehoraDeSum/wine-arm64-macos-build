## Build Instructions (English)

1. Install dependencies using Homebrew:
```bash
brew install autoconf bison flex pkg-config
```

2. Download Wine source:
```bash
cd python-scripts
python3 download_wine_src.py
```

3. Build Wine for ARM64:
```bash
python3 build.py
```

4. (Optional) Apply custom patches:
```bash
python3 patch_engine.py
```

5. Package the engine:
```bash
python3 package_engine.py
```
