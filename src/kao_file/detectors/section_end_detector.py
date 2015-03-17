
class SectionEndDetector:
    """ Detects the end of a File Section """
    
    def __init__(self, startingLine):
        """ Initialize with the start of the section """
        self.startingLine = startingLine
    
    def isEnd(self, line):
        """ Returns if the given line is the end of the section  """
        pass