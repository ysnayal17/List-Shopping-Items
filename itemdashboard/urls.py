from django.urls import path
from . import views


urlpatterns = [
    path('', views.item_list, name="home"),
    path('mark_pending/<int:item_id>', views.mark_pending, name="mark_pending"),
    path('mark_done/<int:item_id>', views.mark_done, name="mark_done"),
    path('delete_item/<int:item_id>', views.delete_item, name="delete_item"),
    path('remove_all', views.remove_all, name="remove_all"),
]
