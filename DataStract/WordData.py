class WordData:
    def __init__(self, word: str, part: str = "", meaning: str = "", example: str = "", symbol: str = "",
                 audio: str = ""):
        self.__word = word
        self.__data = {
            'part': part,
            'meaning': meaning,
            'example': example,
            'symbol': symbol,
            'audio': audio
        }

    def get_word(self) -> str:
        return self.__word

    def get_data(self) -> dict[str, str]:
        return self.__data

    def get_part(self) -> str:
        return self.__data['part']

    def get_meaning(self) -> str:
        return self.__data['meaning']

    def get_example(self) -> str:
        return self.__data['example']

    def get_symbol(self) -> str:
        return self.__data['symbol']

    def get_audio(self) -> str:
        return self.__data['audio']
