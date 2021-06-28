import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from .models import User

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_headerprefix = "bearer".lower()
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        if not auth_header:
            return None
        if len(auth_header) <= 1:
            return None
        elif len(auth_header) > 2:
            return None


        prefix = auth_header[0].decode("utf-8") # Bearer
        
        token = auth_header[1].decode("utf-8")

        if prefix.lower()  != auth_headerprefix:
            return None

        return self._authenticate_credentials(request, token)
    
    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
        except Exception:
            msg = "Invalid token provided"
            raise exceptions.AuthenticationFailed(msg)

        try:
           user = User.objects.get(pk=payload["id"])
        except User.DoesNotExist: 
            msg = "User doesnot exist"
            raise exceptions.AuthenticationFailed(msg)


        return (user, token)
  





