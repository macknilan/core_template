from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_template.users"
    verbose_name: _("Users")

    def ready(self) -> None:
        """
        Function for user model and profile signals.
        """
        from . import signals
