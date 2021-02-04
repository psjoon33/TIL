from googletrans import Translator

translator = Translator()

result = translator.translate('안녕하세요.', dest="ko")

a = result.text
print(a)
# print(result.text)

# print(translator.detect('이 문장은 한글로 쓰여졌습니다.').lang)


