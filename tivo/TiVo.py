from .connection import TiVoConnection
from .const import IRCodeCommand

class TiVo(TiVoConnection):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def setch(self, channel=231):
        if not isinstance(channel, str):
            channel = str(channel)
        cmds=list()
        for num in channel:
            cmds+=[f"IRCODE NUM{num}"]
        cmds+=["IRCODE ENTER"]
        self.sendCommands(cmds)

# Good artists steal.
# https://github.com/jed-frey/python_GCode/blob/master/GCode/GCode.py#L74
def ir_code_wrapper(ir_code):
    def ir_code_cmd(self):
        return self.sendIRCode(ir_code)
    return ir_code_cmd

class_ = IRCodeCommand
for ir_code in dir(class_):
    if ir_code.startswith("_"):
        continue       
    ir_fcn = ir_code_wrapper(ir_code)
    setattr(TiVo, ir_code.lower(), ir_fcn)
    assert hasattr(Tivo, ir_code.lower())
