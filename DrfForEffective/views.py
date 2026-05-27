from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):

    def get(self, request):

        return Response(
            {
                'message': 'Custom Auth API',

                'available_endpoints': {

                    'register': '/api/auth/register/',
                    'login': '/api/auth/login/',
                    'logout': '/api/auth/logout/',

                    'products': '/api/business/products/',
                    'orders': '/api/business/orders/',
                    'reports': '/api/business/reports/',

                    'profile_update': '/api/users/me/update/',
                    'delete_account': '/api/users/me/delete/',
                }
            }
        )