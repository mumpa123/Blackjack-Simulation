#Sole Author: Patrick Coker


from random import randint,shuffle
import matplotlib.pyplot as plt 
import numpy as np 
import time
# DC = dealer face up card


#game parameters that can and will be changed
#from game/rules side: hit or stand on soft 17. Payout of blackjack. whether you can dd on all hands.
#resplit aces. double on split aces. double on split any. deck penetration. num of decks. 



#global constants
#min increment $5
#start with min bet = 10 max 10000

class Card:
    def __init__(self,value): #value of card
        self.value = value 




class Hand:
    def __init__(self,cards,bet):
        self.cards = cards 
        self.bet = bet 




class Player:
    def __init__(self,name,bankroll,min_bet): #name should be type string
        self.name = name
        self.bankroll = bankroll
        self.bet = min_bet
        self.completed_hands = []
        self.running_count = 0
    #actions: consult basic strategy then makes move. 
    def hand(self,hand): #players bet and the cards he is dealt. maybe i should split betting and getting cards into two methods, not sure.
        #cards are a list of card objects whose value is the amount the card is worth
        # causes the player to make bet and get a hand dealt to him.
        self.hands = [hand]

    def action(self,up_card): #up_card = dealer up card then based on that decide what to do.
        act_val = 0
        act_val = basic_strategy(self.hands[0].cards,up_card.value)
        if act_val == 1:
            # print('hit')
            return "hit"
        elif act_val == 2:
            # print('stand')
            self.completed_hands.append(self.hands.pop(0))
            return "stand"
        elif act_val == 3:
            # print("split")
            self.hands.append(Hand([self.hands[0].cards[0]],self.bet))
            self.hands.append(Hand([self.hands[0].cards[1]],self.bet))
            

            
            return "split"
        elif act_val == 4:
            # print('double')
            self.hands[0].bet *= 2
            # self.completed_hands.append(self.hands.pop(0))
            
            return "double"
        else:
            # print('stand')
            return "stand"



    # def win(self):
    #     return 

    # def lose(self):
    #     return 

   
    
    #if split i need to recall betting etc.



def sum_cards(cards):
    
    card_vals = []
    for i in cards:
        if (i.value >= 10) and (i.value != 11):
            card_vals.append(10)
        elif i.value == 1:
            card_vals.append(11)
        else:
            card_vals.append(i.value)

#could recursively go through
    total = sum(card_vals)
    while (total > 21) and (11 in card_vals):
        if (total > 21) and (11 in card_vals):
            for j,i in enumerate(card_vals):
                if i == 11:
                    card_vals[j] = 1
                    total = sum(card_vals)
                    break
    
    
    return total,card_vals



