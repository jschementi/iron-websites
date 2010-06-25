require 'lib/erb'

module Photoviewer
  class View
    def initialize(app)
      @app = app
    end

    def show_images(flickr, tags, current_page)
      @flickr, @tags, @current_page = flickr, tags, current_page
      
      document.search_images.innerHTML = erb :images
	  document.search_links.innerHTML  = erb :pages
      
      handle_pagination 'search_links'
      
      init_lightbox
    end

    def loading_start
      document.images_loading.style[:display] = "inline"
    end
    
    def loading_finish
      document.images_loading.style[:display] = "none"
      document.search_results.style[:display] = "block"
    end

  private

    def flickr_source(p)
      "http://farm#{ p.farm.to_i }.static.flickr.com/#{ p.server }/#{ p.photo_id }_#{ p.secret }"
    end
    
    def flickr_page(p)
      "http://www.flickr.com/photos/#{ p.owner }/#{ p.photo_id }"
    end

    def flickr_num_pages
      @flickr.photos.pages > 15 ? 15 : @flickr.photos.pages.to_i
    end

    def encode(str)
      System::Windows::Browser::HttpUtility.html_encode str
    end

    def handle_pagination(div)
	  $elem = @app.document.get_element_by_id(div)
      @app.document.get_element_by_id(div).children.each do |child|
        if child.id.to_i == @current_page
          child.css_class = "active"
        elsif child.parent
          child.onclick{|s, args| @app.create_request @tags, child.id.to_i }
        end
      end
    end

    def init_lightbox
      if document.overlay && document.lightbox
        document.overlay.parent.remove_child document.overlay
        document.lightbox.parent.remove_child document.lightbox
      end
      
      window.eval "initLightbox()"
    end

    def erb(template, bind = nil)
      ERB.new(File.read("#{template}.erb")).result(bind || binding)
    end
  end
end
