@echo off
call %~dp0python.bat %* %~dp0generate.py
call %~dp0ruby.bat %~dp0deploy.rb
