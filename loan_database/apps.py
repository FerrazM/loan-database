from django.apps import AppConfig


class LoanDatabaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loan_database'


class LoanDatabaseConfig(AppConfig):
    name = 'loan_database'

    def ready(self):
        import loan_database.signals
