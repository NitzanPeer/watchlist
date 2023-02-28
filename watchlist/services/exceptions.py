class MovieError(Exception):
    pass

class NoMoviesFoundError(MovieError):
    pass

class MovieAlreadyExistsError(MovieError):
    pass