"""Шифр Виженера — классический шифр, изначально разработанный итальянским криптографом 
Джованни Баттиста Беллазо и опубликованный в 1553 году. Он назван в честь французского криптографа 
Блеза де Виженера, который разработал более надёжный автоключ 
(шифр, в котором сообщение текста является ключом).

Шифр прост в понимании и применении, но выдержал три столетия попыток его взломать, 
за что получил прозвище «нерасшифруемый шифр».

Из Википедии:

Шифр Виженера — это метод шифрования алфавитного текста с помощью серии различных шифров Цезаря, 
основанных на буквах ключевого слова. Это простая форма полиалфавитной замены.

. . .

В шифре Цезаря каждая буква алфавита сдвинута на некоторое количество мест; например, 
в шифре Цезаря shift 3A, стал бы D, B стал бы E, Y стал бы стал B и так далее. 
Шифр Виженера состоит из нескольких последовательных шифров Цезаря с разными значениями сдвига.

Предположим, что ключ повторяется по всей длине текста, символ за символом. Обратите внимание, 
что в некоторых реализациях ключ повторяется по символам только в том случае, 
если они являются частью алфавита.Здесь это не так.

Сдвиг получается путём применения сдвига Цезаря к символу с соответствующим индексом ключа в алфавите.

Визуальное представление:

"my secret code i want to secure"  // message
"passwordpasswordpasswordpasswor"  // key
Напишите класс, который при наличии ключа и алфавита можно использовать для кодирования и 
декодирования шифра.

Пример
var alphabet = 'abcdefghijklmnopqrstuvwxyz';
var key = 'password';

// creates a cipher helper with each letter substituted
// by the corresponding character in the key
var c = new VigenèreCipher(key, alphabet);

c.encode('codewars'); // returns 'rovwsoiv'
c.decode('laxxhsj');  // returns 'waffles'
Любой символ, не входящий в алфавит, должен оставаться без изменений. 
Например (продолжая предыдущий пример):

c.encode('CODEWARS'); // returns 'CODEWARS'
ПРИМЕЧАНИЕ ДЛЯ PYTHON

Реализация Python требует преобразования в Юникод, т.е. input.decode('utf-8'), output.encode('utf-8')

При попытке вывести строки в кодировке utf-8 без предварительного кодирования 
(как указано выше) возникнет ошибка:

UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-3: ordinal not in range(128)"""

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text):
        self.text = text

        keyi = 0
        n = len(self.alphabet)
        keyl = len(self.text) / len(self.key)
        newkey = list()

        for a in self.text:
            newkey.append(self.key[keyi])
            keyi = (keyi + 1) % len(self.key)

        res1 = []
        for i in range(len(self.text)):
            for j in range(len(self.alphabet)):
                if self.text[i] == self.alphabet[j]:
                    res1.append(j)

        res2 = []
        for ik in range(len(newkey)):
            for jk in range(len(self.alphabet)):
                if newkey[ik] == self.alphabet[jk]:
                    res2.append(jk)

        print(res1, "\n", res2)
        print(f"{n} || {self.text} || {newkey}")

    
    def decode(self, text):
        pass

conf = VigenereCipher("key", 'abcdefghijklmnopqrstuvwxyz')
e = conf.encode("hello")
d = conf.decode(e)


# "codewars"
# "abcdefghijklmnopqrstuvwxyz"
# "password"