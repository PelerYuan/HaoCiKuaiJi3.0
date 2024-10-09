import logging

import requests
from bs4 import BeautifulSoup

from DataStract.WordData import WordData

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


def list_to_str(l):
    result = ''
    for i in l:
        result += str(i) + '\n'
    return result


def search_word(word: str):
    base_url = 'https://dictionary.cambridge.org/dictionary/english-chinese-simplified/'
    # 发送GET请求
    response = requests.get(base_url + word, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 获取中文释义
        target_class = ['trans', 'dtrans', 'dtrans-se', 'break-cj']
        # 查找所有<span>元素
        all_spans = soup.find_all("span")
        # 使用列表推导式筛选具有目标类名的<span>元素
        definitions = [span for span in all_spans if span.get("class") == target_class]
        chinese_definitions = [definition.get_text() for definition in definitions]
        # 获取例句
        examples = soup.select('.eg.deg')
        example_list_english = [example.get_text() for example in examples]
        t = ['trans', 'dtrans', 'dtrans-se', 'hdb', 'break-cj']
        # 查找所有<span>元素
        all_spans = soup.find_all("span")
        # 使用列表推导式筛选具有目标类名的<span>元素
        definitions = [span for span in all_spans if span.get("class") == t]
        example_list_chinese = [definition.get_text() for definition in definitions]
        example_list = [item for pair in zip(example_list_english, example_list_chinese) for item in pair]
        # 获取词性
        parts_of_speech = soup.select('.pos.dpos')
        parts_of_speech_list = [pos.get_text() for pos in parts_of_speech]
        # 获取音标
        phonetic_symbol = '/' + soup.select('.ipa.dipa.lpr-2.lpl-1')[0].get_text() + '/'
        # 获取音频文件链接
        audio_element = soup.find('source', {'type': 'audio/mpeg'})
        audio_link = audio_element['src'] if audio_element else None

        save_audio(word, 'https://dictionary.cambridge.org' + audio_link)

        return WordData(
            word=word,
            part=list_to_str(parts_of_speech_list),
            meaning=list_to_str(chinese_definitions),
            example=list_to_str(example_list),
            symbol=phonetic_symbol,
            audio='https://dictionary.cambridge.org' + audio_link
        )

    else:
        logging.log(logging.ERROR, f'Error searching word: {word}, status code: {response.status_code}')


def save_audio(word: str, url: str):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(f'./data/audio/{word}.mp3', 'wb') as f:
            f.write(response.content)
