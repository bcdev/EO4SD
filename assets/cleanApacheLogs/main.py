# This script removes lines from an Apache log file by using criteria read from a blacklist.
# It is used in the EO4SD project to make the web statistics more reliable in the sense of
# reflecting only users' activity as good as possible.

_author_ = 'uwe'

blacklistFile = "/Volumes/Elephant/Users/uwe/Documents/BC-projects/Development/html/ApacheLogs/blacklist.txt"
apacheLogFile = "/Volumes/Elephant/Users/uwe/Documents/BC-projects/Development/html/ApacheLogs/eo4sd/raw log files/access-eo4sd.brockmann-consult.de.log.2021-01-02-03"
newOutputFile = apacheLogFile + ".cleaned"
cleanedContentFile = apacheLogFile + ".removed"


def read_list(file):
    with open(file) as f:
        _list = f.readlines()
    return _list


if __name__ == '__main__':
    blacklist = read_list(blacklistFile)
    loglist = read_list(apacheLogFile)
    newOutput = open(newOutputFile, 'w')
    cleanedContent = open(cleanedContentFile, 'w')

    for logLineCount in range((len(loglist))):
        _line = loglist[logLineCount].rstrip('\n')
        _clean = True
        # print("Line " + str(logLineCount) + " :: " + _line)
        for blackListLineCount in range(len(blacklist)):
            _searchItem = blacklist[blackListLineCount].rstrip('\n')
            # print("Item: " + _searchItem)
            if _searchItem in _line:
                _clean = False
                print("Found: ", _searchItem, "in line #", logLineCount, _line)
            else:
                continue

        if _clean:
            newOutput.write(_line + '\n')
        else:
            cleanedContent.write(_line + '\n')

    newOutput.close()
    cleanedContent.close()
