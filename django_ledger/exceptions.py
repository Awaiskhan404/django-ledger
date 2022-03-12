

from django.core.exceptions import ValidationError


class InvalidDateInputException(ValidationError):
    pass


class TransactionNotInBalanceException(ValidationError):
    pass
