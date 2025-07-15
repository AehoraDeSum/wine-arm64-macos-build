# Wine ARM64 macOS Build (Unofficial)

This project provides an unofficial Wine engine build for Apple Silicon (ARM64) Macs. It includes:
- ✅ Python-based automation scripts
- ✅ JavaFX GUI test app
- ✅ Detailed documentation in **both English and Turkish**

## 🐍 Build with Python
```bash
cd python-scripts
python3 download_wine_src.py
python3 build.py
python3 patch_engine.py  # Optional
python3 package_engine.py
```

## ☕ Java Engine Tester (GUI with JavaFX)
```bash
cd java-tools
javac --module-path $PATH_TO_FX --add-modules javafx.controls EngineTesterFX.java
java --module-path $PATH_TO_FX --add-modules javafx.controls EngineTesterFX
```

## 📚 Documentation
See `docs/` folder for both English (`*.en.md`) and Turkish (`*.tr.md`) documentation.
