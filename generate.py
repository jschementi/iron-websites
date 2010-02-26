import sys
import os
import codecs

__thisfile__ = os.path.abspath(os.path.dirname(__file__))

sys.path.append(os.path.join(__thisfile__, 'docutils'))
sys.path.append(os.path.join(__thisfile__, 'docutils/extras'))
sys.path.append(os.path.join(__thisfile__, 'jinja2'))

from docutils.core import publish_parts
from jinja2 import Template
#from pygments.formatters import HtmlFormatter
#PYGMENTS_FORMATTER = HtmlFormatter(style='pastie', cssclass='syntax')

main_path = os.path.join(__thisfile__, 'python\\')
print "main_path: %s" % main_path

NAV = [
    ("Overview", '/'),
    ("Download", "/download"),
    ("Browser", "/browser"),
    ("Documentation", "/documentation"),
    ("Support", "/support"),
]

STYLES = {
    'index.html': 'home columns',
    'download/index.html': 'sub columns',
    'support/index.html': 'sub columns',
    'browser/index.html': 'sub columns',
    'documentation/index.html': 'sub columns',
}

DEFAULT_TEMPLATE = 'templates/page.html'
PAGE_TEMPLATES = {
    'index.html': 'templates/home.html',
    'download/index.html': 'templates/download.html',
}

def page_class(page):
    key = normalize(os.path.relpath(page, main_path))
    return STYLES[key] if key in STYLES else ''

def main_navigation(active_page, path_to_root):
    return ''.join([main_nav_href(nav, active_page, path_to_root) for nav in NAV])

def main_nav_href((name, link), active_page, path_to_root):
    active = is_main_nav_active(active_page, link)
    if active:
        print "(active)"
    
    rel = normalize(os.path.normpath(os.path.join(path_to_root, link if link[0] != '/' else ('.%s' % link))))
    print "link '%s' => %s" % (name, rel)

    t = Template("<a href='{{link}}' {% if active %} class='active' {% endif %}>{{name}}</a>")
    c = { 'link': rel, 'name': name, 'active': active }
    return t.render(c)

def is_main_nav_active(current_path, path):
    path = os.path.join(main_path, path if path[0] != '/' else path[1:])
    if os.path.isdir(path):
        path = os.path.join(path, 'index.html')

    current_path = os.path.join(__thisfile__, current_path)
    
    return os.path.dirname(path) == os.path.dirname(current_path)

def normalize(path):
    return path.replace('\\', '/')

def is_page(expected, page):
    return normalize(os.path.relpath(page, main_path)) == expected

def page_specific_html(page, scope):
    template = None
    for key in PAGE_TEMPLATES.keys():
        if is_page(key, page):
            template = PAGE_TEMPLATES[key]

    if template == None:
        template = DEFAULT_TEMPLATE

    t = Template(open(template).read())
    return t.render(scope)

def main(argv):
    for rst_file in argv:
        rst_file = os.path.abspath(rst_file);
        print "rst_file: %s" % rst_file

        basename, extension = os.path.splitext(rst_file)

        result_file = "%s.html" % basename

        with codecs.open(result_file, 'w', encoding='utf-8') as result:
            print "%s => %s" % (rst_file, result_file)
            
            path_to_root = normalize(os.path.dirname(os.path.relpath(main_path, result_file)))
            path_to_root = "./" if path_to_root == '' else path_to_root
            print "path_to_root: %s" % path_to_root

            path_to_css = normalize(os.path.dirname(os.path.relpath(__thisfile__, result_file)))
            path_to_css = "./" if path_to_css == '' else path_to_css
            print "path_to_css: %s" % path_to_css

            # get the rst file contents and render it into parts
            rst = open(rst_file).read()
            parts = publish_parts(source=rst, writer_name='html')

            # get the main template's content and render it
            template = open('templates/layout.html').read()
            t = Template(template)
            c = {
                'title':        parts['title'],
                'body':         page_specific_html(result_file, {
                                    'body':     parts['body'], 
                                    'title':    parts['title'],
                                    'main_nav': main_navigation(result_file, path_to_root),
                                }),
                'page_class':   page_class(result_file),
                'path_to_root': path_to_root,
                'path_to_css':  path_to_css,
            }
            r = t.render(c)
            result.write(r)

files = [
    'python/index',
    'python/download/index',
    'python/browser/docs',
    'python/browser/index',
    'python/browser/spec.v2',
    'python/documentation/index',
    'python/support/index',
]

print 'removing files'
for file in files:
    if os.path.isfile(file):
        os.remove("%s.html" % file)

if __name__ == "__main__":
    main(["%s.rst" % file for file in files])

