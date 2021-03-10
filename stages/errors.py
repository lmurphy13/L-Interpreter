class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def __repr__(self):
        result = f'{0}:{1}'.format(self.error_name, self.details)
        return result

class IllegalCharacterException(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)