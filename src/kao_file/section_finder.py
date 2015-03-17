
class SectionFinder:
    """ Represents a method of finding a function from the body of a file """
    
    def __init__(self, startDetectorCls, endDetectorCls):
        """ Initialize the Section Finder with the detectors to use for finding the start and end """
        self.startDetectorCls = startDetectorCls
        self.endDetectorCls = endDetectorCls
        
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
            
        if not self.requestedLineWithinFunction(currentLine, startingLine, endingLine):
            return None

        return file.getSection(startingLine, endingLine)
            
    def findStartingLine(self, currentLine):
        """ Returns the strating line of the function or None """
        startingLine = currentLine
        startDetector = self.startDetectorCls()
        while not startDetector.isStart(startingLine) and not startingLine.isFirstLine():
            startingLine = startingLine.previous()
        
        return startingLine if startDetector.isStart(startingLine) else None
            
    def findEndingLine(self, startingLine):
        """ Returns the strating line of the function or None """
        if startingLine.isLastLine():
            return None
        
        endingLine = startingLine.next()
        endDetector = self.endDetectorCls(startingLine)
        while not endDetector.isEnd(endingLine) and not endingLine.isLastLine():
            endingLine = endingLine.next()
        
        return endingLine if endDetector.isEnd(endingLine) else None
        
    def requestedLineWithinFunction(self, currentLine, startingLine, endingLine):
        """ Return if the current line is actually within the function """
        return startingLine.lineIndex <= currentLine.lineIndex <= endingLine.lineIndex