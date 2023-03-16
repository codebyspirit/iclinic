from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from connexion.serializers import UserSerializer
from connexion.models import User
import jwt, datetime

#from validate_email import validate_email
from email_validator import validate_email, EmailNotValidError
from django.core.exceptions import ValidationError


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        try:
            v = validate_email(request.data['email'])
            email = v["email"] 
        except EmailNotValidError as e:
            raise AuthenticationFailed(str(e))

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        #if not validate_email(request.data['email']):
        #    raise AuthenticationFailed('email')
        try:
            # validate and get info
            v = validate_email(request.data['email'])
            # replace with normalized form
            email = v["email"] 
            #print("True")
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            #print(str(e))
            raise AuthenticationFailed(str(e))

        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('user not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow() 
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')#.decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'jwt':token}
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        #user = User.objects.filter(id=payload['id'])
        user = User.objects.all()#ilter(id=payload['id'])
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)            


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'message': 'success'}
        return response
        
