import curses

def get_text_for_input(poster, positions):
    all_position_queen = ""
    for pos in positions:
        if positions[pos] == poster[0]:
            all_position_queen +=  pos

    if all_position_queen == "":
        return f"введите позицию (если {poster} не существует оставьте поле пустым)"
    else:
        return f"позиция {poster}: {all_position_queen}"

#
# def print_moves_king:
#     #шаг вперед назад и по оси и по горизонтам
# def print_moves_queen:
#     # горизонтам и вертикально
#     # и по оси
# def print_moves_bishop:
#     # только по оси
# def print_moves_knight:
#     # по принципу Г
# def print_moves_rook:
#     # по вертикалю и горизонталю
# def print_moves_pawn:
    # два шага вперед или один шага вперед

def menu(stdscr):
    is_correct_position = {
        "КР": 0,
        "Ф": 0,
        "Л": 0,
        "С": 0,
        "К": 0,
        "П": 0,
    }
    max_correct_position = {
        "КР": 1,
        "Ф": 9,
        "Л": 10,
        "С": 10,
        "К": 10,
        "П": 8,
    }
    curses.curs_set(0)
    all_position = {}
    # A8 B8 C8 D8 E8 F8 G8 H8  
    # A7 B7 C7 D7 E7 F7 G7 H7
    # A6 B6 C6 D6 E6 F6 G6 H6
    # A5 B5 C5 D5 E5 F5 G5 H5
    # A4 B4 C4 D4 E4 F4 G4 H4
    # A3 B3 C3 D3 E3 F3 G3 H3
    # A2 B2 C2 D2 E2 F2 G2 H2
    # A1 B1 C1 D1 E1 F1 G1 H1
    
    def set_options():
        global options
        options = [
            "Кароль -- введите позицию",
            f"Ферзь -- {get_text_for_input('Ферьз', all_position)}", 
            f"Ладья -- {get_text_for_input('Ладья', all_position)}",
            f"Слон -- {get_text_for_input("Слон", all_position)}",
            f"Конь -- {get_text_for_input("Конь", all_position)}",
            f"Пешка -- {get_text_for_input("Пешки", all_position)}",
            "Готова",
            "Выйти"
        ]
    set_options()
    index = 0
    summa = 0
    while True:
        stdscr.clear()
        for i, option in enumerate(options):
            if i == index:
                stdscr.addstr(f"> {option}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(f"  {option}\n")
        stdscr.refresh()

        key = stdscr.getch()
        
        if key == curses.KEY_UP:
            index = (index - 1) % len(options)
        elif key == curses.KEY_DOWN:
            index = (index + 1) % len(options)
        elif key in [10, 13]:  # Enter
            if options[index] == "Выйти":
                break
            elif options[index] == "Готова":
                if is_correct_position["КР"] == 0:
                    print("Король должен существовать в игре.")
                else:
                    stdscr.clear()
                    stdscr.refresh()
                    stdscr.addstr("Возможные ходы короля: ")
                    stdscr.addstr("Возможные ходы пешки: ")
                    stdscr.addstr("Возможные ходы королева: ")
                    stdscr.addstr("Возможные ходы коня: ")
                    stdscr.addstr("Возможные ходы слона: ")
                    stdscr.addstr("Возможные ходы ладьи: ")
            else:
                curses.endwin()
                while True:
                    position = input("Введите позицию: ")
                    if position[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] and position[1] in ['1', '2', '3', '4', '5', '6', '7', '8'] and len(position) == 2:
                        if position in all_position:
                            print("Вы набрали уже существующую позицию")
                            continue
                        if summa == 15 + is_correct_position["КР"]:
                            print("Вы не можете добавить новую позицию по теоритически, у вас уже 16 установленных позиции!")
                            input("Нажмите энтер чтобы выйти и потом нажмите готова чтобы вычислить все возможные варианты ходов")
                            break
                        elif is_correct_position[options[index][0]] == max_correct_position[options[index][0]]:
                            print("Вы не можете добавить по теортически такую позиция")
                            input("Нажмите энтер чтобы выйти")
                            break

                        summa += 1
                        is_correct_position[options[index][0]] += 1
                        if options[index][0:5] == "Кароль":
                            all_position[position] = "КР"
                        else:    
                            all_position[position] = options[index][0]
                        set_options()
                        break
                    else:
                        print("Вы набрали несуществующую позицию в шахматах. Ваше позиция должно начаться c a,b,c,d,e,f,g,h и закончится на 1,2,3,4,5,6,7,8. Или ваше позиция состоит из трех значение")

#Коня -> 2...10
#Ладья -> 2...10
#Королевы -> 1...9
#Слона -> 2...10
#Пешак -> 1...8
#Король -> 1


curses.wrapper(menu)