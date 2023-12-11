def print_with_pause(text):
    print(text)

def intro():
        print_with_pause("Вітаю у грі під назвою KidreY!")
        print_with_pause("Ви опинились на загадковому острові.")
        print_with_pause("Ваша ціль знайти давно втрачений скарб.")
        print_with_pause("Виберіть звідки почнете пошуки")
        print_with_pause("підводний світ (1),")
        print_with_pause("чарівний ліс (2)")
        print_with_pause("Ваш вибір?")

def first_choice():
    choice1 = input("1 або 2?")
    if choice1 == "1":
        underwater_world()
    elif choice1 == "2":
        magical_forest()
        first_choice()
    else:
        print_with_pause("Будьте уважні!")
        first_choice()

def underwater_world():
    print_with_pause("Ви потрапили у підводний світ.")
    print_with_pause("Куди прямуєте далі?")
    print_with_pause("На пошуки помічника рибку Немо (1), до акули (2), у гості до русалоньки (3)")
    choice2 = input("Що оберете?")
    if choice2 == "1":
        print_with_pause("Ви опинились біля двох морських зірок.")
        print_with_pause("За одною з них знаходиться рибка Немо.")
        choice21 = input("Яку ви оберете? \nВелика з колючками? (1) \nМаленька в горошину (2)")
        if choice21 == "1":
            print_with_pause("Завдяки своїй хорошій інтуіції ви знайшли рибку Немо з першого разу!")
            print_with_pause("Рибка Немо повела вас повз коралові рифи до мушлі.")
            print_with_pause("Щоб відкрити її потрібно знайти ключ!")
            print_with_pause("За мушлею ви бачите три морські водорості.")
            choice211 = input("Яку виберете? \nЧорна? (1) \nЗелена? (2) \nФіолетова? (3)")
            if choice211 == "1":
                print_with_pause("Там нічого немає:(")
                game_lost()
            elif choice211 == "2":
                print_with_pause("Там був морський коник, який вас викрав :(")
                game_lost()
            elif choice211 == "3":
                print_with_pause("Бінго, тут знаходиться ключ!")
                print_with_pause("Ви відімкнули мушлю та побачили підказку у вигляді карти!")
                print_with_pause("На якій вказано шлях до лісу, де знаходиться скарб!")
        elif choice21 == "2":
            print_with_pause("За нею ховався морський їжак :(")
            game_lost()
    elif choice2 == "2":
        print_with_pause("Акула побачила в тобі здобич і з'їла :(")
        game_lost()
    elif choice2 == "3":
        print_with_pause("Вона зачарувала вас своїм спвівом і ви забули про скарб :(")
        game_lost()
    else:
        print_with_pause("Будьте уважні!")
        underwater_world()
    
def magical_forest():
    print_with_pause("Ви опинились в чарівному лісі.")
    print_with_pause("Тут ви знайдете те, що так довго шукали!")
    print_with_pause("Перед вами дві стежини:")
    print_with_pause("до печери (1),")
    print_with_pause("до дерева з дуплом (2)")
    choice3 = input("Куди підете?")
    if choice3 == "1":
        print_with_pause("Ви потрапили в пастку павука гіганта :(")
        game_lost()
    elif choice3 == "2":
        print_with_pause("Вас зустріла білочка і пригостила смаколиками.")
        print_with_pause("Та дала на вибір зілля, яке у майбутньому стане в нагоді!")
        choice31 = input("Яке виберете? \nГолубе зілля? (1) \nЖовте зілля? (2) \nЧервоне зілля? (3)")
        if choice31 == "1":
            print_with_pause("Сила - бачити в темряві.")
            print_with_pause("Нічим не допоможе :(")
            game_lost()
        elif choice31 =="2":
            print_with_pause("Сила - вміння читати думки людей.")
            print_with_pause("Нічим не допоможе :(")
            game_lost()
        elif choice31 == "3":
            print_with_pause("Сила - бути невидимкою.")
            print_with_pause("Молодець!")
            print_with_pause("Ви зробили правильний вибір!")
            print_with_pause("Це допоможе обійти монстра в наступному завданні.")
        else:
            print_with_pause("Будьте уважні!")

def find_treasure():
    print_with_pause("Пройшовши густий ліс, ви натрапили на скалу!")
    print_with_pause("Вона була під охороною монстра.")
    print_with_pause("Тут вам і знадобиться зілля!")
    print_with_pause("Випийте його!")
    print_with_pause("Ура! Ви стали невидимкою та змогли пройти повз монстраю")
    print_with_pause("В скалі є троє дверей.")
    print_with_pause("Одна з яких приведе вас до скарбу!")
    print_with_pause("Дерев'яні двері (1), титанові двері (2), платинові двері (3)")
    choice4 = input("Ваш вибір?")
    if choice4 == "1":
        print_with_pause("Ви потрапили в бібліотеку :(")
        print_with_pause("Упс! Ви програли.")        
        game_lost()
    elif choice4 == "2":
        print_with_pause("Ви потрапили в покинутий замок :(")
        print_with_pause("Упс! Ви програли.")
        game_lost()
    elif choice4 =="3":
        print_with_pause("Ви потрапили в чарівне місце заповнене золотом та дорогоцінним камінням!!!")
        print_with_pause("Вітаю ви виграли!") 
        print_with_pause("Ви впорались з завданням та віднайшли скарб!")

def game_lost():
    print_with_pause("Ви програли!")
    




        

