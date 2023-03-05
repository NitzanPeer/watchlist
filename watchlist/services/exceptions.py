class MovieError(Exception):
    pass

class NoMoviesFoundError(MovieError):
    pass

class MovieAlreadyExistsError(MovieError):
    pass

class StatusAlreadyMarkedThatWay(MovieError):
    pass