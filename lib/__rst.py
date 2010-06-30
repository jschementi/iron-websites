from docutils.core import publish_parts

def render(text):
  parts = publish_parts(source=text, writer_name='html')
  return parts['body']