import jinja2
from os.path import join

class Template:
    def __init__(self, template_dir):
        self.env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

    def render(self, template_file, template_data):
        template_obj = self.env.get_template(template_file)
        return template_obj.render(template_data)

