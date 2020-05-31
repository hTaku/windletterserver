from rest_framework import viewsets, routers
from windletterapi.models import User
from windletterapi.serializers import UpdatePositionSerializer, GetMessageSerializer, SendMessageSerializer, CheckDataSerializer
 
class UpdatePositionViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UpdatePositionSerializer

class GetMessageViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GetMessageSerializer

class SendMessageViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SendMessageSerializer

class CheckDataViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CheckDataSerializer

router = routers.DefaultRouter()
router.register(r'updateposition', UpdatePositionViewSet)
router.register(r'getmessage', GetMessageViewSet)
router.register(r'sendmessage', SendMessageViewSet)
router.register(r'checkdata', CheckDataViewSet)