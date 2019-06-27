class CustomError(Exception):
    """
    Base error class for custom errors
    """
    pass

class MarketParsingError(CustomError):
    """
    There was a problem parsing the steam market page.
    """