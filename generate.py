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


NAV = [
    ("Overview", '/'),
    ("Download", "/download/"),
    ("Tools", "/tools/"),
    ("Browser", "/browser/"),
    ("Documentation", "/documentation/"),
    ("Support", "/support/"),
]

STYLES = {
    'index.html': 'home columns',
    'download/index.html': 'sub columns',
    'support/index.html': 'sub columns',
    'tools/index.html': 'sub larger tools',
    'browser/index.html': 'sub larger',
    'browser/gettingstarted.html': 'sub',
    'browser/download.html': 'sub',
    'browser/examples.html': 'sub',
    'documentation/index.html': 'sub columns',
}

DEFAULT_TEMPLATE = 'templates/page.html'
PAGE_TEMPLATES = {
    'index.html': 'templates/home.html',
    'download/index.html': 'templates/download.html',
}
PAGE_NAV_FILE = 'nav.py'

language_info = {
  'ironruby': {
    'language': 'Ruby',
    'language_website': 'http://ruby-lang.org',
    'stable_version': '1.0',
    'stable_release_url': 'http://ironruby.codeplex.com/releases/view/25901',
    'stable_release_date': '1.0 released on 2010-04-12',
    'stable_release_notes': 'http://rubyforge.org/frs/shownotes.php?group_id=4359&release_id=43292',
    'stable_release_source': 'http://github.com/IronLanguages/main/zipball/v1.0-rtm',
    'code_snippet_html': """<span class="comment"># namespaces are modules</span>
<span class="keyword">include</span> <span class="constant">System</span>::<span class="constant">Collections</span>::<span class="constant">Generic</span>

<span class="comment"># indexers constrains type</span>
d = <span class="constant">Dictionary</span>[<span class="constant">String</span>, <span class="constant">Fixnum</span>].new

<span class="comment"># Ruby idioms just work</span>
d[<span class="string">'Hello'</span>] = <span class="number">1</span>
d[<span class="string">'Hi'</span>] = <span class="number">2</span>

<span class="comment"># this gives a TypeError</span>
d[<span class="number">3</span>] = <span class="number">3</span>

<span class="comment"># Enumerable methods work</span>
d.each{|kvp| <span class="keyword">puts</span> kvp}""",
  },
  'ironpython': {
    'language': 'Python',
    'language_website': 'http://python.org',
    'stable_version': '2.6.2',
    'stable_release_url': 'http://ironpython.codeplex.com/releases/view/41236#DownloadId=159515',
    'stable_release_date': '2.6.2 released on 2010-10-21',
    'stable_release_notes': 'http://ironpython.codeplex.com/releases/view/41236',
    'stable_release_source': 'http://ironpython.codeplex.com/releases/view/41236#DownloadId=159516',
    'code_snippet_html': """<img src="../images/ironpython-interactive.png" height="279" alt="IronPython Interactive in Visual Studio 2010" />""",
    'old_code_snippet_html': """<span class="comment"># namespaces are modules</span>
<span class="keyword">from</span> <span class="constant">System</span>.<span class="constant">Collections</span>.<span class="constant">Generic</span> import <span class="constant">Dictionary</span>

<span class="comment"># indexers constrains type</span>
d = <span class="constant">Dictionary</span>[<span class="constant">str</span>, <span class="constant">int</span>]()

<span class="comment"># Python idioms just work</span>
d[<span class="string">'Hello'</span>] = <span class="number">1</span>
d[<span class="string">'Hi'</span>] = <span class="number">2</span>

<span class="comment"># this gives an error</span>
d[<span class="number">3</span>] = <span class="number">3</span>""",
  }
}

main_path = __thisfile__
language = None

def page_class(page):
    key = normalize(os.path.relpath(page, main_path))
    return STYLES[key] if key in STYLES else ''

def main_navigation(active_page, path_to_root):
    return ''.join([main_nav_href(nav, active_page, path_to_root) for nav in NAV])

def main_nav_href((name, link), active_page, path_to_root):
    active = is_main_nav_active(active_page, link)
    #if active:
    #    print "(active)"
    
    rel = normalize(os.path.normpath(os.path.join(path_to_root, link if link[0] != '/' else ('.%s' % link))))
    rel = "%s/" % rel
    #print "link '%s' => %s" % (name, rel)

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

