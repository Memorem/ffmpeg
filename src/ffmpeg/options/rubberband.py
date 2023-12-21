from src.ffmpeg.options.base import Options


class RubberbandOptions(Options):
    _prefix: str = "rubberband="

    def add_tempo(
        self, *streams_and_tracks: str, value: float, concat_to_pitch: bool = False
    ) -> "RubberbandOptions":
        if not isinstance(value, float):
            raise ValueError("Tempo must be a float")
        if concat_to_pitch and streams_and_tracks:
            raise ValueError("Cannot use streams_and_tracks with concat_to_pitch")

        if concat_to_pitch:
            concat_tempo = f":tempo={value}"
            if "pitch" not in self._commands[-1]:
                raise ValueError("Cannot concatenate to None pitch")

            self._commands[-1] += concat_tempo
        else:
            concat_tempo = f"{self._prefix}tempo={value}"
            command = "".join(streams_and_tracks)
            self.add(command + concat_tempo)

        return self

    def add_pitch(
        self, *streams_and_tracks: str, value: float, concat_to_tempo: bool = False
    ) -> "RubberbandOptions":
        if not isinstance(value, float):
            raise ValueError("Pitch must be a float")
        if concat_to_tempo and streams_and_tracks:
            raise ValueError("Cannot use concat_to_tempo with streams_and_tracks")

        if concat_to_tempo:
            concat_pitch = f":pitch={value}"
            if "tempo" not in self._commands[-1]:
                raise ValueError("Cannot concatenate to None tempo")

            self._commands[-1] += concat_pitch
        else:
            concat_pitch = f"{self._prefix}pitch={value}"
            command = "".join(streams_and_tracks)
            self.add(command + concat_pitch)

        return self
