from typing import ParamSpec, Generic, Callable, TypeAlias



P = ParamSpec('P')
CallbackMap: TypeAlias = dict[Callable[P, None], int]


class Hook(Generic[P]):
    def __init__(self, check: callable = lambda: True):
        ''' Initialize the Hook with a check function. '''
        self.__callback: CallbackMap[P] = {}
        self.__check = check


    def add_callback(
        self,
        cb: Callable[P, None],
        priority: int = 0
    ):
        target = self.__callback
        target[cb] = priority

        ordered = dict(
            sorted(
                target.items(),
                key=lambda item: item[1],
                reverse=True
            )
        )
        self.__callback = ordered   


    def remove_callback(self, cb: Callable[P, None]):
        self.__callback.pop(cb, None)


    def set_check(self, check: callable):
        self.__check = check


    def working(self) -> bool:
        return self.__check()


    def __call__(self, *args: P.args, **kwargs: P.kwargs):
        if not self.working():
            return
        for cb in self.__callback:
            cb(*args, **kwargs)