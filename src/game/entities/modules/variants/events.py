from ..modules import Module
from .....utils import Event
from .....types import Key


class Events(Module):
    '''Events module for entities.'''
    def setup(self):
        self.__set_key_events()
        self.__time_events = {}
        self.owner.press_key.add_callback(self.__on_key_press)


    def assign_time_event(self, name: str, event: callable, interval: float):
        '''Assign a time-based event.'''
        self.__time_events[name] = {
            'event': event,
            'interval': interval,
            'elapsed': 0.0,
        }
        self.owner.update.add_callback(self.__update_time_events)


    def __on_key_press(self, key: Key):
        event = getattr(self, f'on_key_{key.name}_pressed', None)
        if event:
            event()

    
    def __update_time_events(self, delta_time: float):
        remove = []
        
        for event_name in self.__time_events.keys():
            event_data = self.__time_events[event_name]
            event_data['elapsed'] += delta_time
            if event_data['elapsed'] >= event_data['interval']:
                event_data['event']()
                remove.append(event_name)

        for event_name in remove:
            del self.__time_events[event_name]


    def __set_key_events(self):
        # A - Letter events
        self.on_key_A_pressed = Event()
        self.on_key_A_released = Event()
        
        # B - Letter events
        self.on_key_B_pressed = Event()
        self.on_key_B_released = Event()
        
        # C - Letter events
        self.on_key_C_pressed = Event()
        self.on_key_C_released = Event()
        
        # D - Letter events
        self.on_key_D_pressed = Event()
        self.on_key_D_released = Event()
        
        # E - Letter events
        self.on_key_E_pressed = Event()
        self.on_key_E_released = Event()
        
        # F - Letter events
        self.on_key_F_pressed = Event()
        self.on_key_F_released = Event()
        
        # G - Letter events
        self.on_key_G_pressed = Event()
        self.on_key_G_released = Event()
        
        # H - Letter events
        self.on_key_H_pressed = Event()
        self.on_key_H_released = Event()
        
        # I - Letter events
        self.on_key_I_pressed = Event()
        self.on_key_I_released = Event()
        
        # J - Letter events
        self.on_key_J_pressed = Event()
        self.on_key_J_released = Event()
        
        # K - Letter events
        self.on_key_K_pressed = Event()
        self.on_key_K_released = Event()
        
        # L - Letter events
        self.on_key_L_pressed = Event()
        self.on_key_L_released = Event()
        
        # M - Letter events
        self.on_key_M_pressed = Event()
        self.on_key_M_released = Event()
        
        # N - Letter events
        self.on_key_N_pressed = Event()
        self.on_key_N_released = Event()
        
        # O - Letter events
        self.on_key_O_pressed = Event()
        self.on_key_O_released = Event()
        
        # P - Letter events
        self.on_key_P_pressed = Event()
        self.on_key_P_released = Event()
        
        # Q - Letter events
        self.on_key_Q_pressed = Event()
        self.on_key_Q_released = Event()
        
        # R - Letter events
        self.on_key_R_pressed = Event()
        self.on_key_R_released = Event()
        
        # S - Letter events
        self.on_key_S_pressed = Event()
        self.on_key_S_released = Event()
        
        # T - Letter events
        self.on_key_T_pressed = Event()
        self.on_key_T_released = Event()
        
        # U - Letter events
        self.on_key_U_pressed = Event()
        self.on_key_U_released = Event()
        
        # V - Letter events
        self.on_key_V_pressed = Event()
        self.on_key_V_released = Event()
        
        # W - Letter events
        self.on_key_W_pressed = Event()
        self.on_key_W_released = Event()
        
        # X - Letter events
        self.on_key_X_pressed = Event()
        self.on_key_X_released = Event()
        
        # Y - Letter events
        self.on_key_Y_pressed = Event()
        self.on_key_Y_released = Event()
        
        # Z - Letter events
        self.on_key_Z_pressed = Event()
        self.on_key_Z_released = Event()