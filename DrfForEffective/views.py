from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):

    def get(self, request):

        return Response(
            {
                'project': 'DRF for Effective Development by @etogavrusha',

                'description': (
                    'Backend application with custom JWT authentication '
                    'and RBAC authorization system.'
                ),

                'modules': {

                    'authentication': {

                        'register': '/api/auth/register/',
                        'login': '/api/auth/login/',
                        'logout': '/api/auth/logout/',
                    },

                    'users': {

                        'update_profile': '/api/users/me/update/',
                        'delete_account': '/api/users/me/delete/',
                    },

                    'business': {

                        'products': '/api/business/products/',
                        'create_product': '/api/business/products/create/',

                        'orders': '/api/business/orders/',
                        'create_order': '/api/business/orders/create/',

                        'reports': '/api/business/reports/',
                    },

                    'rbac': {

                        'resources': '/api/rbac/resources/',
                        'actions': '/api/rbac/actions/',
                        'permissions': '/api/rbac/permissions/',
                        'roles': '/api/rbac/roles/',
                        'user_roles': '/api/rbac/user-roles/',
                    }
                },

                'authorization': {

                    'type': 'RBAC',

                    'permission_format': 'resource:action',

                    'examples': [

                        'products:read',
                        'products:create',
                        'orders:create',
                        'reports:read',
                        'rbac:manage',
                    ]
                },

                'authentication': {

                    'type': 'JWT',

                    'header': 'Authorization: Bearer <token>',
                }
            }
        )