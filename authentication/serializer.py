from rest_framework import serializers

from users.models import User

from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User

        fields = (
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'password',
            'password_confirmation',
        )


    def validate(self, data):
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError("Passwords do not match.")
        
        return data
    

    def create(self, validated_data):
        validated_data.pop('password_confirmation', None)

        password = validated_data.pop('password')

        user = User.objects.create_user(password = password, **validated_data)

        return user

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise serializers.ValidationError("Invalid email or password.")
        else:
            raise serializers.ValidationError("Both email and password are required.")
        
        data['user'] = user

        return data