from django.views.decorators.csrf import csrf_exempt
from django.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from graphene_django.views import GraphQLView
from ninja.security import django_auth

from cookbook.ingredients import views
from cookbook.schema import schema

from rest_framework import routers
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from cookbook.ingredients.api.api import router as ninja_ingredients_router


router = routers.DefaultRouter()
router.register(r'ingredients', views.IngredientViewSet)
router.register(r'categories', views.CategoryViewSet)

# Ninja imports
# we can also enforce CSRF checks
# api = NinjaAPI(urls_namespace='api-ninja', auth=django_auth, csrf=True)
api = NinjaAPI(urls_namespace='api-ninja', auth=django_auth)
api.add_router('/ninja-ingredients/', ninja_ingredients_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('api-ninja/', api.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Put the line provided below into your `urlpatterns` list.
urlpatterns += staticfiles_urlpatterns()
