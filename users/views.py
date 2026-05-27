from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserUpdateSerializer

class ProfileUpdateView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):

        serializer = UserUpdateSerializer(
            request.user,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
class DeleteAccountView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request):

        user = request.user
        user.is_active = False
        user.save()

        return Response(
            {
                "message": "Account deactivated"
            }
        )
    

