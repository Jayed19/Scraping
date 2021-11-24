#pip install pip install googletrans==3.1.0a0
from googletrans import Translator
translator = Translator()

test=translator.translate('안녕하세요.', dest='ja')
print(test.text)
