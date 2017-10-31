
class PaymentService(object):

    def __init__(self, user):

        self.user = user

    @property
    def cash_account(self):

        return self.user.userprofile.cash_account
