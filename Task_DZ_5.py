
# 1. Напишите программу, удаляющую из текста все слова содержащие "абв",
# которые регисторонезависимо.
# Используйте знания с последней лекции.
# Выполните её в виде функции.

def del_абв(text):
    new_text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(new_text)


source_text = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
no_case_text = source_text.lower()
print(no_case_text)
print(del_абв(no_case_text))


# 2. Вы когда-нибудь играли в игру "Крестики нолики"?
# Попробуйте создать её, причём чтобы сыграть в неё можно было в одиночку.

playing_field = list(range(1, 10))

def draw_field(playing_field):
    print('-' * 13)
    for i in range(3):
        print('|', playing_field[0+i*3], '|', playing_field[1+i*3], '|', playing_field[2+i*3], '|')
        print('-' * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input('Ваш ход  ' + player_token+' ? ')
        try:
            player_answer = int(player_answer)
        except:
            print('Некорректный ввод. Повторите ввод')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(playing_field[player_answer-1])not in "XO"):
                playing_field[player_answer-1] = player_token
                valid = True
            else:
                print('Данная клетка уже занята')
        else:
            print('Некорректный ввод. Введите число от 1 до 9.')

def check_win(playing_field):
    win_coord = ((0, 1, 2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if playing_field[each[0]] == playing_field[each[1]] == playing_field[each[2]]:
            return playing_field[each[0]]
    return False

def main(playing_field):
    counter = 0
    win = False
    while not win:
        draw_field(playing_field)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(playing_field)
            if tmp:
                print(tmp, 'УРА  Вы ПОБЕДИТЕЛЬ!!!')
                win = True
                break
        if counter == 9:
            print('Победиал дружба')
            break
    draw_field(playing_field)

main(playing_field)


# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. 
# В общем, короче говоря, шел я, кажется, в магазин. 
# Ну,эээ, в общем, было лето, кажется. 
# Как бы тепло. Солнечно, короче. 
# Иду я, иду, в общем, по улице, а тут, короче, яма. 
# Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. 
# Ясен пень, в магазин. 
# В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. 
# Кстати, иду я по улице, иду, а тут, короче, яма. 
# Ну, я в нее упал, в общем. Вышел из подъезда, короче. 
# Лето на дворе, ясен пень. Птицы поют, короче, солнечно. 
# В общем, в магазин мне надо. Что-то явно не так, короче. 
# «Рекурсия», - подумал я. 
# Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».

# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. 
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.


text = '''Ну, вышел я, короче, из подъезда. 
В общем, короче говоря, шел я, кажется, в магазин. 
Ну,эээ, в общем, было лето, кажется. 
Как бы тепло. Солнечно, короче. 
Иду я, иду, в общем, по улице, а тут, короче, яма. 
Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. 
Ясен пень, в магазин. 
В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. 
Кстати, иду я по улице, иду, а тут, короче, яма. 
Ну, я в нее упал, в общем. Вышел из подъезда, короче. 
Лето на дворе, ясен пень. Птицы поют, короче, солнечно. 
В общем, в магазин мне надо. Что-то явно не так, короче. 
«Рекурсия», - подумал я. 
Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил.'''

trash_words = ['ну', 'В общем', 'короче говоря', 'кажется', 'иду я','ээ','_э' ,'короче,', ',кажется',
 'в общем', 'ясен пень', 'как бы', 'кстати', 'короче', '... ,', '….','…', '...',', ,', ', _', '_,' ]

for word in trash_words:
    text = text.lower().replace(word, '_')

text = text.replace('я,','я').replace('_','').replace('  ',' ').split('.')

List_sent = []
for sent in text:
  sent = sent.strip()
  if not sent:
    continue
  sent = sent.capitalize()
  List_sent.append(sent)
my_text = '. '.join(List_sent)

my_text = my_text  + '.'

print(my_text)