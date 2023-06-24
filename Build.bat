pyinstaller iFatRainsCrystalWarpRandomizer.pyw
mkdir dist\iFatRainsCrystalWarpRandomizer\syms

Xcopy "logic\syms\*.sym" "dist\iFatRainsCrystalWarpRandomizer\syms" /i /y

pause