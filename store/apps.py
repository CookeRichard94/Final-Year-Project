from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import store.signals
