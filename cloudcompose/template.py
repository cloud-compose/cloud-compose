import jinja2
from os.path import join

class Template:
    def render(self, template_file, template_data):
        template_obj = jinja2.Template(open(template_file).read())
        return template_obj.render(template_data)

