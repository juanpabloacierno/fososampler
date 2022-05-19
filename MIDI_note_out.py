import mido
from mido import Message
msg = Message('note_on', note =60)
msg

outport = mido.open_output()
outport.send (msg)
#print(msg)