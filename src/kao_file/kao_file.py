from .file_line import FileLine
from .file_section import FileSection

from kao_decorators import proxy_for

@proxy_for('lines', ['__len__'])
class KaoFile:
    """ Represents a file """
    
    @classmethod
    def open(cls, filename):
        """ Open the file as a Kao FIle """
        lines = []
        with open(filename, 'r') as file:
            lines = [line.rstrip() for line in file.readlines()]
        return cls(lines)
    
    def __init__(self, lines):
        """ Initialize the file """
        self.lines = lines
            
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