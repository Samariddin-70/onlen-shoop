from django.urls import path,include

urlpatterns =[
    path('',include( 'cors.site_views.urls' )),
    path('dashboard/', include( 'cors.dashboard_views.urls' )),
]