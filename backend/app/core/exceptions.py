class AppException(Exception):
  def __init__(
      self,
      message: str,
      status_code: int = 400,
  ):
    self.message = message
    self.status_code = status_code

class InvalidCredentialsException(AppException):
    def __init__(self):
        super().__init__(
            message="Invalid credentials",
            status_code=401,
        )


class UserAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(
            message="User already exists",
            status_code=400,
        )


class InvalidTokenException(AppException):
    def __init__(self):
        super().__init__(
            message="Invalid token",
            status_code=401,
        )


class ExpiredTokenException(AppException):
    def __init__(self):
        super().__init__(
            message="Token has expired",
            status_code=401,
        )


class UnauthorizedException(AppException):
    def __init__(self):
        super().__init__(
            message="Unauthorized access",
            status_code=403,
        )


class UserNotFoundException(AppException):
    def __init__(self):
        super().__init__(
            message="User not found",
            status_code=404,
        )