from typing import Any, List, Literal, TypeVar

Self = TypeVar("Self", bound="Options")


class Options:
    __slots__ = ("_commands",)

    def __init__(self, commands: List[Any]) -> None:
        self._commands = commands

    def add(self: Self, command: Any) -> Self:
        if isinstance(command, List):
            self._commands.extend(command)
        else:
            self._commands.append(command)

        return self

    def add_map(self: Self, value: str, flag: Literal["-map"] = "-map") -> Self:
        if flag != "-map":
            raise ValueError("Invalid map flag, use '-map' instead")

        return self.add([flag, value])

    def add_prefix(self: Self, *prefixes: str) -> Self:
        self._commands[-1] = "".join(prefixes) + self._commands[-1]

        return self

    def add_suffix(self: Self, *suffixes: str) -> Self:
        self._commands[-1] += "".join(suffixes)

        return self

    def concat_last_commands(
        self: Self, last_command_count: int, sep: Literal[";"] = ";"
    ) -> Self:
        new_commands = self._commands[:-last_command_count] + [
            sep.join(self._commands[-last_command_count:])
        ]
        self._commands.clear()
        self._commands.extend(new_commands)

        return self
