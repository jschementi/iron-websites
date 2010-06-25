require 'pathname'
require 'fileutils'

class Deploy
  class Transform
    def initialize(to_replace_regex, replacement_str, file_path_str)
      @to_replace_regex = to_replace_regex
      @replacement_str = replacement_str
      @file_path_str = file_path_str
    end

    def perform
      # puts "transforming #{@to_replace_regex.inspect} to #{@replacement_str} in #{@file_path_str}"
      newhtml = File.read(@file_path_str).gsub(@to_replace_regex, @replacement_str)
      File.open(@file_path_str, 'w'){|f| f.write newhtml}
    end
  end

  class IronWebsite
    def initialize(deployment_dir)
      @dir = deployment_dir
    end

    def deploy
      # puts "Deploying #{self.class.content_dir}"
      copy
      transform_css_paths
      transform_image_paths
    end

    def transform_css_paths
      Dir["#{@dir}/**/*.html"].each do |html|
        Transform.new(/\.\.\/css/, "css", html).perform
      end
    end

    def transform_image_paths
      Dir["#{@dir}/**/*.html"].each do |html|
        Transform.new(/\.\.\/images/, 'images', html).perform
      end
    end

    def copy
      FileUtils.mkdir_p @dir
      FileUtils.cp_r "#{self.class.content_dir}/.", @dir
      FileUtils.cp_r 'css', @dir
      FileUtils.cp_r 'images', @dir
      Pathname.glob("#{Pathname(@dir) + 'images'}/*").each do |p|
        p.delete if p.basename.to_s =~ /iron/ && p.basename.to_s !~ /#{self.class.content_dir}/
      end
    end

    def self.content_dir
      throw "Must be implemented in a base-class"
    end
  end

  module Sites
    class IronRubyNet < IronWebsite
      def self.content_dir
        "ruby"
      end
    end

    class IronPythonNet < IronWebsite
      def self.content_dir
        "python"
      end
    end
  end

  def initialize
    @sites = Sites.constants.map do |site|
      Sites.const_get(site).new("deploy/#{site}")
    end
  end

  def clean
    # puts "Cleaning"
    d = Pathname('deploy')
    d.rmtree if d.exist?
  end

  def deploy
    clean
    @sites.each{|s| s.deploy}
  end
end

if __FILE__ == $0
  d = Deploy.new
  if ARGV.include?('-clean')
    d.clean
  else
    d.deploy
  end
end
