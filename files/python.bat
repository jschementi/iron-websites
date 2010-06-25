@echo off
call %~dp0config.bat
if exist C:\Python26\python.exe (
  C:\Python26\python.exe %* 
) else (
  %dlr_root%\External.LCA_RESTRICTED\Languages\CPython\26\python.exe %*
)
