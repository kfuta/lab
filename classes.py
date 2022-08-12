class Television:
    """
    A class representing functions for a television object, including functions for turning on television power,
    changing channels, and adjusting volume.
    """

    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2

    def __init__(self) -> None:
        """
        Constructor to create initial state of a television object.
        :param self.__channel: the television's initial channel is 0.
        :param self.__volume: the television's initial volume is 0.
        :param self.__status: the television is initially off (false).
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self) -> None:
        """
        Turns the television on if it is off, and off if it is on.
        """
        if self.__status is False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self) -> None:
        """
        If the television is on and the current channel is less than the maximum channel, the channel is increased by
        one. If the television is on and the current channel is the maximum channel, move to the minimum channel.
        """
        if self.__status is True and self.__channel < Television.MAX_CHANNEL:
            self.__channel += 1
        elif self.__status is True and self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        If the television is on and the current channel is greater than the maximum channel, the channel is decreased
        by one. If the television is on and the current channel is the minimum channel, move to the maximum channel.
        """
        if self.__status is True and self.__channel > Television.MIN_CHANNEL:
            self.__channel -= 1
        elif self.__status is True and self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        If the television is on and the current volume is less than the maximum volume, the volume is increased by one.
        """
        if self.__status is True and self.__volume < Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        If the television is on and the current volume is greater than the minimum volume, the volume is decreased by
        one.
        """
        if self.__status is True and self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns information about the television status, channel, and volume.
        :return: Television status, channel, and volume.
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
