require 'rubygems'
require 'sinatra/base'

IronRuby.require 'lib/__init__.py'

module Tilt

  class RSTTemplate < Template
    def initialize_engine
      @rst = IronRuby.require('lib/__rst.py')
    end
    
    def compile!
      @engine = @rst.render(data)
    end
    
    def evaluate(scope, locals, &block)
      @engine
    end
  end
  register 'rst', RSTTemplate

  class JinjaTemplate < Template
    def initialize_engine
      @jinja = IronRuby.require('lib/__jinja.py')
    end
    
    def compile!
      @engine = @jinja.Template(data)
    end
    
    def evaluate(scope, locals, &block)
      @engine.render(locals)
    end
  end
  register 'jinja', JinjaTemplate

end

module Sinatra::Templates
  def rst(template, options={}, locals={})
    render :rst, template, options, locals
  end
  
  def jinja(template, options={}, locals={})
    render :rst, template, options, locals
  end
end