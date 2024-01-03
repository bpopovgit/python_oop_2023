from typing import Optional, Any


class CustomList:
    def __init__(self, *args):
        self.__values = list(args)

    def append(self, value: Any):
        self.__values.append(value)
        return self.__values

    def __check_index_type(self, index: int) -> None:
        if not isinstance(index, int):
            raise ValueError("Invalid index type. You must pass an integer")

    def remove(self, index: int) -> Optional[Any]:
        self.__check_index_type(index)

        try:
            element = self.__values.pop(index)
            return element
        except IndexError:
            raise IndexError("Invalid index")

    def safe_remove(self, index: int) -> Optional[Any]:
        self.__check_index_type(index)

        try:
            return self.__values.pop(index)
        except IndexError:
            return None

    def get(self, index: int, default_val: Optional[Any] = None):
        self.__check_index_type(index)
        try:
            return self.__values[index]
        except IndexError:
            if default_val is None:
                return None
            return default_val


