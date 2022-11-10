from django.contrib.auth import get_user_model
from huey.contrib.djhuey import task

User = get_user_model()


@task()
def get_users_count():
    return User.objects.count()
