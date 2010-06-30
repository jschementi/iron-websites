require 'rubygems'

require 'sinatra/base'

require 'lib/jinja'
require 'lib/rst'

class IronBase < Sinatra::Base
  set :root, File.dirname(__FILE__)
end

class MainSite < IronBase
  set :public, Proc.new { File.join(root, 'public') }

  get '/' do
    File.read("views/index.html")
  end
end

class IronPythonNet < IronBase
  get '' do
    
  end
end

class IronRubyNet < IronBase
  get '' do
    "Hello world from IronRuby.net!"
  end
end
