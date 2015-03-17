from kao_decorators import proxy_for

@proxy_for('current', ['lstrip', 'strip', 'rstrip', '__len__', '__iter__', '__getitem__'])
class FileLine:
    """ Represents a line in a file """
    
    def __init__(self, lineIndex, lines):
        """ Initialize the file line with the lines and the index of the line it represents """
        self.lineIndex = lineIndex
        self.lines = lines
        self.current = self.lines[self.lineIndex]
       
    @property
    def lineNumber(self):
        """ Returns the line number of this line """
        return self.lineIndex + 1
        
    def isFirstLine(self):
        """ Return if this is the first line of the file """
        return self.lineIndex == 0
        
    def isLastLine(self):
        """ Return if this is the last line of the file """
        return self.lineIndex == len(self.lines)-1
            
    def previous(self):
        """ Return the next file line """
        if self.isFirstLine():
            return None
        else:
            return FileLine(self.lineIndex-1, self.lines)
        
    def next(self):
        """ Return the next file line """
        if self.isLastLine():
            return None
        else:
            return FileLine(self.lineIndex+1, self.lines)