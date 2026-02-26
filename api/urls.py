from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet, OrderViewSet, CustomerViewSet

app_name = 'api'   # 👈 ye line add karo

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'customers', CustomerViewSet, basename='customers')

urlpatterns = router.urls