from hyde._compat import reraise


class HydeException(Exception):
    """Base class for exceptions from hyde."""

    @staticmethod
    def reraise(message, exc_info):
        _, _, tb = exc_info
        reraise(HydeException, HydeException(message), tb)
