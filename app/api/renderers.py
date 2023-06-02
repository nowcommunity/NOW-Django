from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer, StaticHTMLRenderer, HTMLFormRenderer
from rest_framework.status import is_success, is_redirect
from collections import OrderedDict

class WebRenderer(BrowsableAPIRenderer):
    media_type = 'text/html'
    format = 'web'
    template = 'rest_framework/api.html'

    def get_content(self, renderer, data, accepted_media_type, renderer_context):
        response = renderer_context['response']

        if is_success(response.status_code) or is_redirect(response.status_code):
            # Skip rendering content twice on a successful request
            # Assumes a template overrides the data_content block
            return None

        return super().get_content(renderer, data, accepted_media_type, renderer_context)

    def get_default_renderer(self, view):
        # Used for rendering in get_content
        renderer = StaticHTMLRenderer()
        renderer.template_name = self.template
        return renderer

    def get_context(self, data, accepted_media_type, renderer_context):
        context = super().get_context(data, accepted_media_type, renderer_context)

        if isinstance(data, OrderedDict) and 'results' in data:
            data = data['results']

        context['data'] = data
        context['args'] = renderer_context['args']
        context['kwargs'] = renderer_context['kwargs']

        context = renderer_context['view'].modify_context(context)
        return context

    def render(self, data, accepted_media_type=None, renderer_context=None):
        view = renderer_context['view']
        response = renderer_context['response']

        if is_success(response.status_code) or is_redirect(response.status_code):
            self.template = view.get_template(renderer_context)

        return super().render(data, accepted_media_type, renderer_context)