def basic_strategy(cards,up_card):
    action_value = 2
    total_sum,card_vals = sum_cards(cards)

    #pair splitting
    if len(card_vals) == 2:
        if (cards[0].value == cards[1].value):
            
            card1 = card_vals[0]
            if (card1 == 1):
                #split
                return 3
            elif (card1 == 9):
                if (up_card != 7) and (up_card != 10) and (up_card != 11):
                    #split
                    return 3 
            elif (card1 == 8):
                #split
                return 3
            elif (card1 == 7):
                if (up_card <= 7):
                    #split
                    return 3
            elif (card1 == 6): #note TODO double after split parameter not currently implemented
                if (up_card <= 6):
                    #split
                    return 3
            elif (card1 == 4):
                if (up_card == 5) or (up_card == 6):
                    #split
                    return 3
            elif (card1 == 3) or (card1 == 2):
                if (up_card <= 7):
                    #split
                    return 3

        #end of pair splitting






    
    #soft totals
    
    if (11 in card_vals):
        if (total_sum >= 20):
            #stand
            return 2 #need to change to action_value number whatever that is
        elif (total_sum == 19) and (up_card == 6):
            #double
            return 4
        elif (total_sum == 19) and (up_card != 19):
            #stand
            return 2
        elif (total_sum == 18) and ((up_card >= 2) and (up_card <= 6)):
            #double
            return 4
        elif (total_sum == 18) and ((up_card == 8) or (up_card == 7)):
            #double
            return 4
        elif (total_sum == 18):
            #hit
            return 1
        elif (total_sum == 17) and ((up_card >= 3) and up_card <= 6):
            #double
            return 4
        elif (total_sum == 17):
            #hit
            return 1
        elif (total_sum == 16) or (total_sum == 15):
            if (up_card >= 4) and (up_card <= 6):
                #double
                return 4
            else:
                #hit
                return 1
        elif (total_sum == 13) or (total_sum == 14):
            if (up_card == 5) or (up_card == 6):
                #double
                return 4
            else:
                #hit
                return 1
    #end of soft total decisions 

    #hard totals 
    if (11 not in card_vals):
        if (total_sum >= 17):
            #stand
            return 2
        elif (total_sum >= 13):
            if (up_card >= 2) and (up_card <= 6):
                #stand
                return 2
        
            elif (up_card >= 7):
                #hit
                return 1 
        elif (total_sum == 12):
            if (up_card <= 3) or (up_card >= 7):
                #hit 
                return 1
            elif (up_card >= 4) or (up_crd <= 6):
                #stand
                return 2
        elif (total_sum == 11):
            #double
            return 4
        elif (total_sum == 10):
            if (up_card <= 9):
                #double
                return 4 
            elif (up_card >= 10):
                #hit
                return 1 
        elif (total_sum == 9):
            if (up_card == 2) or (up_card >= 7):
                #hit
                return 1
            elif (up_card >=3) or (up_card <= 6):
                #double
                return 4 
        elif (total_sum <= 8):
            #hit 
            return 1 

        #end of hard totals


    



    # if card1 == card2:
    #     if split:
    #         split()
    #         basic_strategy(new_cards,up_card)
    #     elif soft_total:


        #if soft total:
        #else:
        #if hard total:

    
    return action_value 


class Dealer:
    def __init__(self,num):  #num is just like what number the dealer is, just to differentiate. Probably don't need just make a dealer andstick that in every game.
        self.num = num 

    def hit():
        return 

    def stand():
        return 



def new_card(player):
    new_card = deck.popitem()[1]
    count(player,new_card.value)
    return new_card
def count(player,card_val):
    if card_val == 1:
        player.running_count += 1
    if card_val >= 10:
        player.running_count += 1
    if card_val <= 6:
        player.running_count += 1
# should i make a game class and run instances it to play multiple games at once?


def game_round(player, deck): #deck = the dictionary of cards, player = player object, 
    #i'm gonna use popitem thus its gonna pull from the back of the deck
    bet = 0
    bet += player.bet 

    player.hand(Hand([deck.popitem()[1],deck.popitem()[1]],bet))
    dealer_hand = [deck.popitem()[1],deck.popitem()[1]]
    
    if (sum_cards(player.hands[0].cards) == 21) and (sum_cards(dealer_hand) != 21):
        player.bankroll += 1.5 * bet
        return "blackjack"
    dealer_upcard = dealer_hand[0] 
    count(player,dealer_upcard.value)
    # act = player.action(dealer_upcard) #player action (hit,stand,double,split)
    flag = True
    curr_hand = 0
    while player.hands:
        flag = True
        while flag:
            act = player.action(dealer_upcard) #player action (hit,stand,double,split)
            if act == "hit":
                player.hands[0].cards.append(deck.popitem()[1])
            elif act == "double":
                player.hands[0].cards.append(deck.popitem()[1])
                player.completed_hands.append(player.hands.pop(0))
                flag = False 
                curr_hand = 0
            elif act == "stand":
                flag = False
                curr_hand = 0
            elif act == "split":
                player.hands[-1].cards.append(deck.popitem()[1])
                player.hands[-2].cards.append(deck.popitem()[1])
                player.hands.pop(0)
                if ((sum_cards(player.hands[-1].cards)[0] == 21) and (sum_cards(dealer_hand)[0] != 21)):
                    player.bankroll += 1.5 * player.hands[-1].bet
                    player.hands[-1].bet = 0
                    # flag = False
                    player.hands.pop(-1)
                if len(player.hands) > 1:
                    if ((sum_cards(player.hands[-2].cards)[0] == 21) and (sum_cards(dealer_hand)[0] != 21)):
                        player.bankroll += 1.5 * player.hands[-2].bet
                        player.hands[-2].bet = 0
                        # flag = False
                        player.hands.pop(-2)
                    
        
        # curr_hand += 1
        # if curr_hand == 20:
        #     for i in player.hands:
        #         print('player cards are: ',end='')
        #         for j in i.cards:
        #             print(j.value,end=', ')
        #     print("\n totaling: ", sum_cards(i.cards)[0])
        #     print()
        #     time.sleep(10000)
            
        
    # for i in player.completed_hands:
    #     print('player cards are: ',end='')
    #     for j in i.cards:
    #         print(j.value,end=', ')
    #     print("\n totaling: ", sum_cards(i.cards)[0])
    #     print()

    # player_total = sum_cards(player.cards)[0]
    # print(player_total)
        

    while sum_cards(dealer_hand)[0] < 17:
        dealer_hand.append(deck.popitem()[1])

    dealer_total = sum_cards(dealer_hand)[0]
    for comp_hand in player.completed_hands:
        player_total = sum_cards(comp_hand.cards)[0]
        if (player_total > 21):
            player.bankroll -= comp_hand.bet 
            return "player loses"
        elif (dealer_total > 21):
            player.bankroll += comp_hand.bet
            return "player wins"
        elif (player_total > dealer_total):
            player.bankroll += comp_hand.bet 
            return "player wins"
        elif (player_total < dealer_total): #push 
            player.bankroll -= comp_hand.bet
            return "player loses"
        else:
            return "push"
    


    #game logic




    #results add and take away money


    return "game_round() function ran"



def build_deck(num_decks):
    cards = []
    card_dict = {}
    for i in range(num_decks):
        for val in range(1,5):
            for j in range(1,14):
                cards.append(Card(j))
                
    
    shuffle(cards) #shuffles deck
    for index,i in enumerate(cards): #puts deck into dictionary with the key the index of the card in the deck ie index 1 = first card and index 100 is 100th card from top of deck.
        card_dict[index+1] = i

    return card_dict 

def simulation(num_decks,num_players):
    
    card_dict = build_deck(num_decks)
    tot_vals = []
    tot_rounds = []
    for i in range(100): #run 10,000 sets of ~500 hands (till runs out of money each time up to 1000)
        tot_vals = []
        John = Player("John",750,5)
        num_games = 0
        while (num_games < 100000) and (John.bankroll >= 0):
            if len(card_dict) < (0.25 * (num_decks*52)):
                card_dict = build_deck(num_decks)
            
            game_round(John,card_dict)
            John.completed_hands = []
            # print("------------------")
            num_games += 1  
            tot_vals.append(John.bankroll)
        #     print("total = ", John.bankroll)
        
        # print('total = ', John.bankroll)
        # print("number of rounds = ", num_games)
        
        tot_rounds.append(num_games)

        val_vals = np.arange(1,len(tot_vals)+1)
        
            # plt.grid()
        # plt.scatter(val_vals,tot_vals,s=2)
        # plt.show()
    
    #post process data
    freq_dict = {}
    for val in tot_rounds:
        freq_dict[val] = freq_dict.get(val,0) + 1
    print('average =', sum(tot_rounds) / len(tot_rounds))

    tot_rounds.sort()
    

    values = list(freq_dict.keys())
    freq = list(freq_dict.values())
    plt.bar(values,freq,width=25)
    plt.grid()
    plt.show()

    
    return num_players



#order of events.
#dealer shuffles
#dealer puts deck in shoe and puts the stop card i forget what its called, the thing indicating deck pen
#all players bet
#players are dealt 2 cards face up
#dealer is dealt 1 card face down and 1 face up(ie known to player)
#if player_hand = 21 then blackjack if dealer does not have blackjack. if dealer has blackjack and player does not then money is taken away immediately and the hand is over.
#else player either hits,stands,doubles,splits, until stand or bust
#hand is over money gets paid out.


def main():
    simulation(6,1)
    print("Ran Successfully")
    return
    


if __name__ == "__main__":
    main()

