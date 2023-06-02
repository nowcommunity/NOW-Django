from rest_framework.utils.urls import replace_query_param
from rest_framework.settings import api_settings

def preserve_view_query_params(view, url, request):
    if hasattr(view, 'filterset_class') and view.filterset_class is not None and hasattr(view, 'get_filterset_class'):
        for (param, options) in view.get_filterset_class().get_filters().items():
            if param and (param in request.GET) or param == api_settings.ORDERING_PARAM:
                value = request.GET[param]
                url = replace_query_param(url, param, value)

    return url
