from django.core.mail import send_mail

def send_confirmation_email(user, code):
    send_mail(
        'Здраствуйте, активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно вести код:'
        f'\n{code}'
        f'\nНе передаватйте этот код никому!',
        'bekurudinov@gmail.com',
        [user],
        fail_silently=False,

    )


