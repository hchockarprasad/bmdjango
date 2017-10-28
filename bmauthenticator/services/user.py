from django.contrib.auth.models import User

from bmcore.models import UserProfile


# Add your user service here

class UserService(object):

    model = User

    @staticmethod
    def validate_password(user, password):

        return user.check_password(password)

    def check_user_exists(self, username):

        return self.model.objects.filter(username=username).exists()

    def register(self, username, email, password, **kwargs):

        if self.check_user_exists(username) is False:

            user = self.model.objects.create_user(username, email, password, **kwargs)

            user.set_password(password)

            return user

        return None

    def login(self, username, password):

        user_qs = self.model.objects.filter(username=username)

        if user_qs.exists():

            user_obj = user_qs.first()

            if self.validate_password(user_obj, password):

                return {'status': True, 'message': 'Logged in successfully', 'data': user_obj}

        return {'status': False, 'message': 'Invalid credentials', 'data': None}

    def update(self, user, **kwargs):

        if user:

            first_name = kwargs.get('first_name', None)

            last_name = kwargs.get('last_name', None)

            email = kwargs.get('email', None)

            user_obj = self.model.objects.get(id=user.id)

            user_obj.first_name = first_name

            user_obj.last_name = last_name

            user_obj.email = email

            user_obj.save()

            UserProfile.objects.update(user, **kwargs)

            return user_obj

    def change_password(self, user, password_old, password_new):

        if self.validate_password(user, password_old):

            user.set_password(password_new)

            return {'status': True, 'message': 'Password changed successfully'}

        else:

            return {'status': False, 'message': 'Invalid current password'}
