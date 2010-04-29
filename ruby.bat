@echo off
call %~dp0config.bat
%dlr_root%\External.LCA_RESTRICTED\Languages\Ruby\ruby-1.8.6p368\bin\ruby.exe %*
