class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


class NameTooLongError(BaseValidationError):
    pass


class NameTooCuteError(BaseValidationError):
    pass

# this allows users of your package to write try…except
# statements that can handle all the errors from this package without
# having to catch them manually


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


def handle_validation_error(err):
    pass


try:
    validate('ali')
except BaseValidationError as err:
    handle_validation_error(err)

