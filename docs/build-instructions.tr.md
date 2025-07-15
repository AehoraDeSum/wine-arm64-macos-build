## Derleme Talimatları (Türkçe)

1. Gerekli bağımlılıkları Homebrew ile yükleyin:
```bash
brew install autoconf bison flex pkg-config
```

2. Wine kaynak kodunu indirin:
```bash
cd python-scripts
python3 download_wine_src.py
```

3. Wine'ı ARM64 için derleyin:
```bash
python3 build.py
```

4. (İsteğe bağlı) Özel yamaları uygulayın:
```bash
python3 patch_engine.py
```

5. Wine motorunu paketleyin:
```bash
python3 package_engine.py
```
