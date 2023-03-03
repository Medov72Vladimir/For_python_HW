#   *Задача 20: 
#   В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
#   В случае с английским алфавитом очки распределяются так:
#   A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
#   F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
#   А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
#   Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
#   Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, 
#   которая вычисляет стоимость введенного пользователем слова. Будем считать, что 
#   на вход подается только одно слово, которое содержит либо только английские, 
#   либо только русские буквы.
#   *Пример:*
#   ноутбук
#   12

word = input().upper()
ENGe = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
ENG2 = dict.fromkeys(['D','G'],2)
ENG3 = dict.fromkeys(['B','C','M','P'],3)
ENG4 = dict.fromkeys(['F','H','W','V','Y'],4)
ENGe.update(ENG2)
ENGe.update(ENG3)
ENGe.update(ENG4)
ENGe['K'] = 5
ENGe['J'] = 8
ENGe['X'] = 8
ENGe['Q'] = 10
ENGe['Z'] = 10
RUSr = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
RUS2 = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
RUS3 = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
RUS5 = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
RUS8 = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
RUS10 = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
RUSr.update(RUS2)
RUSr.update(RUS3)
RUSr.update(RUS5)
RUSr.update(RUS8)
RUSr.update(RUS10)
RUSr['Й'] = 4
RUSr['Ы'] = 4
sum = 0
if 65 <= ord(word[0]) <= 90:
    for i in word:
        sum += ENGe[i]
    print(sum)
else:
    for i in word:
        sum += RUSr[i]
    print(sum)