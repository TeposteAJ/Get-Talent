from django.urls import path, include

from empleador.views import InfoEmpleadorPostView

urlpatterns = [ 
    path('user_company/', InfoEmpleadorPostView.as_view()),
    #path('user_company/<int:user_id>/', InfoEmpleadorPostView.as_view()),
]