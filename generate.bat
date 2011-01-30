@echo off
pushd %~dp0
python %~dp0generate.py -python
python %~dp0generate.py -ruby
ruby %~dp0deploy.rb
popd
