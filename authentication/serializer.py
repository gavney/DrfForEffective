from rest_framework import serializers

from users.models import User

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
            'password_confirm',
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

        user = User.objects.create(password = password, **validated_data)

        return user
