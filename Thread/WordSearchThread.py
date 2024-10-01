import queue
import time

from PySide6.QtCore import QThread, Signal

from Functions.EnglishDictionary.Cambridge import search_word


class WordSearchThread(QThread):
    task_finished = Signal(dict)

    def __init__(self):
        super().__init__()
        self.__queue = queue.Queue()
        self.__running = True

    def add_word(self, word: str):
        print(word)
        self.__queue.put(word)

    def run(self):
        while self.__running:
            word = self.__queue.get()
            if word:
                print(word)
                result = search_word(word)
                print(result)
                if result:
                    self.task_finished.emit(result)
                    time.sleep(0.1)

    def stop(self):
        self.__running = False
        self.__queue.put(None)
