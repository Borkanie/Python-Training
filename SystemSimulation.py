

# to start venv \env\Scripts\activate.bat
class state:
    def __init__(self, value:int, name:str, sampling_time:int = 10): 
        self.value = value
        self.name = name
        self.sampling_time = sampling_time

class equation:
    def __init__(self, states,equation:str):
       self.states=states
       state_positions={}
       for state in states:
           if state in equation:
               if state not in state_positions.keys():
                   state_positions[state_positions]=[equation.find(state)]
               else:
                     state_positions[state_positions].add([equation.find(state)])