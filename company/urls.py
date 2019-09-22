from django.urls import path
from . import views

app_name = "company"

urlpatterns = [
    path('', views.CompanyList.as_view(), name='company-list'),
    path('add/', views.CompanyCreate.as_view(), name='company-add'),
    path('update/<int:pk>', views.CompanyUpdate.as_view(), name='company-update'),
    path('delete/<int:pk>', views.CompanyDelete.as_view(), name='company-delete'),
    path('detail/<int:pk>', views.CompanyDetail.as_view(), name='company-detail'),
]
