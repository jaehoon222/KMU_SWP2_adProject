import LocaleSearcher
from LocaleSearcher import  *

query = "원당로 65"
food = "떡볶이"
x, y, locales = SearchLocale(query, food)
print("x: "+x+" y: "+y)
for locale in locales:
    print("{0}({1},{2})".format(locale.pn,locale.x,locale.y))
