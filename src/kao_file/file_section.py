from kao_decorators import equality_via, proxy_for

@proxy_for('lines', ['__len__', '__iter__', '__getitem__'])
@equality_via('startIndex', 'endIndex', 'lines')
class FileSection:
    """ Represents a section of a file """
    
    def __init__(self, startingLineNumber, endingLineNumber, lines):
        """ Initialize the file section with the lines it encompasses """
        self.startIndex = startingLineNumber
        self.endIndex = endingLineNumber
        self.lines = lines[self.startIndex: self.endIndex+1]