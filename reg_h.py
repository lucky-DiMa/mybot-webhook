import  commands_scripts
import msg_answer_scripts
import inline_scripts

def reg_handlers():
    msg_answer_scripts.reg_handlers()
    commands_scripts.reg_handlers()
    inline_scripts.reg_handlers()
