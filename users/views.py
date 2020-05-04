import jwt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler

from CRM_FOOD import settings
from .models import User, Role
from .serializers import UserSerializer, RoleSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

class RoleView(ListCreateAPIView):
    model = Role
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserView(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UpdateUserView(RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()




@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        login = request.data['login']
        password = request.data['password']

        user = User.objects.get(login=login, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.name, user.surname)
                user_details['token'] = token
                #user_logged_in.send(sender=user.__class__,
                #                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)
