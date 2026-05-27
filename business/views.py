from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from permissions.permissions import HasApiPermission


class ProductsListView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasApiPermission
    ]

    resource = 'products'
    action = 'read'

    def get(self, request):

        data = [
            {
                'id': 1,
                'name': 'Laptop',
                'price': 1200
            },
            {
                'id': 2,
                'name': 'Phone',
                'price': 800
            }
        ]

        return Response(data)


class ProductCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasApiPermission
    ]

    resource = 'products'
    action = 'create'

    def post(self, request):

        return Response(
            {
                'message': 'Product created'
            },
            status=status.HTTP_201_CREATED
        )


class ProductUpdateView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasApiPermission
    ]

    resource = 'products'
    action = 'update'

    def put(self, request, product_id):

        return Response(
            {
                'message': f'Product {product_id} updated'
            }
        )


class ProductDeleteView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasApiPermission
    ]

    resource = 'products'
    action = 'delete'

    def delete(self, request, product_id):

        return Response(
            {
                'message': f'Product {product_id} deleted'
            }
        )


class OrdersListView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasApiPermission
    ]

    resource = 'orders'
    action = 'read'

    def get(self, request):

        data = [
            {
                'id': 1,
                'product': 'Laptop',
                'quantity': 2
            },
            {
                'id': 2,
                'product': 'Phone',
                'quantity': 1
            }
        ]

        return Response(data)


class OrderCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasApiPermission
    ]

    resource = 'orders'
    action = 'create'

    def post(self, request):

        return Response(
            {
                'message': 'Order created'
            },
            status=status.HTTP_201_CREATED
        )


class ReportsView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasApiPermission
    ]

    resource = 'reports'
    action = 'read'

    def get(self, request):

        data = {
            'total_users': 120,
            'total_orders': 540,
            'revenue': 125000
        }

        return Response(data)