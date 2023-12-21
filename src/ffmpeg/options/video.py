from dataclasses import dataclass
from typing import Literal, Optional, Union

from src.common.types import (
    VideoBitrateType,
    VideoCodecType,
    VideoResolutionType,
)
from src.ffmpeg.options.base import Options


@dataclass
class AudioConfig:
    codec: Optional[VideoCodecType] = None
    bitrate: Optional[VideoBitrateType] = None
    resolution: Optional[Union[str, VideoResolutionType]] = None
    filter_value: Optional[str] = None


class VideoOptions(Options):
    def add_config(self, config: AudioConfig) -> "VideoOptions":
        if config.codec:
            self.add_codec(config.codec)
        if config.bitrate:
            self.add_bitrate(config.bitrate)
        if config.resolution:
            self.add_resolution(config.resolution)
        if config.filter_value:
            self.add_filter(config.filter_value)
        return self

    def add_codec(
        self, value: VideoCodecType, flag: Literal["-c:v"] = "-c:v"
    ) -> "VideoOptions":
        if flag != "-c:v":
            raise ValueError("Invalid video codec flag, use '-c:v' instead")

        return self.add([flag, value])

    def add_bitrate(
        self, value: VideoBitrateType, flag: Literal["-b:v"] = "-b:v"
    ) -> "VideoOptions":
        if flag != "-b:v":
            raise ValueError("Invalid video bitrate flag, use '-b:v' instead")

        return self.add([flag, value])

    def add_resolution(
        self, value: Union[str, VideoResolutionType], flag: Literal["-s"] = "-s"
    ) -> "VideoOptions":
        if flag != "-s":
            raise ValueError("Invalid video resolution flag, use '-s' instead")

        return self.add([flag, value])

    def add_filter(self, value: str, flag: Literal["-vf"] = "-vf") -> "VideoOptions":
        if flag != "-vf":
            raise ValueError("Invalid video filter flag, use '-vf' instead")

        return self.add([flag, value])
