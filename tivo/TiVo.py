from .connection import TiVoConnection
from .const import IRCodeCommand

keyboard_lookup= {
    " ": "SPACE",
}

class TiVo(TiVoConnection):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
               
    def send_str(self, str_: str):
        """Send a string to the Tivo"""
        cmd_list = list()
        for char in str_:
            if char in keyboard_lookup.keys():
                char_ = keyboard_lookup[char]
                cmd_list+=[f"KEYBOARD {char_}"]
                continue
            else:
                cmd_list+=[f"KEYBOARD {char}"]
        return self.sendCommands(cmd_list)
        
    def combo(self, コナミコマンド):
        """ Send a combination of commands, in a list, to the tivo"""
        # コナミコマンド
        if isinstance(コナミコマンド, str):
            コナミコマンド = コナミコマンド.split(",")
    
        results = list()
        for cmd in コナミコマンド:
            results+=getattr(self, cmd)()
        return results
        
    def get_chan(self):
        """ Channel Getter"""
        return int(self.send_str("")[0]["channel"])
        
    def set_chan(self, channel):
        """ Channel Setter """
        """ Types on the keyboard, my Tivo doesn't have the SETCH """
        
        # Accept ints.
        if not isinstance(channel, str):
            channel = str(channel)
        # Command list.
        cmds=list()
        for num in channel:
            # Type out each number.
            cmds+=[f"IRCODE NUM{num}"]
        # Press Enter.
        cmds+=["IRCODE ENTER"]
        # Send.
        self.sendCommands(cmds)
    
    chan = property(get_chan, set_chan)

# Good artists steal.
# https://github.com/jed-frey/python_GCode/blob/master/GCode/GCode.py#L74
def ir_code_wrapper(ir_code):
    def ir_code_cmd(self, times=1):
        result = list()
        for _ in range(times):
            result+=self.sendIRCode(ir_code)
        return result
    return ir_code_cmd

for ir_code in dir(IRCodeCommand):
    if ir_code.startswith("_"):
        continue       
    ir_fcn = ir_code_wrapper(ir_code)
    setattr(TiVo, ir_code.lower(), ir_fcn)
    assert hasattr(TiVo, ir_code.lower())
