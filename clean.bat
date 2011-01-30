@echo off
python %~dp0clean.py -python
python %~dp0clean.py -ruby
ruby %~dp0deploy.rb -clean