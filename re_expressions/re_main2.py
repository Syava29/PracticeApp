import re

srt_input = r'Иван Иванович! Нужен ответ на письмо от ivanoff@ivan-chai.ru. Не забудьте поставить в копию sergeo-lupin@mail.ru - это важно. письма на почту r.e.egor@yandex.domen1.domen2.ru ношу словно я роман\
 с продолженьем пишу'

print(re.findall(r'\S+@\S+', srt_input))