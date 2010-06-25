require 'rubygems'

require 'sinatra/base'

class IronBase < Sinatra::Base
  set :root, File.dirname(__FILE__)
end

class MainSite < IronBase
  set :public, Proc.new { File.join(root, 'public') }

  get '/' do
    File.read("index.html")
  end
end

class IronPythonNet < IronBase
  #set :public, Proc.new { File.join(root, 'python/public') }
  #set :view,   Proc.new { File.join(root, 'python/view') }
  
  get '' do
    "Hello World from IronPython.net!"
  end
end

class IronRubyNet < IronBase
  #set :public, Proc.new { File.join(root, 'ruby/public') }
  #set :view,   Proc.new { File.join(root, 'ruby/view') }
  
  get '' do
    "Hello world from IronRuby.net!"
  end
end

