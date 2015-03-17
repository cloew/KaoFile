
class SectionFinder:
    """ Represents a method of finding a function from the body of a file """
    
    def __init__(self, sectionDetector):
        """ Initialize the Section Finder with the detector to use for finding the start and end """
        self.detector = sectionDetector
        
    def find(self, file, startAt=None):
        """ Returns the function lines that encapsulate the given line number or None """
        if len(file) == 0:
            return None
           
        lineNumber = startAt
        if startAt is None:
            lineNumber = len(file)-1
            
        currentLine = file.getLineAt(lineNumber)
        startingLine = self.findStartingLine(currentLine)
        if startingLine is None:
            return None
            
        endingLine = self.findEndingLine(startingLine)
        if endingLine is None:
            return endingLine

        return file.getSection(startingLine, endingLine)
            
    def findStartingLine(self, currentLine):
        """ Returns the strating line of the function or None """
        startingLine = currentLine
        while not self.detector.isStart(startingLine) and not startingLine.isFirstLine():
            startingLine = startingLine.previous()
        
        return startingLine if self.detector.isStart(startingLine) else None
            
    def findEndingLine(self, startingLine):
        """ Returns the strating line of the function or None """
        if startingLine.isLastLine():
            return None
        
        endingLine = startingLine
        while not self.detector.isEnd(endingLine) and not endingLine.isLastLine():
            endingLine = endingLine.next()
        
        return endingLine if self.detector.isEnd(endingLine) else None