import inspect
from typing import ParamSpec, Generic, Callable, TypeAlias



P = ParamSpec('P')
CallbackMap: TypeAlias = dict[Callable[P, None], int]


class Event(Generic[P]):
    def __init__(self, check: callable = lambda: True):
        ''' Initialize the Hook with a check function. '''
        self.__callback: CallbackMap[P] = {}
        self.__check = check

    
    def clear_callbacks(self):
        ''' Clear all callbacks. '''
        self.__check = lambda: False


    def add_callback(
        self,
        cb: Callable[P, None],
        priority: int = 0
    ):
        ''' Add a callback with an optional priority. '''
        self.__callback[cb] = priority
        self.__callback = dict(
            sorted(
                self.__callback.items(),
                key=lambda item: item[1],
                reverse=True
            )
        )   


    def remove_callback(self, cb: Callable[P, None]):
        ''' Remove a callback. '''
        self.__callback.pop(cb, None)


    def set_check(self, check: callable):
        ''' Set the check function. '''
        self.__check = check


    def working(self) -> bool:
        ''' Check if the event is working. '''
        return self.__check()


    def debug(self):
        self.add_callback(lambda *args, **kwargs: print("Event triggered with args:", args, "and kwargs:", kwargs))


    def __call__(self, *args: P.args, **kwargs: P.kwargs):
        '''Call the event, executing all callbacks if working.

        If a callback expects no parameters, it is invoked without args to avoid
        signature mismatches when events supply collision data.
        '''
        if not self.working():
            return

        for cb in self.__callback:
            sig = inspect.signature(cb)
            if len(sig.parameters) == 0:
                cb()
            else:
                cb(*args, **kwargs)