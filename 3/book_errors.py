# напишите здесь вашу реализацию классов исключений: 
# BookIOErrors, NotExistingExtensionError, PermissionDeniedError
# PageNotFoundError, TooLongTextError

class BookIOErrors(Exception):
    pass
    
class NotExistingExtensionError(BookIOErrors):
    pass

class PermissionDeniedError(BookIOErrors):
    pass
    
class PageNotFoundError(BookIOErrors):
    pass
    
class TooLongTextError(BookIOErrors):
    pass

