from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from .views import PartnerUpdate, RegisterAccount, LoginAccount, AccountDetails, \
    CategoryView, ShopView, OrderView, ContactView, ProductInfoView, PartnerState, \
    BasketView, ConfirmAccount, PartnerOrders, user_logout

urlpatterns = [
    path('partner/update/', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state/', PartnerState.as_view(), name='partner-state'),
    path('user/register/', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm/', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('partner/orders/', PartnerOrders.as_view(), name='partner-orders'),
    path('user/login/', LoginAccount.as_view(), name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('user/details/', AccountDetails.as_view(), name='user-details'),
    path('user/contact/', ContactView.as_view(), name='user-contact'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('shops/', ShopView.as_view(), name='shops'),
    path('order/', OrderView.as_view(), name='order'),
    path('products/', ProductInfoView.as_view(), name='products'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('user/password_reset/', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm/', reset_password_confirm, name='password-reset-confirm'),
]

