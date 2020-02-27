"""Voice TV Control
    https://py.checkio.org/en/mission/voice-tv-control/

    The technologies are rapidly evolving - only 50 years ago a simple
    black-and-white TV was a luxury! And now even a cool big color TV
    with remote control is a common thing. Let's try to improve our
    TV and add the voice control to it! To begin with, we’ll write
    the simple prototype in Python. It’ll use the following commands:

    first_channel() - turns on the first channel from the list.
    last_channel() - turns on the last channel from the list.
    turn_channel(N) - turns on the N channel. Pay attention that the
    channel numbers start from 1, not from 0.
    next_channel() - turns on the next channel. If the current
    channel is the last one, turns on the first channel.
    previous_channel() - turns on the previous channel. If the
    current channel is the first one, turns on the last channel.
    current_channel() - returns the name of the current channel.
    is_exist(N/'name') - gets 1 argument - the number N or the
    string 'name' and returns "Yes", if the channel N or 'name'
    exists in the list, or "No" - in the other case.

    The default channel turned on before all commands is №1.
    Your task is to create the VoiceCommand class and methods described above.
    In this mission you could use the Iterator design pattern.

    Example:

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    controller.first_channel() == "BBC"
    controller.last_channel() == "TV1000"
    controller.turn_channel(1) == "BBC"
    controller.next_channel() == "Discovery"
    controller.previous_channel() == "BBC"
    controller.current_channel() == "BBC"
    controller.is_exist(4) == "No"
    controller.is_exist("BBC") == "Yes"

    Input: The voice commands.
    Output: The channel name or result of the is_exist method.
    Precondition: All commands and channel names are correct.
"""

from functools import singledispatchmethod


def to_yes_no(boolean):
    """Converts boolean value (True/False) to "Yes/No" string"""
    return "Yes" if boolean else "No"


class VoiceCommand(list):
    def __init__(self, channels):
        super().__init__(channels)
        self._index = 0

    @property
    def channel(self):
        return self._index

    @channel.setter
    def channel(self, channel):
        self._index = channel % len(self)

    def first_channel(self):
        self.channel = 0
        return self.current_channel()

    def last_channel(self):
        self.channel = len(self) - 1
        return self.current_channel()

    def turn_channel(self, channel):
        self.channel = channel - 1
        return self.current_channel()

    def next_channel(self):
        self.channel += 1
        return self.current_channel()

    def current_channel(self):
        return self[self.channel]

    def previous_channel(self):
        self.channel -= 1
        return self.current_channel()

    @singledispatchmethod
    def is_exist(self):
        raise NotImplementedError("Supported types are int and str")

    @is_exist.register
    def _(self, channel: int):
        return to_yes_no(channel <= len(self))

    @is_exist.register
    def _(self, channel: str):
        return to_yes_no(channel in self)


if __name__ == "__main__":
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"

    controller.turn_channel(3)
    controller.next_channel()
    controller.current_channel()
    print("PASSED")
