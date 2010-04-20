@echo off
pushd %~dp0
call %~dp0python.bat %~dp0generate.py -python
call %~dp0python.bat %~dp0generate.py -ruby
call %~dp0ruby.bat %~dp0deploy.rb
popd
