from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler
import random
from os import getenv
from sys import exit

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

updater = Updater(token=bot_token)
dispatcher = updater.dispatcher
id_list = list(random.sample(range(50), 50))
ans = []
q_asked = []

def start(update, context):
    update.message.reply_text(text="Добро пожаловать! Я бот Сеги. Пожалуйста, выберите один из приведенных ниже вариантов:")
    menu(update, context)

def Segiban(update, context):
    query = update.callback_query
    text = "Сёгибан\nВ сёги доска называется сёгибан и представляет собой прямоугольник с нанесённой на него сеткой 9х9 клеток. Все клетки одинакового размера и цвета. Также на доске вы можете заметить четыре маленькие точки, которые помогают разделить доску на девять квадратов 3х3, это облегчает восприятие игрового поля. Сёгибан как правило изготавливается из древесины торреи орехоносной."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='rules_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass

def Komadai(update, context):
    query = update.callback_query
    text = "Комадай\nКроме сёгибана при игре может использоваться комадай — подставка для взятых в плен фигур противника. Комадай используется для повышения удобства во время игры. Располагается справа от сёгибана ближе к игроку."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='rules_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass

def Transformations(update, context):
    query = update.callback_query
    text = "Превращения\nВизуально на сёгибане можно выделить З равных по размеру области:\nлагерь противника\nнейтральная территория\nваш собственный лагерь\n\nПри попадании в лагерь противника все фигуры кроме короля и золотого генерала можно превратить в их улучшенные версии. Переворот фигур происходит по желанию игроков, но есть ряд правил:\nПереворачивать можно фигуры, которые только вошли в зону превращения или уже ходят в ней\nЕсли фигура вышла из зоны превращения и не была перевёрнута, то для превращения ей снова понадобится войти в зону\nФигура сброшенная в лагерь противника может быть превращена при совершении хода\nМладшие фигуры (кэйма, кёся, фухё) обязательно переворачивать при достижении ими последней\nгоризонтали с которой они уже никуда не смогут походить (предпоследней для кейма)\nОднажды перевернувшись фигура уже не возвращается в начальное состояние до тех пор пока её не съедят"
    back_btn = InlineKeyboardButton(text='Назад', callback_data='rules_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass

def Figure(update, context):
    query = update.callback_query
    text = "Фигуры\nВ начале партии фигуры расставляются по свои лагерям.\n Всего в сражении на доске учувствует 40 фигур, по 20 с каждой стороны. На каждую фигуру нанесены иероглифы кандзи обозначающие их имена. Обычно фигуры обозначаются двумя иероглифами, но нередко обозначение сокращают до одного иероглифа. О превращениях фигур поговорим чуть позже. В сёги 8 видов основных фигур и 6 перевёрнутых, которые в итоге дают 10 различных по возможностям фигур. Ниже вы можете узнать о них подробнее:"
    btn1 = InlineKeyboardButton(text='Осё и Гёкусё', callback_data='Ose_and_Hecuse')
    btn2 = InlineKeyboardButton(text='Хися (Летающая колесница)', callback_data='Flying_Chariot')
    btn3 = InlineKeyboardButton(text='Рюю (королевский дракон)', callback_data='Royal_dragon')
    btn4 = InlineKeyboardButton(text='Какугё (слон)', callback_data='Elephant')
    btn5 = InlineKeyboardButton(text='Рюма (лошадиный дракон)', callback_data='Horse_dragon')
    btn6 = InlineKeyboardButton(text='Кинсё (золотой генерал)', callback_data='Golden_general')
    btn7 = InlineKeyboardButton(text='Гинсё (серебряный генерал)', callback_data='Silver_general')
    btn8 = InlineKeyboardButton(text='Нари-Гин (перевёрнутое серебро)', callback_data='Inverted_silver')
    btn9 = InlineKeyboardButton(text='Кэйма (конь)', callback_data='Horse')
    btn10 = InlineKeyboardButton(text='Нари-Кэй (перевёрнутый конь)', callback_data='Inverted_horse')
    btn11 = InlineKeyboardButton(text='Кёся (копьё)', callback_data='Spear')
    btn12 = InlineKeyboardButton(text='Нари-Кё (перевёрнутое копьё)', callback_data='Inverted_spear')
    btn13 = InlineKeyboardButton(text='Фухё (солдат)', callback_data='Soldier')
    btn14 = InlineKeyboardButton(text='Токин (превращённый солдат)', callback_data='Inverted_soldier')
    back_btn = InlineKeyboardButton(text='Назад', callback_data='rules_back')
    markup = InlineKeyboardMarkup([[btn1], [btn2], [btn3], [btn4], [btn5], [btn6], [btn7], [btn8], [btn9], [btn10], [btn11], [btn12], [btn13], [btn14], [back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass

def Ose_and_Hecuse(update, context):
    query = update.callback_query
    text = "Осё и Гёкусё\nКоролевский генерал или Осё — это аналог короля в европейских шахматах. Ходит также, на одну клетку в любом направлении.\nГекусё в переводе с японского — драгоценный генерал. Ходит он также как и осё.\nНа поле обе фигуры ведут себя одинаково. Не переворачиваются. Внешне отличаются лишь одной небольшой чёрточкой справа от иероглифа\nВсё дело в том, что для японцев сёги — это не просто игра. Для них это также в некотором роде ритуал. Осё — фигура для более опытного или старшего по возрасту или титулу игрока. Гёкусё — фигура для младших или менее опытных игроков. Таким образом японцы проявляют уважение.\nТак например, если играют отец и сын, то король осё достанется отцу. Аналогичная ситуация с хозяином дома и его гостями, осё — для хозяина.\nИсключения могут возникнуть при наличии у одного из игроков профессионального разряда."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.ОсёГёкусё.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Flying_Chariot(update, context):
    query = update.callback_query
    text = "Хися (Летающая колесница)\nХися — одна из сильнейших фигур в сёги. Ходит по вертикали и горизонтали на любое число клеток. Точно также, как и шахматная ладья.\nРазмещается над правым конём. При перевороте получает имя рюю."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Хися.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Royal_dragon(update, context):
    query = update.callback_query
    text = "Рюю (королевский дракон)\nПосле переворота король-дракон сохраняет возможность ходить по вертикали и горизонтали на любое количество клеток, а также обретает способность ходить в любую сторону на одну клетку (как король)."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Рюю.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Elephant(update, context):
    query = update.callback_query
    text = "Какугё (слон)\nКакуге наравне с летающей колесницей, считается ещё одной из сильнейших фигур. Ходит какуге аналогично слону в шахматах — на любое число клеток по диагоналям.\nРасполагается над левым конём. При перевороте какугё превращается в рома."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Какугё.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Horse_dragon(update, context):
    query = update.callback_query
    text = "Рюма (лошадиный дракон)\nПосле переворота слон может ходить по диагоналям на любое число клеток, а также в любую сторону на одну клетку."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Рюма.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Golden_general(update, context):
    query = update.callback_query
    text = "Кинсё (золотой генерал)\nСокращённо кинсё также называют просто золото. Золотые генералы — это личные телохранители короля. На доске у каждого игрока по 2 золота. При начальной расстановке фигур они находятся слева и справа от короля.\nКинсё ходит почти также как и король, но не может отступать назад по диагонали.\nТакже как и король, золото не переворачивается. Его обратная сторона пуста."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Кинсё.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Silver_general(update, context):
    query = update.callback_query
    text = "Гинсё (серебряный генерал)\n Сокращённо эту фигуру называют гин или серебро. по рангу серебро чуть слабее золота. Ходит на одну клетку во все стороны, но не ходит назад и по бокам.\nНа доске у каждого игрока по 2 серебряных генерала. Изначально на сёгибане серебро находится сбоку от золота. Превращается в нари-гин."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Гинсё.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Inverted_silver(update, context):
    query = update.callback_query
    text = "Нари-Гин (перевёрнутое серебро)\nПеревёрнутое серебро ходит как золото."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Нари-гин.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Horse(update, context):
    query = update.callback_query
    text = "Кэйма (конь)\n Конь в сёги имеет меньше возможностей, чем его европейски собрат. Кейма может ходить на 2 поля вперёд, а потом направо или налево. Крайне уязвимая фигура. Не может отступать.\nУ каждого игрока по 2 коня. Начальная позиция сбоку от серебряного генерала. Превращается в нари-кей."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Кэйма.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Inverted_horse(update, context):
    query = update.callback_query
    text = "Нари-Кэй (перевёрнутый конь)\nПеревёрнутый конь теряет свои способности и становится золотым генералом, приобретая всю его мощь."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Нари-Кэй.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Spear(update, context):
    query = update.callback_query
    text = "Кёся (копьё)\n При дословном переводе с японского название этой фигуры «пахнущая колесница», но также у неё есть кличка — яро. Яра с японского это стрелка или копьё. Чаще эту фигуру называют стрелка, но копьё мне нравится больше. Ведь эта фигура подобно копью пронизывает все клетки перед собой.\nПолезные, но крайне уязвимые фигуры. Не могут отступать до переворота.\nВ начале игры у каждого игрока по 2 копья. Их стартовые позиции левый и правый край первой горизонтали. Превращается в нари-кё"
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Кёся.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Inverted_spear(update, context):
    query = update.callback_query
    text = "Нари-Кё (перевёрнутое копьё)\nПосле переворота нари-кё теряет возможности обычного копья и ходит в точности как золотой генерал."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Нари-кё.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Soldier(update, context):
    query = update.callback_query
    text = "Фухё (солдат)\nПешки самые слабая фигура на сёгибане, но не стоит их недооценивать. Умелый командир способен превратить их в грозную силу и нанести поражение противнику.\nФухё самые многочисленные фигуры на сёгибане. Всего у каждого игрока по 9 пешек. Располагаются они все на третьей горизонтали. Превращаются в токин."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Фухё.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass
def Inverted_soldier(update, context):
    query = update.callback_query
    text = "Токин (превращённый солдат) Попав во вражеский лагерь, пешка может стать золотым генералом. Если переводить дословно токин= «как золото» и ходит эта фигура также как золото."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='figure_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    with open('img/rules/О.Токин.png', 'rb') as photo:
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=markup)
    pass

def Basic_actions(update, context):
    query = update.callback_query
    text = "Основные моменты шахмат сёги:"
    btn1 = InlineKeyboardButton(text='Сбросы', callback_data='Resets')
    btn2 = InlineKeyboardButton(text='Запрет на сброс', callback_data='Ban_on_resetting')
    btn3 = InlineKeyboardButton(text='Ничья', callback_data='Draw')
    btn4 = InlineKeyboardButton(text='Подсчёт очков', callback_data='Scoring_points')
    back_btn = InlineKeyboardButton(text='Назад', callback_data='rules_back')
    markup = InlineKeyboardMarkup([[btn1], [btn2], [btn3], [btn4], [back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass

def Resets(update, context):
    query = update.callback_query
    text = "Сбросы\nВ сёги возможно повторное использование захваченных фигур противника. При сбросе фигура выставляется в любую пустую клетку на сёгибане.\nПравила сброса\nНа сброс тратится один ход\nСброс занимает целый ход. Одновременно со сбросом нельзя съесть фигуру противника или выполнить превращение сброшенной фигуры\nПри сбросе фигура имеет свой изначальный статус (не превращена)\nСо следующего после сброса хода фигура может выполнять превращение и захватывать фигуры противника"
    back_btn = InlineKeyboardButton(text='Назад', callback_data='basic_actions_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass
def Ban_on_resetting(update, context):
    query = update.callback_query
    text = "Запрет на сброс\nСброс фигур запрещается в следующих случаях:\nЗапрещён сброс фигур на клетки, с которых они уже не смогут совершать ходы (последняя горизонталь для фухё и кёся и предпоследняя для кейма)\nЗапрещён сброс пешки на вертикаль на которой уже находится ваша пешка (наличие токина на вертикали не запрещает сброса)\nЗапрещён сброс пешки, ставящий мат (сброс пешки на короля, который не может съесть её или уйти от удара)"
    back_btn = InlineKeyboardButton(text='Назад', callback_data='basic_actions_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass
def Draw(update, context):
    query = update.callback_query
    text = "Ничья\nВ сёги ничья довольно редкое явление, однако иногда оно имеет место быть. Ничью можно объявить в двух случаях:\nСэнничитэ\nОдна и та же позиция возникает четыре раза. В этом случае партию переигрывают, при этом сентэ и готэ меняются местами.\nДзисёги\nСитуация, при которой ни один из игроков не может поставить мат другому. Как правило такое случается из-за нюгёку — один из игроков строит крепость в лагере другого.\nРезультат игры в случае дзисёги определяется по очкам.\n\nЕсли у каждого игрока есть минимум 24 очка, то объявляется абсолютная ничья\nЕсли у кого-то из игроков меньше 24 очков, то его объявляют проигравшим\n\nПатовых ситуаций и ничьих из-за них в сёги не бывает."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='basic_actions_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass
def Scoring_points(update, context):
    query = update.callback_query
    text = "Подсчёт очков\nПодсчитываются все фигуры игрока на поле и на его комадай (в руке), кроме короля.\nЛадья и слон оцениваются в 5 очков, а все остальные — очко."
    back_btn = InlineKeyboardButton(text='Назад', callback_data='basic_actions_back')
    markup = InlineKeyboardMarkup([[back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass

def rules(update, context):
    query = update.callback_query
    text = "Основные правила шахмат сёги:\nСёги — это игра для двух игроков, которые сражаются друг с другом на доске. Как и в классических европейских шахматах, игроки поочерёдно, шаг за шагом, передвигают фигуры. Процесс совершения ходов до конца игры называется «той-кеку» (игра). В сёги побеждает тот, кто первым съест вражеского короля, то есть поставит ему мат.\n В сёги в отличии от европейских шахмат нет чёрных и белых фигур — все фигуры одного цвета. Их принадлежность игроку определяется по направлению их острой части. Противоборствующие стороны лишь условно делят на чёрные — готэ (ходящие первыми) и белые сэнтэ — (ходящие позже). Основным отличием европейских шахмат от сёги является возможность возврата ранее съеденных фигур противника обратно на поле, но уже на своей стороне. Именно это, порой, делает партии сёги невероятно сложными и интересными."
    btn1 = InlineKeyboardButton(text='Сёгибан', callback_data='Segiban')
    btn2 = InlineKeyboardButton(text='Комадай', callback_data='Komadai')
    btn3 = InlineKeyboardButton(text='Превращения', callback_data='Transformations')
    btn4 = InlineKeyboardButton(text='Фигуры', callback_data='Figure')
    btn5 = InlineKeyboardButton(text='Основные моменты', callback_data='Basic_actions')
    back_btn = InlineKeyboardButton(text='Вернуться в меню', callback_data='back')
    markup = InlineKeyboardMarkup([[btn1], [btn2], [btn3], [btn4], [btn5], [back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass

def test(update, context):
    start_quiz(update, context)
    pass

def back(update, context):
    query = update.callback_query
    button1 = InlineKeyboardButton(text='Обучение', callback_data='rules')
    button2 = InlineKeyboardButton(text='Тестирование', callback_data='test')
    menu_message = "Выберите, что вы хотите сделать:"
    menu_markup = InlineKeyboardMarkup([[button1], [button2]])
    context.bot.send_message(chat_id=query.message.chat.id, text=menu_message, reply_markup=menu_markup)
    pass

def rules_back(update, context):
    query = update.callback_query
    text = "Основные правила шахмат сёги:\nСёги — это игра для двух игроков, которые сражаются друг с другом на доске. Как и в классических европейских шахматах, игроки поочерёдно, шаг за шагом, передвигают фигуры. Процесс совершения ходов до конца игры называется «той-кеку» (игра). В сёги побеждает тот, кто первым съест вражеского короля, то есть поставит ему мат.\n В сёги в отличии от европейских шахмат нет чёрных и белых фигур — все фигуры одного цвета. Их принадлежность игроку определяется по направлению их острой части. Противоборствующие стороны лишь условно делят на чёрные — готэ (ходящие первыми) и белые сэнтэ — (ходящие позже). Основным отличием европейских шахмат от сёги является возможность возврата ранее съеденных фигур противника обратно на поле, но уже на своей стороне. Именно это, порой, делает партии сёги невероятно сложными и интересными."
    btn1 = InlineKeyboardButton(text='Сёгибан', callback_data='Segiban')
    btn2 = InlineKeyboardButton(text='Комадай', callback_data='Komadai')
    btn3 = InlineKeyboardButton(text='Превращения', callback_data='Transformations')
    btn4 = InlineKeyboardButton(text='Фигуры', callback_data='Figure')
    btn5 = InlineKeyboardButton(text='Основные действия', callback_data='Basic_actions')
    back_btn = InlineKeyboardButton(text='Вернуться в меню', callback_data='back')
    markup = InlineKeyboardMarkup([[btn1], [btn2], [btn3], [btn4], [btn5], [back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass

def figure_back(update, context):
    query = update.callback_query
    text = "Фигуры\nВ начале партии фигуры расставляются по свои лагерям.\n Всего в сражении на доске учувствует 40 фигур, по 20 с каждой стороны. На каждую фигуру нанесены иероглифы кандзи обозначающие их имена. Обычно фигуры обозначаются двумя иероглифами, но нередко обозначение сокращают до одного иероглифа. О превращениях фигур поговорим чуть позже. В сёги 8 видов основных фигур и 6 перевёрнутых, которые в итоге дают 10 различных по возможностям фигур. Ниже вы можете узнать о них подробнее:"
    btn1 = InlineKeyboardButton(text='Осё и Гёкусё', callback_data='Ose_and_Hecuse')
    btn2 = InlineKeyboardButton(text='Хися (Летающая колесница)', callback_data='Flying_Chariot')
    btn3 = InlineKeyboardButton(text='Рюю (королевский дракон)', callback_data='Royal_dragon')
    btn4 = InlineKeyboardButton(text='Какугё (слон)', callback_data='Elephant')
    btn5 = InlineKeyboardButton(text='Рюма (лошадиный дракон)', callback_data='Horse_dragon')
    btn6 = InlineKeyboardButton(text='Кинсё (золотой генерал)', callback_data='Golden_general')
    btn7 = InlineKeyboardButton(text='Гинсё (серебряный генерал)', callback_data='Silver_general')
    btn8 = InlineKeyboardButton(text='Нари-Гин (перевёрнутое серебро)', callback_data='Inverted_silver')
    btn9 = InlineKeyboardButton(text='Кэйма (конь)', callback_data='Horse')
    btn10 = InlineKeyboardButton(text='Нари-Кэй (перевёрнутый конь)', callback_data='Inverted_horse')
    btn11 = InlineKeyboardButton(text='Кёся (копьё)', callback_data='Spear')
    btn12 = InlineKeyboardButton(text='Нари-Кё (перевёрнутое копьё)', callback_data='Inverted_spear')
    btn13 = InlineKeyboardButton(text='Фухё (солдат)', callback_data='Soldier')
    btn14 = InlineKeyboardButton(text='Токин (превращённый солдат)', callback_data='Inverted_soldier')
    back_btn = InlineKeyboardButton(text='Назад', callback_data='back_rules')
    markup = InlineKeyboardMarkup([[btn1], [btn2], [btn3], [btn4], [btn5], [btn6], [btn7], [btn8], [btn9], [btn10], [btn11], [btn12], [btn13], [btn14], [back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass

def basic_actions_back(update, context):
    query = update.callback_query
    text = "Основные моменты шахмат сёги:"
    btn1 = InlineKeyboardButton(text='Сбросы', callback_data='Resets')
    btn2 = InlineKeyboardButton(text='Запрет на сброс', callback_data='Ban_on_resetting')
    btn3 = InlineKeyboardButton(text='Ничья', callback_data='Draw')
    btn4 = InlineKeyboardButton(text='Подсчёт очков', callback_data='Scoring_points')
    back_btn = InlineKeyboardButton(text='Назад', callback_data='back_rules')
    markup = InlineKeyboardMarkup([[btn1], [btn2], [btn3], [btn4], [back_btn]])
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)
    pass

def menu(update, context):
    button1 = InlineKeyboardButton(text='Обучение', callback_data='rules')
    button2 = InlineKeyboardButton(text='Тестирование', callback_data='test')
    menu_message = "Выберите, что вы хотите сделать:"
    menu_markup = InlineKeyboardMarkup([[button1], [button2]])
    update.message.reply_text(text=menu_message, reply_markup=menu_markup)

quiz = [
    {
        "question": "Как называется фигура, которая перемещается на любое количество свободных клеток по горизонтали и вертикали?",
        "options": ["Ладья", "Король", "Королевский генерал", "Конь"],
        "img": "",
        "answer": 0
    },
    {
        "question": "Как называется фигура, которая перемещается на одну клетку по диагонали?",
        "options": ["Король", "Слон", "Солдат", "Королевский генерал"],
        "img": "",
        "answer": 1
    },
    {
        "question": "Как называется фигура, которая перемещается на две клетки вперед на первом ходу, а затем на одну клетку вперед на последующих ходах?",
        "options": ["Конь", "Слон", "Солдат", "Ладья"],
        "img": "",
        "answer": 3
    },
    {
        "question": "Как называется начальное расположение фигур в игре Сёги?",
        "options": ["Гюсю-мейчу", "Хися-дзэн", "Фурин-кадзэ ", "Кинг-тен"],
        "img": "",
        "answer": 2
    },
    {
        "question": "Как называется фигура, которая перемещается на одну клетку в любом направлении, кроме назад?",
        "options": ["Кинг", "Какугё", "Хися", "Кьоша"],
        "img": "",
        "answer": 1
    },
    {
        "question": "Какой цвет начинает игру первым?",
        "options": ["Белый", "Красный", "Чёрный", "Синий"],
        "img": "",
        "answer": 0
    },
    {
        "question": "Как называется правило, запрещающее игроку совершать ход, который приведет к захвату его же генерала?",
        "options": ["Правило \"самоубийства\"", "Правило \"перемещения\"", "Правило \"просмотра\"", "Правило \"перемены\""],
        "img": "",
        "answer": 0
    },
    {
        "question": "Какое правило позволяет игроку поставить на доску любую фигуру, которую он захватил ранее, кроме короля?",
        "options": ["Правило \"самоубийства\"", "Правило \"просмотра\"", "Правило \"перемещения\"", "Правило \"перемены\""],
        "img": "",
        "answer":3
    },
    {
        "question": "Как называется фигура, которая может двигаться на любое количество клеток только по диагонали?",
        "options": ["Король", "Королевский генерал", "Слон", "Ладья"],
        "img": "",
        "answer":2
    },
    {
        "question": "Как называется фигура, которая перемещается на две клетки вперед по вертикали?",
        "options": ["Ладья", "Конь", "Королевский генерал", "Солдат"],
        "img": "",
        "answer":1
    },
    {
        "question": "Какой фигурой нельзя ходить по диагонали?",
        "options": ["Солдат", "Ладья", "Конь", "Слон"],
        "img": "",
        "answer":1
    },
    {
        "question": "Какой фигурой можно ходить в направлении, противоположном стороне поля?",
        "options": ["Конь", "Слон", "Королевский генерал", "Ладья"],
        "img": "",
        "answer": 2
    },
    {
        "question": "Сколько фигур у каждого игрока в начале игры?",
        "options": ["15", "18", "17", "20"],
        "img": "",
        "answer": 3
    },
    {
        "question": "Как называется правило, запрещающее игроку совершать ход, который приведет к повторению позиции на доске три раза?",
        "options": ["Правило \"тройного повторения\"", "Правило \"перемещения\"", "Правило \"просмотра\"", "Правило \"перемены\""],
        "img": "",
        "answer":0
    },
    {
        "question": "Как называется фигура, которая перемещается на одну клетку вперед или назад?",
        "options": ["Солдат", "Слон", "Конь", "Ладья"],
        "img": "",
        "answer":0
    },
    {
        "question": "Какой фигурой нельзя ходить по вертикали?",
        "options": ["Ладья", "Слон", "Королевский генерал", "Конь"],
        "img": "",
        "answer":1
    },
    {
        "question": "Какой игрок выигрывает в Сёги, если удалось захватить генерала противника?",
        "options": ["У которого захватили", "Никто", "Который захватил", "Такое невозможно"],
        "img": "",
        "answer":2
    },
    {
        "question": "Можно ли передвигать солдата назад, если он уже перешел на сторону противника?",
        "options": ["Да", "Иногда", "Нет", "Не знаю"],
        "img": "",
        "answer": 2
    },
    {
        "question": "Какой фигурой нельзя ходить по диагонали?",
        "options": ["Слон", "Конь", "Королевский генерал", "Ладья"],
        "img": "",
        "answer": 1
    },
    {
        "question": "Сколько фигур можно \"съесть\" у противника в одном ходу?",
        "options": ["Две", "Три", "Четыре", "Одну"],
        "img": "",
        "answer":3
    },
    {
        "question": "Какой фигурой можно ходить только по горизонтали и вертикали?",
        "options": ["Ладья", "Слон", " Конь", "Солдат"],
        "img": "",
        "answer":0
    },
    {
        "question": "Какой игрок выигрывает в Сёги, если удалось поставить шах королю противника, но его невозможно захватить на следующем ходу?",
        "options": ["Такое не возможно", "Ничья", "Тот кто поставил шах", "Никто, игра продолжается"],
        "img": "",
        "answer":3
    },
    {
        "question": "Как называется правило, согласно которому при смене хода игрок должен назвать фигуру, которой он сделал свой предыдущий ход?",
        "options": ["Правило \"хождения\"", "Правило \"отчетности\"", "Правило \"называния\"", "Правило \"передачи\""],
        "img": "",
        "answer":2
    },
    {
        "question": "Можно ли перемещать генерала на поле, где он будет находиться под боем соперника?",
        "options": ["Да", "Нет", "Иногда", "Не знаю"],
        "img": "",
        "answer": 1
    },
    {
        "question": "Какой фигурой можно ходить на несколько клеток за один ход?",
        "options": ["Солдатом", "Ладьей", "Конем", "Слоном"],
        "img": "",
        "answer": 2
    },
    {
        "question": "Как называется специальный ход, который делает солдат, достигнув противоположного конца доски?",
        "options": ["Преображение", "Превращение", "Преобразование", "Перемена"],
        "img": "",
        "answer":1
    },
    {
        "question": "Какой фигурой нельзя перепрыгивать?",
        "options": ["Солдатом", "Генералом", "Ладьей", "Конем"],
        "img": "",
        "answer":0
    },
    {
        "question": "Какой игрок выигрывает в Сёги, если удалось захватить все фигуры противника, кроме короля?",
        "options": ["Тот который захватил", "Ничья", "Такое невозможно", "У которого захватили"],
        "img": "",
        "answer":0
    },
    {
        "question": "Какой размер поля в Сёги?",
        "options": ["6x6", "8x8", "9x9", "7x7"],
        "img": "",
        "answer":2
    },
    {
        "question": "Какая фигура в Сёги может двигаться только на одну клетку вперед, но на противоположной стороне поля может стать золотой фигурой и иметь больше возможностей движения?",
        "options": ["Ладья", "Пешка", "Конь", "Серебрянный генерал"],
        "img": "",
        "answer": 1
    },
    {
        "question": "Что это за фигура?",
        "options": ["Ладья", "Пешка", "Конь", "Серебрянный генерал"],
        "img": "img/test/Т.Гинсё.png",
        "answer":4
    },
    {
        "question": "Что за фигура?",
        "options": ["Слон", "Королевский генерал", "Пешка", "Перевернутое копье"],
        "img": "img/test/Т.Гёкусё.png",
        "answer":1
    },
    {
        "question": "Это за фигура...",
        "options": ["Ладья", "Копье", "Слон", "Золотой генерал"],
        "img": "img/test/Т.Какугё.png",
        "answer":2
    },
    {
        "question": "Какая это фигура?",
        "options": ["Перевернутое копье", "Серебрянный генерал", "Королевский дракон", "Золотой генерал"],
        "img": "img/test/Т.Кинсё.png",
        "answer":3
    },
    {
        "question": "Как называеться эта фигура?",
        "options": ["Ладья", "Пешка", "Конь", "Летающая колесница"],
        "img": "img/test/Т.Кэйма.png",
        "answer":3
    },
{
        "question": "Какое название у этой фигуры?",
        "options": ["Копье", "Перевернутое копье", "Перевернутый солдат", "Серебрянный генерал"],
        "img": "img/test/Т.Кёся.png",
        "answer":0
    },
    {
        "question": "Что обознатает иероглиф на этой фигуре?",
        "options": ["Золотой генерал", "Перевернутое серебро", "Конь", "Серебрянный генерал"],
        "img": "img/test/Т.Нари-гин.png",
        "answer":1
    },
    {
        "question": "Что обознатает иероглиф на фигуре?",
        "options": ["Ладья", "Перевернутый конь", "Конь", "Перевернутое копье"],
        "img": "img/test/Т.Нари-Кэй.png",
        "answer":1
    },
    {
        "question": "Что за значение у иероглифа на этой фигуре?",
        "options": ["Ладья", "Перевернутый солдат", "Перевенрутое копье", "Король"],
        "img": "img/test/Т.Нари-кё.png",
        "answer":2
    },
    {
        "question": "Что за значение у иероглифа на фигуре?",
        "options": ["Король", "Королевский генерал", "Перевернутое серебро", "Серебрянный генерал"],
        "img": "img/test/Т.Осё.png",
        "answer":0
    },
{
        "question": "Какое название у фигуры?",
        "options": ["Лошадиный дракон", "Королеский дракон", "Перевернутое серебро", "Золотой генерал"],
        "img": "img/test/Т.Рюма.png",
        "answer":0
    },
    {
        "question": "Как называеться фигура?",
        "options": ["Ладья", "Лошадиный дракон", "Золотой генерал", "Королеский дракон"],
        "img": "img/test/Т.Рюю.png",
        "answer":3
    },
    {
        "question": "Что за значение у иероглифа у фигуры?",
        "options": ["Ладья", "Перевернутый солдат", "Золотой генерал", "Королевский генерал"],
        "img": "img/test/Т.Токин.png",
        "answer":1
    },
    {
        "question": "Что обознатает иероглиф у фигуре?",
        "options": ["Конь", "Солдат", "Король", "Копье"],
        "img": "img/test/Т.Фухё.png",
        "answer":1
    },
    {
        "question": "Назовите эту фигуру",
        "options": ["Перевернутое копье", "Королевский дракон", "Летающая колесница", "Серебрянный генерал"],
        "img": "img/test/Т.Хися.png",
        "answer":2
    },
{
        "question": "Какая фигура может так ходить?",
        "options": ["Королевский генерал", "Пешка", "Конь", "Королевский дракон"],
        "img": "img/test/ТХ.Гёкусё.png",
        "answer":0
    },
    {
        "question": "Какая фигура так ходит?",
        "options": ["Ладья", "Слон", "Конь", "Королевский генерал"],
        "img": "img/test/ТХ.Какугё.png",
        "answer":1
    },
    {
        "question": "Что за фигура может так ходить?",
        "options": ["Серебрянный генерал", "Копье", "Конь", "Ладья"],
        "img": "img/test/ТХ.Кэйма.png",
        "answer":2
    },
    {
        "question": "Назовите фогуру, которая так ходит?",
        "options": ["Королевский генерал", "Серебрянный генерал", "Перевернутый конь", "Перевернутое серебро"],
        "img": "img/test/ТХ.Нари-гин.png",
        "answer":3
    },
    {
        "question": "Назовите фогуру, которая может так ходить?",
        "options": ["Летающая колесница", "Королевский дракон", "Перевернутый конь", "Серебрянный генерал"],
        "img": "img/test/ТХ.Хися.png",
        "answer":0
    },
]

def start_quiz(update, context):
    ans.clear()
    q_asked.clear()
    random.shuffle(id_list)
    q_number = id_list[0]
    send_question(update, context, q_number, 1)

def send_question(update, context, q_number, n):
    query = update.callback_query
    keyboard = []
    for i, option in enumerate(quiz[q_number]["options"]):
        keyboard.append([InlineKeyboardButton(option, callback_data=str(i))])
    keyboard.append([InlineKeyboardButton(text='Вернуться в меню', callback_data='back')])
    reply_markups = InlineKeyboardMarkup(keyboard)
    text = str(n) + "." + quiz[q_number]["question"]
    if quiz[q_number]["img"] != "":
        photo = open(quiz[q_number]["img"], 'rb')
        context.bot.send_photo(chat_id=query.message.chat.id, photo=photo, caption=text, reply_markup=reply_markups)
    else: context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=reply_markups)
    q_asked.append(q_number)

def find_by_questioon(iterable, key, value):
    for index, dict_ in enumerate(iterable):
        if dict_[key] == value:
            return index

def answer_callback(update, context):
    query = update.callback_query
    if query.message.text == None:
        q_number = find_by_questioon(quiz, "question", query.message.caption.split(".")[1])
    else: q_number = find_by_questioon(quiz, "question", query.message.text.split(".")[1])
    answer = int(query.data)
    if answer == quiz[q_number]["answer"]:
        query.answer("Правильно!")
        ans.append(1)
    else:
        query.answer("Непривильно :(")
        ans.append(0)
    if len(q_asked) < 10:
        send_question(update, context, id_list[len(ans)], len(ans)+1)
    else:
        text = f"Тест завершен!\nКоличество правильных ответов: {ans.count(1)}"
        btn = InlineKeyboardButton(text='Вернуться в меню', callback_data='back')
        markup = InlineKeyboardMarkup([[btn]])
        context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=markup)

# Commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('menu', menu))

# Register the callback functions with the bot
dispatcher.add_handler(CallbackQueryHandler(rules, pattern='rules'))
dispatcher.add_handler(CallbackQueryHandler(test, pattern='test'))
dispatcher.add_handler(CallbackQueryHandler(back, pattern='back'))
dispatcher.add_handler(CallbackQueryHandler(Segiban, pattern='Segiban'))
dispatcher.add_handler(CallbackQueryHandler(Komadai, pattern='Komadai'))
dispatcher.add_handler(CallbackQueryHandler(Transformations, pattern='Transformations'))
dispatcher.add_handler(CallbackQueryHandler(Figure, pattern='Figure'))
dispatcher.add_handler(CallbackQueryHandler(Ose_and_Hecuse, pattern='Ose_and_Hecuse'))
dispatcher.add_handler(CallbackQueryHandler(Flying_Chariot, pattern='Flying_Chariot'))
dispatcher.add_handler(CallbackQueryHandler(Royal_dragon, pattern='Royal_dragon'))
dispatcher.add_handler(CallbackQueryHandler(Elephant, pattern='Elephant'))
dispatcher.add_handler(CallbackQueryHandler(Horse_dragon, pattern='Horse_dragon'))
dispatcher.add_handler(CallbackQueryHandler(Golden_general, pattern='Golden_general'))
dispatcher.add_handler(CallbackQueryHandler(Silver_general, pattern='Silver_general'))
dispatcher.add_handler(CallbackQueryHandler(Inverted_silver, pattern='Inverted_silver'))
dispatcher.add_handler(CallbackQueryHandler(Horse, pattern='Horse'))
dispatcher.add_handler(CallbackQueryHandler(Inverted_horse, pattern='Inverted_horse'))
dispatcher.add_handler(CallbackQueryHandler(Spear, pattern='Spear'))
dispatcher.add_handler(CallbackQueryHandler(Inverted_spear, pattern='Inverted_spear'))
dispatcher.add_handler(CallbackQueryHandler(Soldier, pattern='Soldier'))
dispatcher.add_handler(CallbackQueryHandler(Inverted_soldier, pattern='Inverted_soldier'))
dispatcher.add_handler(CallbackQueryHandler(Basic_actions, pattern='Basic_actions'))
dispatcher.add_handler(CallbackQueryHandler(Resets, pattern='Resets'))
dispatcher.add_handler(CallbackQueryHandler(Ban_on_resetting, pattern='Ban_on_resetting'))
dispatcher.add_handler(CallbackQueryHandler(Draw, pattern='Draw'))
dispatcher.add_handler(CallbackQueryHandler(Scoring_points, pattern='Scoring_points'))
dispatcher.add_handler(CallbackQueryHandler(rules_back, pattern='rules_back'))
dispatcher.add_handler(CallbackQueryHandler(figure_back, pattern='figure_back'))
dispatcher.add_handler(CallbackQueryHandler(basic_actions_back, pattern='basic_actions_back'))
dispatcher.add_handler(CallbackQueryHandler(answer_callback))

# Start the bot
updater.start_polling()
