import time
import pytest

def test_pause_01(session_uuid, module_uuid, class_uuid, function_uuid, tivo):
    print("*" * 50)
    print("* Session UUID: {}".format(session_uuid))
    print("* Module UUID: {}".format(module_uuid))
    print("* Class UUID: {}".format(class_uuid))
    print("* Function UUID: {}".format(function_uuid))
    print("*" * 50)
    tivo.pause()
    tivo.pause()
    
def test_search(session_uuid, module_uuid, class_uuid, function_uuid, tivo):
    print("*" * 50)
    print("* Session UUID: {}".format(session_uuid))
    print("* Module UUID: {}".format(module_uuid))
    print("* Class UUID: {}".format(class_uuid))
    print("* Function UUID: {}".format(function_uuid))
    print("*" * 50)
    tivo.combo(["livetv", "tivo", "right", "right", "right", "select"])
    tivo.send_str("HELLO WORLD")
    tivo.livetv()

@pytest.mark.parametrize("channel", [231, 232, 233, 235, 240])
def test_pbs(session_uuid, module_uuid, class_uuid, function_uuid, tivo, channel):
    print("*" * 50)
    print("* Session UUID: {}".format(session_uuid))
    print("* Module UUID: {}".format(module_uuid))
    print("* Class UUID: {}".format(class_uuid))
    print("* Function UUID: {}".format(function_uuid))
    print("*" * 50)
    tivo.chan=channel
    
