from typing import Literal

from src.ffmpeg.base import CommandBuilder
from src.ffmpeg.options import AudioOptions, FilterComplexOptions, VideoOptions


class FFmpegCommandBuilder(CommandBuilder):
    def __init__(
        self, force: bool = False, executor: Literal["ffmpeg"] = "ffmpeg"
    ) -> None:
        super().__init__(executor, force)

    @property
    def audio(self) -> AudioOptions:
        return AudioOptions(self._command)

    @property
    def video(self) -> VideoOptions:
        return VideoOptions(self._command)

    @property
    def filter_complex(self) -> FilterComplexOptions:
        return FilterComplexOptions(self._command)
