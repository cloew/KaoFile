from smart_defaults import smart_defaults, ViaField

class SectionFinder:
    """ Represents a method of finding a function from the body of a file """
    DOWN = 0
    UP = 1
    
    def __init__(self, sectionDetector):
        """ Initialize the Section Finder with the detector to use for finding the start and end """
        self.detector = sectionDetector
        
    @smart_defaults
    def find(self, file, startAt=None, direction=ViaField('DOWN')):
        """ Returns the function lines that encapsulate the given line number or None """
        if len(file) == 0:
            return None
           
        lineNumber = startAt
        if startAt is None:
            lineNumber = self.getStartValueFromDirection(direction, file)
            
        currentLine = file.getLineAt(lineNumber)
        startingLine = self.findStartingLine(currentLine, direction)
        if startingLine is None:
            return None
            
        endingLine = self.findEndingLine(startingLine)
        if endingLine is None:
            return endingLine

        return file.getSection(startingLine, endingLine)
        
    def getStartValueFromDirection(self, direction, file):
        """ Return the proper start value for the given direction """
        if direction is self.DOWN:
            return 0
        else:
            return len(file)-1
            
    def findStartingLine(self, currentLine, direction):
        """ Returns the strating line of the function or None """
        startingLine = currentLine
        while not self.detector.isStart(startingLine) and not self.checkAtEdgeOfFile(startingLine, direction):
            if direction is self.DOWN:
                startingLine = startingLine.next()
            else:
                startingLine = startingLine.previous()
        
        return startingLine if self.detector.isStart(startingLine) else None
        
    def checkAtEdgeOfFile(self, line, direction):
        """ Check if the given line is at the edge for the given search direction """
        atEdge = None
        if direction is self.DOWN:
            atEdge = line.isLastLine()
        else:
            atEdge = line.isFirstLine()
        return atEdge
            
    def findEndingLine(self, startingLine):
        """ Returns the strating line of the function or None """
        endingLine = startingLine
        while not self.detector.isEnd(endingLine) and not endingLine.isLastLine():
            endingLine = endingLine.next()
        
        return endingLine if self.detector.isEnd(endingLine) else None