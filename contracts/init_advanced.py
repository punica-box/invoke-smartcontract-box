from boa.interop.System.App import RegisterAppCall
from boa.interop.System.ExecutionEngine import GetExecutingScriptHash, GetCallingScriptHash, GetEntryScriptHash
from boa.interop.System.Runtime import CheckWitness, GetTime, Notify, Serialize, Deserialize


ContractA = RegisterAppCall('54ab2c2a7833d35fd7a401c05203e995e331f9be', 'operation', 'args')

ContractAddress = GetExecutingScriptHash()


def Main(operation, args):
    if operation == "invokeA":
        if len(args) != 2:
            return False
        opt = args[0]
        params = args[1]
        return invokeA(opt, params)
    return False

def invokeA(operation, params):
    callerHash = GetCallingScriptHash()
    entryHash = GetEntryScriptHash()
    Notify(["111_invokeA",operation, params])
    return ContractA(operation, [params])
