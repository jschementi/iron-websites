require 'rubygems'
require File.dirname(__FILE__) + '/app'

use Rack::CommonLogger
use Rack::ShowExceptions

map '/' do
  run MainSite
end

map '/python' do
  run IronPythonNet
end
  
map '/ruby' do
  run IronRubyNet
end