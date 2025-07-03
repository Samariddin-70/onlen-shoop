from django.urls import path
from .user import register,sign_in,logo_ut, step_two


urlpatterns = [
    path('regis/', register, name='regis'),
    path('sign_in/', sign_in, name='sign_in'),
    path('logo_ut/', logo_ut,name = 'logo_ut'),
    path('step_two/', step_two, name = 'step_two'   )
]