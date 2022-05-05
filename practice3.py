from googletrans import Translator

tran = Translator()
src = input("책을 읽으며 인상 깊었던 구절을 적어주세요 : ")
dt = tran.detect(src)
r1 = tran.translate(src, "en")
r2 = tran.translate(src, "ja")

print("================ 번역 결과 =================")
print("입력어 -", dt.lang, ":", src)
print("번역어1 -", r1.dest, ":", r1.text)
print("번역어2 -", r2.dest, ":", r2.text)
print("===========================================")