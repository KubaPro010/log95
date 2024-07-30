import log95

def test():
    log = log95.log95("Test", log95.log95Levels.DEBUG)
    log.log(log95.log95Levels.DEBUG, "Debug", "Deb")
    log.log(log95.log95Levels.VERBOSE, "Verbose", "Verb")
    log.log(log95.log95Levels.CRITICAL_ERROR, "Critical", "Crit")
    log.log(log95.log95Levels.ERROR, "Error", "Err")
    log.log(log95.log95Levels.WARN, "Warn", "War")
    log.log(log95.log95Levels.INFO, "Info", "Inf")
if __name__ == "__main__":
    test()