from django.urls import path
from .views import LaptopListView,LaptopCreateView,LaptopUpdateView,LaptopDeleteView

urlpatterns=[
    path('listview/',LaptopListView.as_view(),name='listview'),
    path('create/',LaptopCreateView.as_view(),name='create'),
    path('update/<int:pk>',LaptopUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',LaptopDeleteView.as_view(),name='delete')
]