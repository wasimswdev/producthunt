from django.urls import path,include
import products.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('create/',products.views.create,name='create'),
path('<int:product_id>',products.views.detail,name='detail'),
path('<int:product_id>/upvote',products.views.upvote,name='upvote'),


] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
