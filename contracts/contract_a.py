
from boa.interop.System.Runtime import Notify

def Main(operation, args):
    if operation == "getData":
        Notify(['contractA11111'])
        Notify(args)
        Notify(len(args))
        if len(args)!=1:
            return False
        key = args[0]
        return getData(key)
    return False

def getData(key):
    Notify(['2222222', key])
    return key
