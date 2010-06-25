@echo off

set csc=C:\Windows\Microsoft.NET\Framework\v3.5\csc.exe
set slpath=%merlin_root%\Utilities\Silverlight\x86ret

if exist %~dp0bin.zip del %~dp0bin.zip

if not exist %~dp0__bin (
    mkdir %~dp0__bin
) else (
    rmdir /Q /S %~dp0__bin
)
%csc% /noconfig /nologo /nostdlib+ /target:library /out:%~dp0__bin\mandelbrotbase.dll /reference:%slpath%\mscorlib.dll,%slpath%\System.dll,%slpath%\System.Windows.dll,%slpath%\System.Core.dll %~dp0mandelbrotbase.cs
%~dp0bin3\chiron.exe /s /d:__bin /x:bin.zip
if exist %~dp0__bin (
    rmdir /Q /S %~dp0__bin
)

echo mandelbrotbase.cs compiled and put in bin.zip
