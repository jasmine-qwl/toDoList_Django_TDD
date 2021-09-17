from accounts.models import User, Token

class PasswordlessAuthenticationBackend(object):

    def authenticate(self, request):
        print('start authentication')
        uid=request.GET.get('token')
        print(uid)
        try:
            token = Token.objects.get(uid=uid)
            print(1)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            print(2)
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            print(3)
            return None

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None