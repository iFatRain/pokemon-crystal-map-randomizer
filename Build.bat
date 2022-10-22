pyinstaller iFatRainsCrystalWarpRandomizer.pyw --onefile
mkdir dist\syms

Xcopy "logic\*.sym" "dist\syms" /i /y