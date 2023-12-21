import abc
import os
import subprocess
from typing import Any, Literal, TypeAlias, TypeVar, Union

from src.common.exceptions import CommandError
from src.common.types import ExecutableFFType

_StrPath: TypeAlias = Union[str, os.PathLike[str]]
Self = TypeVar("Self", bound="CommandBuilder")


class CommandBuilder(abc.ABC):
    __slots__ = ("_command",)

    def __init__(
        self,
        executor: Union[_StrPath, ExecutableFFType],
        force: bool = False,
    ) -> None:
        self._command = [executor]
        if force:
            self._command.append("-y")

    def __call__(self, output_filepath: _StrPath, **kwargs: Any) -> str:
        self._command.append(output_filepath)
        try:
            return subprocess.check_output(self._command, encoding="utf-8", **kwargs)
        except Exception as e:
            raise CommandError from e

    def add_file(self: Self, filepath: _StrPath, flag: Literal["-i"] = "-i") -> Self:
        if flag != "-i":
            raise ValueError("Invalid video input flag, use '-i' instead")

        self._command.extend([flag, filepath])

        return self
