from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "id", "first_name", "last_name", "date_joined", "sex", "birthday",
                  "mobile_phone", "is_active", "bookings"
                  ]

    def get_fields(self):
        fields = super().get_fields()

        if not self.context['request'].user.is_staff:
            del fields['bookings']

        return fields


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "id", "first_name", "last_name", "date_joined", "sex", "birthday",
                  "mobile_phone", "is_active", "bookings"
                  ]


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']
