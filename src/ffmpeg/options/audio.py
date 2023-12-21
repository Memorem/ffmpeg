from typing import Literal, Union

from src.common.types import (
    AudioBitrateType,
    AudioCodecType,
    AudioSamplingType,
)
from src.ffmpeg.options.base import Options


class AudioOptions(Options):
    def add_codec(
        self, value: AudioCodecType, flag: Literal["-c:a"] = "-c:a"
    ) -> "AudioOptions":
        if flag != "-c:a":
            raise ValueError("Invalid audio codec flag, use '-c:a' instead")

        return self.add([flag, value])

    def add_bitrate(
        self, value: AudioBitrateType, flag: Literal["-b:a"] = "-b:a"
    ) -> "AudioOptions":
        if flag != "-b:a":
            raise ValueError("Invalid audio bitrate flag, use '-b:a' instead")

        return self.add([flag, value])

    def add_sampling(
        self, value: Union[int, AudioSamplingType], flag: Literal["-ar"] = "-ar"
    ) -> "AudioOptions":
        if flag != "-ar":
            raise ValueError("Invalid audio sampling flag, use '-ar' instead")

        return self.add([flag, value])

    def add_filter(self, value: str, flag: Literal["-af"] = "-af") -> "AudioOptions":
        if flag != "-af":
            raise ValueError("Invalid audio filter flag, use '-af' instead")

        return self.add([flag, value])
