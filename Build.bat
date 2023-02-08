pyinstaller iFatRainsCrystalWarpRandomizer.pyw --onefile
mkdir dist\syms

Xcopy "logic\syms\*.sym" "dist\syms" /i /y