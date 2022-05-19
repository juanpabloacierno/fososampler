import mido

i = 1
port = mido.get_input_names()  # MIDI port name
# print(port)
inport = mido.open_input()

while i == 1:
    msg = inport.receive()
    print(msg)

    

