
def logsinit():
    global LOGSCOLOR
    from colorama import init, Fore
    LOGSCOLOR = Fore
    init()

def log(text: str):
    try:
        print(LOGSCOLOR.YELLOW+'[LOGS] '+LOGSCOLOR.RESET+text)
    except:
        pass # debug off
