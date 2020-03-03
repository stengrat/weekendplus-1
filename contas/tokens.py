from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class AtivacaoConta(PasswordResetTokenGenerator):
    def valor_hash(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.profile.email_confirmado)
        )

contas_token_ativacao = AtivacaoConta()