def merge_dicts(d1, d2):
  for k in d2:
    d1[k] = d2[k]
  return d1

def main(argv):
    global language
    global main_path
    main_path = os.path.join(__thisfile__, language_info[language]['language'].lower(), '')

    for rst_file in argv:

        rst_file = language_info[language]['language'].lower() + '/'  + rst_file
        rst_file = os.path.abspath(rst_file);
        #print "rst_file: %s" % rst_file

        basename, extension = os.path.splitext(rst_file)

        result_file = "%s.html" % basename

        with codecs.open(result_file, 'w', encoding='utf-8') as result:
            #print "%s => %s" % (rst_file, result_file)
            
            path_to_root = normalize(os.path.dirname(os.path.relpath(main_path, result_file)))
            path_to_root = "./" if path_to_root == '' else path_to_root
            #print "path_to_root: %s" % path_to_root

            path_to_css = normalize(os.path.dirname(os.path.relpath(__thisfile__, result_file)))
            path_to_css = "./" if path_to_css == '' else path_to_css
            #print "path_to_css: %s" % path_to_css

            # get the rst file contents and render it into parts
            rst = open(rst_file).read()
            parts = publish_parts(source=rst, writer_name='html')

            # get the main template's content and render it
            template = open('templates/layout.html').read()
            t = Template(template)

            # sub-page navigation
            navpy_path = os.path.join(os.path.dirname(result_file), PAGE_NAV_FILE)
            subpage_nav = None
            if os.path.exists(navpy_path):
                navpy = eval(open(navpy_path).read().replace("\r",''))
                nav_vars = {
                    'this_page': os.path.relpath(result_file, os.path.dirname(navpy_path)),
                    'nav': navpy,
                }
                subpage_nav = Template(open('templates/nav.html').read()).render(nav_vars)

            # render the main navigation
            main_nav = main_navigation(result_file, path_to_root)

            # each language has it's own template variables
            lang_spec = {
                'language':               language_info[language]['language'],
                'language_lower':         language_info[language]['language'].lower(),
                'language_website':       language_info[language]['language_website'],
                'stable_version':         language_info[language]['stable_version'],
                'stable_release_url':     language_info[language]['stable_release_url'],
                'stable_release_date':    language_info[language]['stable_release_date'],
                'stable_release_notes':   language_info[language]['stable_release_notes'],
                'stable_release_source':  language_info[language]['stable_release_source'],
                'code_snippet_html':      language_info[language]['code_snippet_html'],
            }

            # throw the rst body through the templater too
            parts['body'] = Template(parts['body']).render(lang_spec) 

            # now render the full layout
            r = t.render(merge_dicts({
                'title':        parts['title'],
                'body':         page_specific_html(result_file, merge_dicts({
                                    'body':     parts['body'],
                                    'title':    parts['title'],
                                    'main_nav': main_nav,
                                    'page_nav': subpage_nav,
                                }, lang_spec)),
                'page_class':   page_class(result_file),
                'path_to_root': path_to_root,
                'path_to_css':  path_to_css,
                'main_nav':     main_nav,

            }, lang_spec))
            result.write(r)

files = [
    'index',
    'announcements/index',
    'download/index',
    'tools/index',
    'browser/index',
    'browser/gettingstarted',
    'browser/download',
    'browser/examples',
    'browser/docs',
    'browser/spec.v2',
    'documentation/index',
    'support/index',
]

def usage():
    print "python generate.py [-ruby|-python|-h]"
    exit(1)

import sys
language = 'ironpython'
for i in sys.argv:
    if i == '-ruby':
          language = 'ironruby'
    if i == '-python':
          language = 'ironpython'
    if i == '-h':
          usage()

#print 'removing generated HTML files'
for file in ["%s.html" % file for file in files]:
    if os.path.isfile(language_info[language]['language'] + '/' + file):
        os.remove(language_info[language]['language'] + '/' + file)

if __name__ == "__main__":
    import sys
    main(["%s.rst" % file for file in files])

