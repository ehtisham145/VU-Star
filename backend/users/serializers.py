from rest_framework import serializers
from django.contrib.auth import get_user_model
# The main work of serializer is to convert json code to python objects
User = get_user_model()
# Here we are getting the default User model in django which we have defined in the 
# project setting of our django

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    #here write only mode means when the data will be accepted by api in
    # in response API will shown nothing because password is confidentail
 
    class Meta:
        #connectting the Serializer with our model
        model = User
        #Here we are defining the fields name which the Reguster Feature will use
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        # When we use the create_user function then the password in database is stored in hash format
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            role=validated_data.get('role', 'student')
        )
        return user