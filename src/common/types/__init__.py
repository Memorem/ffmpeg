from typing import Literal, TypeAlias

__all__ = (
    "AudioCodecType",
    "ExecutableFFType",
    "MP3BitrateType",
    "AACBitrateType",
    "FLACBitrateType",
    "VorbisBitrateType",
    "AudioBitrateType",
    "AudioSamplingType",
    "VideoBitrateType",
    "VideoCodecType",
    "VideoResolutionType",
)

ExecutableFFType = Literal["ffmpeg", "ffprobe", "ffplay"]

# Common
AudioLowTierCommonBitrateType: TypeAlias = Literal["8k", "16k", "24k", "32k", "48k"]
AudioMidTierCommonBitrateType: TypeAlias = Literal[
    "64k", "80k", "96k", "112k", "128k", "160k"
]
HighTierCommonBitrateType: TypeAlias = Literal["192k", "224k", "256k", "320k"]

# MP3
MP3BitrateType: TypeAlias = Literal[
    AudioLowTierCommonBitrateType,
    AudioMidTierCommonBitrateType,
    HighTierCommonBitrateType,
]

# AAC
AACBitrateType: TypeAlias = Literal[
    AudioLowTierCommonBitrateType,
    AudioMidTierCommonBitrateType,
    HighTierCommonBitrateType,
]

# Opus
OpusBitrateType: TypeAlias = AudioMidTierCommonBitrateType

# FLAC
FLACBitrateType: TypeAlias = Literal[
    HighTierCommonBitrateType,
    "384k",
    "448k",
    "512k",
    "576k",
    "640k",
    "768k",
    "896k",
    "1024k",
    "1152k",
    "1280k",
    "1408k",
    "1536k",
    "1792k",
    "1920k",
    "2048k",
]

# Vorbis
VorbisBitrateType: TypeAlias = Literal[
    AudioMidTierCommonBitrateType, HighTierCommonBitrateType
]

AudioBitrateType: TypeAlias = Literal[
    AudioLowTierCommonBitrateType,
    AudioMidTierCommonBitrateType,
    FLACBitrateType,
]


AudioCodecType: TypeAlias = Literal[
    "aac",
    "libmp3lame",
    "libopus",
    "flac",
    "libvorbis",
    "pcm_s16le",
    "pcm_s24le",
    "aac_at",
    "pcm_mulaw",
    "pcm_alaw",
    "adpcm_adx",
    "adpcm_g722",
    "adpcm_g726",
    "adpcm_ima_qt",
    "adpcm_ima_wav",
    "adpcm_ms",
    "adpcm_swf",
    "adpcm_yamaha",
    "alac",
    "dca",
    "eac3",
    "g723_1",
    "g729",
    "mp2",
    "mp3",
    "opus",
    "vorbis",
    "wavpack",
    "wmalossless",
    "wmapro",
    "wmav1",
    "wmav2",
    "pcm_f32le",
    "pcm_f64le",
    "pcm_s16be",
    "pcm_s24be",
    "pcm_s32be",
    "pcm_s32le",
    "pcm_u8",
    "real_144",
    "sbc",
]


AudioSamplingType: TypeAlias = Literal[
    "8000",
    "11025",
    "12000",
    "16000",
    "22050",
    "24000",
    "32000",
    "44100",
    "48000",
    "64000",
    "88200",
    "96000",
    "176400",
    "192000",
    "352800",
    "384000",
]

VideoBitrateType: TypeAlias = Literal[
    "100k",
    "200k",
    "300k",
    "400k",
    "500k",
    "600k",
    "800k",
    "1M",
    "1.5M",
    "2M",
    "2.5M",
    "5M",
    "10M",
    "20M",
    "30M",
    "40M",
    "50M",
    "100M",
    "200M",
    "500M",
    "800M",
    "1000M",
    "1500M",
    "2000M",
]

VideoCodecType: TypeAlias = Literal[
    "libx264",
    "libx265",
    "libvpx",
    "libtheora",
    "mpeg4",
    "h264_nvenc",
    "hevc_nvenc",
    "libv4l2",
    "dnxhd",
    "h263",
    "h263p",
    "huffyuv",
    "ffv1",
    "prores",
    "vp8",
    "vp9",
    "av1",
    "msmpeg4",
    "msmpeg4v2",
    "msmpeg4v3",
    "msvideo1",
    "wmv1",
    "wmv2",
    "wmv3",
    "wmv1_v2",
    "wmv2_v2",
    "wmv3_v2",
    "rv10",
    "rv20",
    "rv30",
    "rv40",
    "cinepak",
    "indeo2",
    "indeo3",
    "indeo4",
    "indeo5",
    "flv1",
    "svq1",
    "svq3",
    "gif",
    "mjpeg",
    "libopenh264",
    "libopenh264_v2",
    "libaom",
    "libaom_av1",
    "libvpx_vp8",
    "libvpx_vp9",
    "nvenc_h264",
    "nvenc_hevc",
    "omx_h264",
    "omx_h265",
    "libsvtav1",
    "libsvtvp9",
    "libxavs",
    "libxavs2",
    "libxvid",
    "mpeg1video",
    "mpeg2video",
    "libopenjpeg",
    "libvpx_vp9",
    "libtheora",
    "libaom_av1",
    "libdav1d",
    "libaom_av1",
    "libxavs2",
    "libsvtav1",
    "libsvtvp9",
]

VideoResolutionType: TypeAlias = Literal[
    "320x240",
    "640x360",
    "640x480",
    "720x480",
    "1280x720",
    "1920x1080",
    "2560x1440",
    "2560x1600",
    "3440x1440",
    "3840x1600",
    "3840x2160",
    "5120x2160",
    "7680x4320",
    "1280x800",
    "1440x900",
    "1680x1050",
    "1920x1200",
    "3360x2100",
    "3840x2400",
    "5120x3200",
]
