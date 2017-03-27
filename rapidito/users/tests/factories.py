import factory


class UserFactory(factory.django.DjangoModelFactory):  # pylint: disable=too-few-public-methods
    username = factory.Sequence('user-{0}'.format)
    email = factory.Sequence('user-{0}@example.com'.format)
    password = factory.PostGenerationMethodCall('set_password', 'password')

    class Meta:  # pylint: disable=too-few-public-methods
        model = 'users.User'
        django_get_or_create = ('username', )
