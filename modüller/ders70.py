import re

#re module
str ="Barış KURT 20 yaşındayım. Alanyada yaşıyorum."

# re.findall()
# result = re.findall("R",str)

#re.split()
# result = re.split(" ",str)

#re.sub()
# result = re.sub(" ","-",str)
# result = re.sub("\s","-",str)  \s => boşluk karakteri

# re.search()
# result = re.search("Barış",str)
# result = result.span() #hangi karakterler arasında oldugunu söler
# result = result.start() # ahngi karakterden başaldıgını söler
# result = result.end() hangi karakterle bittgii söler
# result = result.group() # bulduğuyu ifadeyi ekrana yazar
# result = result.string # nerde arandıgı yazar

# regular expression
"""
[] - Köşeli parantezler arasına yazılan bütün karakterler aranır
    [abc] => a        : 1 match
             ac       : 2 match
             python   : no matches

    [a-e]  => [abcde]
    [1-5]  => [12345]
    [0-39] => [01239]
    [^abc] => abc dışındaki karakterler
    [^0-9] => rakam olmayan karakterler
"""
result = re.findall("[abc]",str)
result = re.findall("[Barış]",str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[1-5]",str)
result = re.findall("[^abc]",str)
result = re.findall("[^0-9]",str)

"""
    . - herhangi bir tek karakteri belirtir

        .. => a     : no match
              ab    : 1 match
              abc   : 1 match
              abcd  : 2 matches
"""
result = re.findall("...",str)
result = re.findall("Ba...",str)

"""
    ^ - Belirtilen string karakterle mi başlıyor

    ^a => a   : 1 match
          abc : 1 match
          bac : no match
"""
result = re.findall("^B",str)

"""
    $ - Belirtilen string karakterle mi bitiyor

    a$ => a      : 1 match
          lamba  : 1 match
          Python : no match
"""
result = re.findall("T$",str)
result = re.findall("ş$",str)
result = re.findall("t$",str)

"""
    * - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder

    ma*n => mn    : 1 match
            man   : 1 match
            maaan : 1 match
            main  : no match (a'nın arkasına n gelmiyor)
"""
result = re.findall("Ba*rış",str)

"""
    + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder

    ma+n => mn    : no match
            man   : 1 match
            maaan : 1 match
            main  : no match (a'nın arkasına n gelmiyor)
"""
result = re.findall("Ba+rış",str)

"""
    ? - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder

    ma?n => mn    : no match
            man   : 1 match
            maaan : 1 match
            main  : no match (a'nın arkasına n gelmiyor)
"""
result = re.findall("Ba?rış",str)

"""
    {} - Karakter sayısını kontrol eder

        a1{2}      => a karakterinin arkasına 1 karakterini 2 kez tekrarlamalı
        a1{2,3}    => a karakterinin arkasına 1 karakterini en az 2 en fazla 3 kez tekrarlamalı
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar
"""
result = re.findall("a{1}",str)
result = re.findall("[0-9]{2}",str)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir

        a|b => a yada b

        cde    => no match
        ade    => 1 match
        acdbea => 3 match
"""

"""
    () - gruplamak  için kullanılır

        (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir
"""

"""
    \ - Özel karakterleri aramanızı sağlar
        \$a => $ karakterinin arkasına a karakterini arar. Yani $ regular exp. engine tarafından yorumlanmaz

    \A - Belirtilen karakter string in başında mı?
        \Athe => the string in başındamı?

    \Z - Belirtilen karakter string in sonunda mı?
        the\Z => the string in sonunda mı? 

    \b - Belirtilen karakter kelimenin başında yada sonunda mı?
        \bthe => the kelimenin başındamı
        the\b => the kelimenin sonundamı
    
    \B - Belirtilen karakter kelimenin başında yada sonunda değil mı?
        \Bthe => the kelimenin başında degil mi
        the\B => the kelimenin sonunda degil mi

    \d - [0-9] ile aynı anlama gelir yani rakamları arar
        \d => 12abc34
    
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar
        \D => 1ab44_50

    \s - Boşluk karakterlerini arar
    \S - Boşluk karakterlerinin dışındakiler
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri
    \W - \w nin tam tersi
"""
result = re.findall("\ABarış",str)
result = re.findall("yaşıyorum.\Z",str)
print(result)