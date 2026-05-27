from django.urls import path

from .views import (
    ProductsListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,

    OrdersListView,
    OrderCreateView,

    ReportsView,
)

urlpatterns = [

    # PRODUCTS

    path(
        'products/',
        ProductsListView.as_view(),
        name='products-list'
    ),

    path(
        'products/create/',
        ProductCreateView.as_view(),
        name='product-create'
    ),

    path(
        'products/<int:product_id>/update/',
        ProductUpdateView.as_view(),
        name='product-update'
    ),

    path(
        'products/<int:product_id>/delete/',
        ProductDeleteView.as_view(),
        name='product-delete'
    ),

    # ORDERS

    path(
        'orders/',
        OrdersListView.as_view(),
        name='orders-list'
    ),

    path(
        'orders/create/',
        OrderCreateView.as_view(),
        name='order-create'
    ),

    # REPORTS

    path(
        'reports/',
        ReportsView.as_view(),
        name='reports'
    ),
]