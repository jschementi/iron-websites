@echo off
call %~dp0config.bat
if exist C:\Ruby\bin\ruby.exe (
  C:\Ruby\bin\ruby.exe %*
) else (
  %dlr_root%\External.LCA_RESTRICTED\Languages\Ruby\ruby-1.8.6p368\bin\ruby.exe %*
)