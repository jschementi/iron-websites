from jinja2 import Template

def render(template, dict):
  return Template(template).render(dict)