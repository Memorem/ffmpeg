from typing import Any, List

from src.common.exceptions import CommandConcatenateError
from src.ffmpeg.options.base import Options
from src.ffmpeg.options.rubberband import RubberbandOptions


class FilterComplexOptions(Options):
    _flag: str = "-filter_complex"

    def __init__(self, commands: List[Any]) -> None:
        super().__init__(commands)
        self._commands.append(self._flag)

    @property
    def rubberband(self) -> RubberbandOptions:
        return RubberbandOptions(self._commands)

    def add_concat(
        self, *streams_and_tracks: str, number: int, video: int, audio: int, mark: str
    ) -> "FilterComplexOptions":
        if self._commands.count("-i") < 2:
            raise CommandConcatenateError("Concatenation requires at least two inputs")

        flag = f"concat=n={number}:v={video}:a={audio}[{mark}]"
        command = "".join(streams_and_tracks)
        return self.add(command + flag)

    def add_asetrate(self, value: int, ratio: float) -> "FilterComplexOptions":
        return self.add(f"asetrate={value}*{ratio}")


# DOC
"""

n: количество входных потоков.
v: количество видеопотоков.
a: количество аудиопотоков.
output_metas: дополнительная информация о выходном потоке (например, v=0:a=1[out] указывает, что выходной поток должен содержать 1 аудиопоток).

Квадратные скобки [] внутри output_metas являются частью синтаксиса. Они необходимы для указания метки выходного потока. В этом случае, [out] - это метка для выходного потока, который будет использоваться далее в команде.

example:

concat=n=<number_of_streams>:v=<video_streams>:a=<audio_streams>[<output_metas>]


ffmpeg -y -i file1.mp3 -i file2.mp3 -i file3.mp3 -i file4.mp3 -i file5.mp3 \
-filter_complex "[0:0]rubberband=pitch=1.0:tempo=1.0; \
                 [1:0]rubberband=pitch=1.01:tempo=1.01; \
                 [2:0]rubberband=pitch=1.02:tempo=1.02; \
                 [3:0]rubberband=pitch=1.03:tempo=1.03; \
                 [4:0]rubberband=pitch=1.04:tempo=1.04; \
                 concat=n=5:v=0:a=1[out]" \
-map "[out]" -acodec libmp3lame -ab 320k testOUT.mp3


ffmpeg -y -i "Hoaprox, Yuan, Haneri - Saviour.mp3" -i "OSKI - What's The Problem_ [NCS Release].mp3" -i "T & Sugah - For You (ft. Snnr) [NCS Release].mp3" \
-filter_complex "[0:0]rubberband=pitch=1.12:tempo=1.0[a1]; \
                 [1:0]rubberband=pitch=1.12:tempo=1.0[a2]; \
                 [2:0]rubberband=pitch=1.12:tempo=1.0[a3]; \
                 [a1]asetrate=48000*1.05[s1]; \
                 [a2]asetrate=48000*1.05[s2]; \
                 [a3]asetrate=48000*1.05[s3]; \
                 [s1][s2][s3]concat=n=3:v=0:a=1[out]" \
-map "[out]" -acodec libmp3lame -ab 320k -ar 48000 testOUT.mp3


ffmpeg -y -i "Hoaprox, Yuan, Haneri - Saviour.mp3" -i "OSKI - What's The Problem_ [NCS Release].mp3" -i "T & Sugah - For You (ft. Snnr) [NCS Release].mp3" -i "Chromosomes&JACSIN-Origin_Epic_Pop_Heroic_Vocal_Hybrid_Music.m4a" \
-filter_complex "[0:0]rubberband=pitch=1.10:tempo=1.0[a1]; \
                 [1:0]rubberband=pitch=1.10:tempo=1.0[a2]; \
                 [2:0]rubberband=pitch=1.10:tempo=1.0[a3]; \
                 [3:0]rubberband=pitch=1.10:tempo=1.0[a4]; \
                 [a1]asetrate=48000*1.03[s1]; \
                 [a2]asetrate=48000*1.03[s2]; \
                 [a3]asetrate=48000*1.03[s3]; \
                 [a4]asetrate=48000*1.03[s4]; \
                 [s1][s2][s3][s4]concat=n=4:v=0:a=1[out]" \
-map "[out]" -acodec libmp3lame -ab 320k -ar 48000 testOUT.mp3

ffmpeg -y -i "Hoaprox, Yuan, Haneri - Saviour.mp3" -i "OSKI - What's The Problem_ [NCS Release].mp3" -i "T & Sugah - For You (ft. Snnr) [NCS Release].mp3" -i "Chromosomes&JACSIN-Origin_Epic_Pop_Heroic_Vocal_Hybrid_Music.m4a" \
-filter_complex "[0:0]rubberband=pitch=1.15:tempo=1.1[a1]; \
                 [1:0]rubberband=pitch=1.15:tempo=1.1[a2]; \
                 [2:0]rubberband=pitch=1.15:tempo=1.1[a3]; \
                 [3:0]rubberband=pitch=1.15:tempo=1.1[a4]; \
                 [a1][a2][a3][a4]concat=n=4:v=0:a=1[out]" \
-map "[out]" -acodec libmp3lame -ab 320k -ar 48000 testOUT.mp3

ffmpeg -y -i "Hoaprox, Yuan, Haneri - Saviour.mp3" -i "OSKI - What's The Problem_ [NCS Release].mp3" -i "T & Sugah - For You (ft. Snnr) [NCS Release].mp3" -i "Chromosomes&JACSIN-Origin_Epic_Pop_Heroic_Vocal_Hybrid_Music.m4a" \
-filter_complex "[0:0]rubberband=pitch=1.16[a1]; \
                 [1:0]rubberband=pitch=1.16[a2]; \
                 [2:0]rubberband=pitch=1.16[a3]; \
                 [3:0]rubberband=pitch=1.16[a4]; \
                 [a1][a2][a3][a4]concat=n=4:v=0:a=1[out]" \
-map "[out]" -acodec libmp3lame -ab 320k -ar 48000 testOUT.mp3


ffmpeg -i file1.mp4 -i file2.mp4 -i new_audio.mp3 \
-filter_complex "[0:v][0:a][1:v][2:a]concat=n=2:v=1:a=1[outv][outa]" \
-map "[outv]" -map "[outa]" -c:v libx264 -preset veryfast -crf 18 -c:a aac -b:a 192k output.mp4


ffmpeg -y -i "Chromosomes&JACSIN-Origin_Epic_Pop_Heroic_Vocal_Hybrid_Music.m4a" -filter_complex "rubberband=pitch=1.16" -acodec libmp3lame -ab 320k -ar 48000 testOUT.mp3

"""
# DOC
