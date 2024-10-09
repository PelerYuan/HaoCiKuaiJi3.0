class WordData:
    def __init__(self, word: str, part: str = "", meaning: str = "", example: str = "", symbol: str = "",
                 audio: str = ""):
        self.__word = word
        self.part = part
        self.meaning = meaning
        self.example = example
        self.symbol = symbol
        self.audio = audio

    def get_word(self) -> str:
        return self.__word

    def get_part(self) -> str:
        return self.part

    def get_meaning(self) -> str:
        return self.meaning

    def get_example(self) -> str:
        return self.example

    def get_symbol(self) -> str:
        return self.symbol

    def get_audio(self) -> str:
        return self.audio
