from googletrans import Translator

sentence = input("책을 읽으며 인상 깊었던 구절을 적어주세요:  ")
translator = Translator()
original = translator.detect(sentence)
en_result = translator.translate(sentence, dest ='en')
fr_result = translator.translate(sentence, dest = 'fr')

print("============번역 결과===========")
print("입력어-", original.lang, ":", en_result.origin)
print("번역어1-", en_result.dest, ":", en_result.text)
print("번역어2-", fr_result.dest, ":", fr_result.text)
print("================================")