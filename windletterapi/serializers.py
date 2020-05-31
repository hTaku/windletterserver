from rest_framework import serializers
from windletterapi.models import User, Trajectory
 
class UpdatePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'divice_position')

class GetMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'receive_message_text')

class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'send_message_text')
class CheckDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ChangeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TrajectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajectory