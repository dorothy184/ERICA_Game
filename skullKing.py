#-*-coding: utf-8-*-
from __future__ import print_function  # <-- this should be the first
import random


def choice(message):
    answer = raw_input(message)
    while answer not in {"y", "n"}:
        answer = raw_input(message)
    if answer == "y":
        return True
    else:
        return False


def sunseo():  # 순서정하기 함수
    rank = [0, 0, 0, 0]
    jusawe = [1, 2, 3, 4]
    name = ["com1", "com2", "com3", "player"]
    ans = []
    random.shuffle(jusawe)
    for i in range(4):
        cnt = 0
        for j in range(4):
            if jusawe[i] < jusawe[j]:
                cnt = cnt + 1
        rank[i] = cnt + 1

    cnt = 0
    while cnt < 4:
        ans.append(name[rank.index(4 - cnt)])
        rank[rank.index(4 - cnt)] = 0
        cnt = cnt + 1

    return ans


def Deck():
    # Escape < B=Y=R<G < Mermaid < Pirate<SkullKing
    # 1       2 3 4 5    6        7       8
    deck = []
    for k in range(5):
        deck.append((1, k))
    for color in range(2, 6):
        for k in range(1, 14):
            deck.append((color, k))
    for k in range(2):
        deck.append((6, k))
    for k in range(5):
        deck.append((7, k))
    for k in range(1):
        deck.append((8, k))
    random.shuffle(deck)
    return deck


def cardlist(deck):
    cardlist = []
    for i in range(len(deck)):
        if int(deck[i][0]) == 1:
            cardlist.append("Escape_" + str(deck[i][1]))
        elif int(deck[i][0]) == 2:
            cardlist.append("Blue_" + str(deck[i][1]))
        elif int(deck[i][0]) == 3:
            cardlist.append("Yellow_" + str(deck[i][1]))
        elif int(deck[i][0]) == 4:
            cardlist.append("Red_" + str(deck[i][1]))
        elif int(deck[i][0]) == 5:
            cardlist.append("Grey_" + str(deck[i][1]))
        elif int(deck[i][0]) == 6:
            cardlist.append("Mermaid_" + str(deck[i][1]))
        elif int(deck[i][0]) == 7:
            cardlist.append("Pirate_" + str(deck[i][1]))
        elif int(deck[i][0]) == 8:
            cardlist.append("SkullKing_" + str(deck[i][1]))
    return cardlist


def display_card(cardlist):
    print("|  ",end="")
    if(len(cardlist)==1):
        print(cardlist[len(cardlist) - 1], " |")
    else:
        for i in range(len(cardlist) - 1):
            print(cardlist[i], " |  ",end="")
        print(cardlist[len(cardlist) - 1], " |")

def show_your_card(player, com1, com2, com3, players):
    show = 1
    for i in range(4):
        if players[i] == "player":
            if show == 1:
                print("내가 가지고 있는 카드는\n")
                display_card(cardlist(player))
                print()
                return show
            elif show == 2:
                print("내가 가지고 있는 카드는\n")
                display_card(cardlist(player))
                print()
                return show
            elif show == 3:
                print("내가 가지고 있는 카드는\n")
                display_card(cardlist(player))
                print()
                return show
            else:
                print("내가 가지고 있는 카드는\n")
                display_card(cardlist(player))
                print()
                return show
        else:
            show += 1


def spread_card(round):
    deck = Deck()
    player = []
    com1 = []
    com2 = []
    com3 = []
    for i in range(round):
        player.append(deck[0])
        deck = deck[1:]
        com1.append(deck[0])
        deck = deck[1:]
        com2.append(deck[0])
        deck = deck[1:]
        com3.append(deck[0])
        deck = deck[1:]
    return player, com1, com2, com3


def sun_player_present(players, player, com1, com2, com3):
    if (players[0] == "player"):
        show_your_card(player, com1, com2, com3, players)
        c = raw_input("리드 수트로 제시할 카드를 입력하시오.")
        lead_suit = cardremove(c, player)
    elif (players[0] == "com1"):
        lead_suit = cardchange2(com1[0])
        com1 = com1[1:]
        print("com1이 리드 수트를 제시합니다")
        print("리드 수트는", lead_suit, "입니다")
        print()
    elif (players[0] == "com2"):
        lead_suit = cardchange2(com2[0])
        com2 = com2[1:]
        print("com2가 리드 수트를 제시합니다")
        print("리드 수트는", lead_suit, "입니다")
        print()
    elif (players[0] == "com3"):
        lead_suit = cardchange2(com3[0])
        com3 = com3[1:]
        print("com3가 리드 수트를 제시합니다")
        print("리드 수트는", lead_suit, "입니다")
        print()

    return lead_suit


def big(a, b):
    bool = False
    if (int(a[0]) > int(b[0]) or int(a[0]) == int(b[0]) and int(a[1]) > int(b[1])):
        bool = True
    return bool


def num_big(a, b):
    bool = False
    if (int(a[0]) == int(b[0]) and int(a[1]) > int(b[1])):
        bool = True
    return bool


def no_card(who, lead_suit):  # 낼 카드가 0개인지 확인
    no = 0
    for i in range(len(who)):
        if int(lead_suit[0]) == 1 or int(lead_suit[0]) == 7 or int(lead_suit[0]) == 8:
            if big(who[i], lead_suit):
                no = no + 1
        elif int(lead_suit[0]) == 2 or int(lead_suit[0]) == 3 or int(lead_suit[0]) == 4 or int(lead_suit[0]) == 5:
            if int(who[i][0]) == 2 or int(who[i][0]) == 3 or int(who[i][0]) == 4 or int(who[i][0]) == 5:
                if num_big(who[i], lead_suit):  # lead_suit가 B, Y, R, G 레벨일 경우, 카드 숫자가 더 커야 함
                    no = no + 1
            else:
                if big(who[i], lead_suit):
                    no = no + 1
        elif int(lead_suit[0]) == 6:
            if int(who[i][0]) == 8:  # lead_suit가 Mermaid 레벨일 경우, who가 Pirate이어도 카드를 못 냄
                continue
            else:
                if big(who[i], lead_suit):
                    no = no + 1
    return no


def higher_level(c, lead_suit):
    bool = False
    if int(lead_suit[0]) == 1 or int(lead_suit[0]) == 7 or int(lead_suit[0]) == 8:
        if big(c, lead_suit):
            bool = True
    elif int(lead_suit[0]) == 2 or int(lead_suit[0]) == 3 or int(lead_suit[0]) == 4 or int(lead_suit[0]) == 5:
        if int(c[0]) == 2 or int(c[0]) == 3 or int(c[0]) == 4 or int(c[0]) == 5:
            if num_big(c, lead_suit):  # lead_suit가 B, Y, R, G 레벨일 경우, 카드 숫자가 더 커야 함
                bool = True
        else:
            if big(c, lead_suit):
                bool = True
    elif int(lead_suit[0]) == 6:
        if int(c[0]) != 8:  # lead_suit가 Mermaid 레벨일 경우, who가 Pirate이어도 카드를 못 냄
            if big(c, lead_suit):
                bool = True
    return bool


def player_draw_card(player, lead_suit,players,compare, r_winner):
    if (no_card(player, cardchange1(lead_suit)) <= 0):
        print("player는 낼 카드가 없습니다 ")
        print("player는 게임에서 탈락합니다. Bye~")
        print()
        players.remove("player")
        print()
        return player
    print()
    print("내가 가지고 있는 카드는")
    print()
    display_card(cardlist(player))
    print()
    while True:
        c = raw_input("제시할 카드를 입력해 주세요.")
        c_num = cardchange1(c)
        bool = False
        i=-1
        while(i<len(player)-1):
            i+=1
            if (c_num[0] == player[i][0] and c_num[1] == player[i][1] and higher_level(c_num, cardchange1(lead_suit))):
                bool = True
                break
        if(bool):
            break
        else:
            continue
    cardremove(c, player)
    if (higher_level(c_num, cardchange1(compare))):
        compare = c
        r_winner = "player"
    if (no_card(player, cardchange1(lead_suit)) <= 0):
        print("player는 낼 카드가 없습니다 ")
        print("player는 게임에서 탈락합니다. Bye~")
        print()
        players.remove("player")
        print()
        return player



def save_winnings(a):  # a= boolean
    tries += 1
    members[username] = members[username][0], tries, wins
    store_members(members)
    again = input("게임을 계속 하시겠습니까?(y/n)")
    if again == y:
        if a:
            ++wins
        Skull_King()
    else:
        print("게임을 종료합니다.")
        exit(0)


def store_members(members):
    file = open("members.txt", "w")
    name = members.keys()
    for name in names:
        password, tries, wins = members[name]
        line = name + ',' + password + ',' + str(tries) + '+' + str(wins) + '\n'
        file.write(line)
    file.close()


def rule():
    a = choice("Skull_King의 규칙을 아시나요?(y/n) ")
    if a != True:
        if choice("게임 규칙에 대한 설명을 들으시겠습니까?(y/n) ") == True:
            print("\nⅠ. 카드 소개",
                  "카드는 일반 카드 52장과 특수 카드 14장으로 이루어져 있다 ",
                  "일반 카드엔 13장의 옐로우, 블루, 레드, 그레이 카드가 있고 ",
                  "특수 카드엔 탈출 5장, 해적 5장, 인어 2장, 스컬킹 1장이 있다. ",
                  "카드 랭킹은 탈출<블루=옐로우=레드<그레이<인어<해적 순이며 ",
                  "스컬킹은 인어를 제외한 모든 카드보다 높은 랭킹을 가진다.\n",
                  "Ⅱ. 게임 준비",
                  "게임은 총 5라운드로 진행되며, 카드를 섞은 후 현재 라운드 수만큼 나누어 같는다.\n",
                  "Ⅲ. 용어 설명"
                  "리드 수트: 선플레이어가 제시한 카드 ",
                  "트릭: 선플레이어의 카드 제시하면 나머지 플레이어들은 돌아가며 같은 색깔의 높은 숫자의 카드 혹은 높은 레벨의 카드를 내야 한다. ",
                  "이처럼 모든 플레이어들이 순차적으로 카드를 내는 것을 트릭이라 하며, 이중에서 가장 높은 레벨의 카드를 제시한 자가 트릭을 딴다.\n",
                  "Ⅳ. 라운드 진행",
                  "라운드 시작 전 플레이어에겐 배팅 선택의 기회가 주어진다. ",
                  "그 후 첫번째 판을 시작하고, 선플레이어가 리드 수트를 제시하고, 나머지 플레이어들이 돌아가며 카드를 낸다. ",
                  "만약 제시할 카드가 없다면, 그 플레이어는 바로 게임에서 탈락한다. 판에서 가장 높은 카드를 제시한 플레이어가 그 판을 승리한다. ",
                  "판의 승리자는 +1점을 얻는다. 이는 게임의 최종 점수에 반영되는 것이 아닌 라운드의 승리자를 가리기 위한 것이다.\n",
                  "Ⅴ. 라운드 종료 후",
                  "라운드 종료 후 라운드의 승리자만이 +30점 얻는다. ",
                  "배팅 했을 시 예측했던 트릭수가 맞은 경우 (트릭수 * 20) 점을 획득하고 ",
                  "틀렸을 경우 (예측 트릭수와 실제 따낸 트릭수의 차 * 10)점을 잃는다.\n", sep='\n')
            print()
            print("규칙을 다 읽으셨나요? ")
            print("다 읽으셨다면 엔터를 누르세요.")
            while True:
                try:
                    if "" == input():
                        break
                    else:
                        continue
                except:
                    continue

            print("그럼 게임을 시작합니다.")
            print()
        else:
            print("그럼 게임을 시작합니다.")
            print()
    else:
        print("그럼 게임을 시작합니다.")


def trick(predict, real):
    score = 0
    if predict == real:
        score += real * 20
    else:
        score -= abs(predict - real) * 10
    return score


def load_members():
    file = open("members.txt", "r")
    members = {}
    for line in file:
        name, passwd, tries, wins = line.strip('\n').split(',')
        members[name] = (passwd, int(tries), float(wins))
    file.close()
    return members


def login(members):
    username = input("사용자명을 입력하십시오: (4 글자 이내) ")
    while len(username) > 4:
        username = input("사용자명을 입력하십시오: (4 글자 이내) ")
    trypasswd = input("비밀번호를 입력하십시오: ")
    if username in members.keys():
        if trypasswd == members[username][0]:
            print("플레이 횟수: ", members[username][1], "\n" "승리 횟수: ",
                  members[username][2])  # username의 게임시도 횟수와 이긴 횟수를 members에서 가져와 보여준다.

            if members[username][1] == 0:
                print("당신의 승률은 0 % 입니다.")
            else:
                print("당신의 승률은 ", "{0:.1f}".format(members[username][2] / members[username][1] * 100), "% 입니다.")
            tries, wins = members[username][1], members[username][2]
            return username, tries, wins, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd, 0, 0)
        return username, 0, 0, members


def BetorNot():
    bet = int(input("얼마에 배팅하시겠습니까? "))
    while bet > 10 or bet < 0:
        print("잘못된 숫자입니다. 다시 입력하십시오.")
        bet = int(input("얼마에 배팅하시겠습니까? "))
    return bet

def computer_bet(computer,betcardlist,beforecard,players,compare,r_winner):
    #computer는 현재 제시할 컴퓨터 이름ex) computer2, betcardlist는 그 컴퓨터의 카드가 있는 리스트 ex)com2
    #beforecard는 전 플레이어나 컴퓨터가 낸 카드
    color_partition = beforecard.split('_')
    newbeforecard = []
    canbetcard = []
    if color_partition[0] == "Escape":
        newbeforecard.append((1,int(color_partition[1])))
    elif color_partition[0] == "Blue":
        newbeforecard.append((2,int(color_partition[1])))
    elif color_partition[0] == "Yellow":
        newbeforecard.append((3,int(color_partition[1])))
    elif color_partition[0] == "Red":
        newbeforecard.append((4,int(color_partition[1])))
    elif color_partition[0] == "Grey":
        newbeforecard.append((5,int(color_partition[1])))
    elif color_partition[0] == "Mermaid":
        newbeforecard.append((6,int(color_partition[1])))
    elif color_partition[0] == "Pirate":
        newbeforecard.append((7,int(color_partition[1])))
    elif color_partition[0] == "SkullKing":
        newbeforecard.append((8,int(color_partition[1])))
    for i in range(len(betcardlist)):
        if (higher_level(betcardlist[i], newbeforecard[0])):
            canbetcard.append(betcardlist[i])
    random.shuffle(canbetcard)
    if(len(canbetcard)==0):
        print(computer + "낼 카드가 없습니다")
        print(computer+"는 게임에서 탈락합니다. Bye~")
        print()
        players.remove(computer)
        return 0
    computercard = canbetcard[0]
    if(higher_level(computercard,cardchange1(compare))):
        compare=cardchange2(computercard)
        r_winner=computer
    print(computer,"가",cardchange2(computercard) ,"카드를 제시하였습니다.");
    betcardlist.remove(computercard)
    return 0


def cardremove(cardname, player):
    partitioncard = []
    partitioncard = cardname.split('_')
    if partitioncard[0] == "Escape":
        player.remove((1, int(partitioncard[1])))
    elif partitioncard[0] == "Blue":
        player.remove((2, int(partitioncard[1])))
    elif partitioncard[0] == "Yellow":
        player.remove((3, int(partitioncard[1])))
    elif partitioncard[0] == "Red":
        player.remove((4, int(partitioncard[1])))
    elif partitioncard[0] == "Grey":
        player.remove((5, int(partitioncard[1])))
    elif partitioncard[0] == "Mermaid":
        player.remove((6, int(partitioncard[1])))
    elif partitioncard[0] == "Pirate":
        player.remove((7, int(partitioncard[1])))
    elif partitioncard[0] == "SkullKing":
        player.remove((8, int(partitioncard[1])))

    return cardname

def cardchange1(card_munza):
    partitioncard = []
    partitioncard = card_munza.split('_')
    if partitioncard[0] == "Escape":
        tuplecard = ((1, int(partitioncard[1])))
    elif partitioncard[0] == "Blue":
        tuplecard=((2, int(partitioncard[1])))
    elif partitioncard[0] == "Yellow":
        tuplecard = ((3, int(partitioncard[1])))
    elif partitioncard[0] == "Red":
        tuplecard = ((4, int(partitioncard[1])))
    elif partitioncard[0] == "Grey":
        tuplecard = ((5, int(partitioncard[1])))
    elif partitioncard[0] == "Mermaid":
        tuplecard = ((6, int(partitioncard[1])))
    elif partitioncard[0] == "Pirate":
        tuplecard = ((7, int(partitioncard[1])))
    elif partitioncard[0] == "SkullKing":
        tuplecard = ((8, int(partitioncard[1])))

    return tuplecard

def cardchange2(card):
    if int(card[0]) == 1:
        munza=("Escape_" + str(card[1]))
    elif int(card[0]) == 2:
        munza=("Blue_" + str(card[1]))
    elif int(card[0]) == 3:
        munza=("Yellow_" + str(card[1]))
    elif int(card[0]) == 4:
        munza=("Red_" + str(card[1]))
    elif int(card[0]) == 5:
        munza=("Grey_" + str(card[1]))
    elif int(card[0]) == 6:
        munza=("Mermaid_" + str(card[1]))
    elif int(card[0]) == 7:
        munza=("Pirate_" + str(card[1]))
    elif int(card[0]) == 8:
        munza=("SkullKing_" + str(card[1]))
    return munza

def Skull_King():
    rule()  # 설명 할지 말지 선택 & 설명
    round=1
    p_s=0
    c1_s=0
    c2_s=0
    c3_s=0
    while (round <= 5):
        print()
        print(round, "round를 시작합니다")
        print()
        players=sunseo()
        card = cardlist(Deck())
        player, com1, com2, com3 = spread_card(round)
        leadsuit = sun_player_present(players, player, com1, com2, com3)
        compare=leadsuit
        r_winner=players[0]
        while(len(players)>0):
            if (players[0] == "com1"):
                computer_bet("com2", com1, leadsuit, players, compare, r_winner)
                player_draw_card(player, leadsuit, players,compare, r_winner)
                computer_bet("com3", com1, leadsuit, players,compare, r_winner)
            elif (players[0] == "player"):
                computer_bet("com2", com1, leadsuit, players,compare, r_winner)
                computer_bet("com1", com1, leadsuit, players,compare, r_winner)
                computer_bet("com3", com1, leadsuit, players,compare, r_winner)
            elif (players[0] == "com2"):
                computer_bet("com1", com1, leadsuit, players,compare, r_winner)
                computer_bet("com3", com1, leadsuit, players,compare, r_winner)
                player_draw_card(player, leadsuit, players,compare, r_winner)
            elif (players[0] == "com3"):
                computer_bet("com1", com1, leadsuit, players,compare, r_winner)
                computer_bet("com2", com1, leadsuit, players,compare, r_winner)
                player_draw_card(player, leadsuit, players,compare, r_winner)
            print("라운드의 위너는 ", r_winner, "입니다")
            if(r_winner=="player"):
                p_s+=1
            elif (r_winner == "com1"):
                c1_s += 1
            elif (r_winner == "com2"):
                c2_s += 1
            elif (r_winner == "com3"):
                c3_s += 1
            print("점수 집계")
            print("player:",p_s," ,com1:", c1_s,", com2:", c2_s, ", com3:", c3_s)
            break;
        round+=1
    final = [p_s, c1_s, c2_s, c3_s]
    f_player = ["player", "com1", "com2", "com3"]
    max = [final[0]]
    max_p = ["player"]
    for i in range(1, 4):
        if (max[0] < final[i]):
            max.remove(max[0])
            max_p.remove(max_p[0])
            max.append(final[i])
            max_p.append(f_player[i])
    print("이 게임의 최종 승자는")
    for i in range(len(max_p)):
        print(max_p[i])
    print("입니다")
Skull_King()
