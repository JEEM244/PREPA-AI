# PyInstaller spec for a portable Windows console executable.
from PyInstaller.utils.hooks import collect_submodules

hidden = collect_submodules("prepa_ai")
a = Analysis(
    ["cli/launcher.py"],
    pathex=["cli"],
    binaries=[],
    datas=[],
    hiddenimports=hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["tkinter", "unittest"],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, a.binaries, a.datas, [],
    name="PREPA-AI",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
)
