@echo off
call %~dp0config.bat
%merlin_root%\..\External.LCA_RESTRICTED\Languages\CPython\26\python.exe %*
