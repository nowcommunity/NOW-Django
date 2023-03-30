from rest_framework import routers
from .views import HomeView

class Router(routers.DefaultRouter):
	APIRootView = HomeView

class ApiRouter(routers.DefaultRouter):
	include_root_view = False
