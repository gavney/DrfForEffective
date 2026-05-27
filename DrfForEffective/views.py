from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):

    def get(self, request):

        return Response(
            {
                "project": "DRF for Effective Development by @etogavrusha",

                "stack": [
                    "Python",
                    "Django",
                    "Django REST Framework",
                    "PostgreSQL"
                ],

                "description": (
                    "Backend application with custom JWT authentication "
                    "and RBAC authorization system"
                ),

                "authentication": {
                    "type": "JWT",
                    "header": "Authorization: Bearer <token>",
                    "flow": "register -> login -> access protected endpoints"
                },

                "modules": {
                    "auth": [
                        "/api/auth/register/",
                        "/api/auth/login/",
                        "/api/auth/logout/"
                    ],

                    "users": [
                        "/api/users/me/update/",
                        "/api/users/me/delete/"
                    ],

                    "business": [
                        "/api/business/products/",
                        "/api/business/products/create/",
                        "/api/business/orders/",
                        "/api/business/orders/create/",
                        "/api/business/reports/"
                    ],

                    "rbac": [
                        "/api/rbac/resources/",
                        "/api/rbac/actions/",
                        "/api/rbac/permissions/",
                        "/api/rbac/roles/",
                        "/api/rbac/user-roles/"
                    ]
                },

                "rbac_model": "User → UserRole → Role → Permission → Resource + Action",

                "permission_format": "resource:action",

                "examples": [
                    "products:read",
                    "products:create",
                    "orders:create",
                    "reports:read",
                    "rbac:manage"
                ],

                "roles": {
                    "admin": "full access",
                    "manager": "products/orders/reports limited access",
                    "user": "basic access (read products, create orders)"
                },

                "errors": {
                    "401": "unauthorized (no/invalid/expired token or inactive user)",
                    "403": "forbidden (no permission for resource)"
                }
            }
        )