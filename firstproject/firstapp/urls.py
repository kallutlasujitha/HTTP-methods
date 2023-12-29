
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('',views.user)
# ]


# HTML FORM PAGE:

from django.urls import path
from . import views

urlpatterns = [
    path('',views.user,name="user"),
    path('data/',views.details,name="details"),
    path('update/',views.update,name="update"),
    path('delete/<int:id>',views.Delete,name="delete"),
]



















