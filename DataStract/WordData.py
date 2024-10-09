from DataStract.ConstData import ConstData


class WordData:
    def __init__(self, word: str, part: str = "", meaning: str = "", example: str = "", symbol: str = "",
                 audio: str = ""):
        self.__word = word
        self.__part = part
        self.__meaning = meaning
        self.__example = example
        self.__symbol = symbol
        self.__audio = audio

    def is_stop_sign(self) -> bool:
        return self.__word == ConstData.STOP_SIGN

    def get_word(self) -> str:
        return self.__word

    def get_part(self) -> str:
        return self.__part

    def get_meaning(self) -> str:
        return self.__meaning

    def get_example(self) -> str:
        return self.__example

    def get_symbol(self) -> str:
        return self.__symbol

    def get_audio(self) -> str:
        return self.__audio

    def get_all_data(self):
        return {
            'word': self.__word,
            'part': self.__part,
            'meaning': self.__meaning,
            'example': self.__example,
            'symbol': self.__symbol,
            'audio': self.__audio
        }
