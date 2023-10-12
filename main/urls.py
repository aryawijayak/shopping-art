from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, increase_product_amount,  decrease_product_amount 
from main.views import register
from main.views import login_user 
from main.views import logout_user
from main.views import edit_product
from main.views import get_product_json, add_product_ajax, remove_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('increase_amount/<int:id>', increase_product_amount, name='increase_product_amount'),
    path('decrease_amount/<int:id>', decrease_product_amount, name='decrease_product_amount'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('remove_product_ajax/<int:id>', remove_product_ajax , name='remove_product_ajax'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
]