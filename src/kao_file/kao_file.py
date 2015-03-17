from .file_line import FileLine
from .file_section import FileSection

from kao_decorators import proxy_for

@proxy_for('lines', ['__len__'])
class KaoFile:
    """ Represents a file """
    
    def __init__(self, filename=None, lines=None):
        """ Initialize the file """
        if filename is not None:
            with open(filename, 'r') as file:
                self.lines = [line.rstrip() for line in file.readlines()]
        elif lines is not None:
            self.lines = lines
        else:
            raise TypeError("Either Filename or lines must be provided")
            
    def getLineAt(self, index):
        """ Return the File Line at the given index """
        return FileLine(index, self.lines)
            
    def getSection(self, startingLine, endingLine):
        """ Return the File Section for the given lines """
        return FileSection(startingLine.lineIndex, endingLine.lineIndex, self.lines)
            
    def replaceSection(self, section, lines):
        """ Return the File Section for the given lines """
        self.lines[section.startIndex: section.endIndex+1] = lines
        return FileSection(section.startIndex, section.startIndex+len(lines)-1, self.lines)
        
    def save(self, filename):
        """ Save the file """
        with open(filename, 'w') as f:
            f.write('\n'.join(self.lines))
            
    def append(self, lines):
        """ Add the given lines to the end of the file """
        self.lines += lines