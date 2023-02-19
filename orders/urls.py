from django.urls import path  # re_path
from .views import PartnerUpdate, RegisterAccount, LoginAccount, AccountDetails, \
    CategoryView, ShopView, OrderView, ContactView, ProductInfoView, PartnerState

urlpatterns = [
    path('partner/update/', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state/', PartnerState.as_view(), name='partner-state'),
    path('user/register/', RegisterAccount.as_view(), name='user-register'),
    path('user/login/', LoginAccount.as_view(), name='user-login'),
    path('user/details/', AccountDetails.as_view(), name='user-details'),
    path('user/contact/', ContactView.as_view(), name='user-contact'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('shops/', ShopView.as_view(), name='shops'),
    path('order/', OrderView.as_view(), name='order'),
    path('products/', ProductInfoView.as_view(), name='products'),
    path('shops/', ShopView.as_view(), name='shops'),
]
