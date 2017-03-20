import factory


class UserFactory(factory.django.DjangoModelFactory): # pylint: disable=too-few-public-methods
    username = factory.Sequence(lambda n: 'user-{0}'.format(n)) # pylint: disable=unnecessary-lambda
    email = factory.Sequence(lambda n: 'user-{0}@example.com'.format(n)) # pylint: disable=unnecessary-lambda
    password = factory.PostGenerationMethodCall('set_password', 'password')

    class Meta: # pylint: disable=too-few-public-methods
        model = 'users.User'
        django_get_or_create = ('username', )
