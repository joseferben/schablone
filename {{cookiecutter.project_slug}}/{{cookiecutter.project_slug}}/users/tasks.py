from django.contrib.auth import get_user_model
from huey import crontab
from huey.contrib.djhuey import periodic_task, task

User = get_user_model()


@task()
def get_users_count():
    return User.objects.count()
