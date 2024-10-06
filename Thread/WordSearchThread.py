import queue
import time

from PySide6.QtCore import QThread, Signal

from DataStract.WordGroup import WordGroup
from Functions.EnglishDictionary.Cambridge import search_word
from Functions.WordGroup import save_word_group


class WordSearchThread(QThread):
    task_finished = Signal(dict, WordGroup)

    def __init__(self):
        super().__init__()
        self.__queue = queue.Queue()
        self.__running = True

    def add_word(self, word: str, word_group: WordGroup):
        self.__queue.put([word, word_group])

    def run(self):
        while self.__running:
            word, word_group = self.__queue.get()
            if word:
                result = search_word(word)
                if result:
                    word_group.update_word(**result)
                    save_word_group(word_group)
                    print('aaaaaa')
                    self.task_finished.emit(result, word_group)
                    time.sleep(0.1)

    def stop(self):
        self.__running = False
        self.__queue.put([None, None])
