#Sole Author: Patrick Coker

#3-0 implements counting

from random import randint,shuffle
import matplotlib.pyplot as plt 
import numpy as np 
import time
import keyboard
import os
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
        self.true_count = 0
        self.running_count = 0
        self.true_count_hist = []
        self.results = []
        
    #actions: consult basic strategy then makes move. 
    def hand(self,hand): #players bet and the cards he is dealt. maybe i should split betting and getting cards into two methods, not sure.
        #cards are a list of card objects whose value is the amount the card is worth
        # causes the player to make bet and get a hand dealt to him.
        self.hands = [hand]

    def true_counter(self,num_cards_left):
        self.true_count = self.running_count / (num_cards_left / 52) #num decks left
        self.true_count_hist.append(self.true_count)
        
        
        
        
    def action(self,up_card,bet): #up_card = dealer up card then based on that decide what to do.
        act_val = 0
        act_val = basic_strategy(self.hands[0].cards,up_card.value)
        if act_val == 1:
            # print('hit')
            return "hit"
        elif act_val == 2:
            # print('stand')
            # self.completed_hands.append(self.hands.pop(0))
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



    def win(self):
        self.results.append(1)
        

    def lose(self):
        self.results.append(-1)
        
    def push(self):
        self.results.append(0)

   
    
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
    # action_value = 2
    total_sum,card_vals = sum_cards(cards)

    #pair splitting
    if len(card_vals) == 2:
        #problem here
        # print(card_vals[0],', ', card_vals[1])
        if (card_vals[0] == card_vals[1]) or (card_vals[0] == 1 and card_vals[1] == 1) or (card_vals[0] == 11 or card_vals[0] == 1):
            # print("yes")
            card1 = card_vals[0]
            if (card1 == 1):
                #split
                # print("split")
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
        elif (total_sum == 19):
            #stand
            return 2
        elif (total_sum == 18) and ((up_card >= 2) and (up_card <= 6)):
            #double
            return 4
        elif (total_sum == 18) and ((up_card == 8) or (up_card == 7)):
            #stand
            return 2
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
    # if (11 not in card_vals):
    if (total_sum >= 17):
        #stand
        return 2
    elif (total_sum >= 13):
        if (up_card >= 2) and (up_card <= 6):
            #stand
            return 2
    
        elif (up_card >= 7) or (up_card == 1):
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

    
    


class Dealer:
    def __init__(self,num):  #num is just like what number the dealer is, just to differentiate. Probably don't need just make a dealer andstick that in every game.
        self.num = num 

    def hit():
        return 

    def stand():
        return 



def new_card(player,deck): #counts the card that gets played and increases the value voila. need to replace all deck.popitem()[1] with this function but only do dealers hidden card after hand is over.
    new_card = deck.popitem()[1]
    count(player,new_card.value)
    # print('card = ', new_card.value)
    # print('running count = ', player.running_count)
    
    return new_card


def count(player,card_val):
    if (card_val >= 10) or (card_val == 1):
        player.running_count -= 1
        # print("plus 1 card val = ", card_val)
    if (card_val <= 6) and (card_val != 1):
        player.running_count += 1
        # print("minus 1 card val = ", card_val)
# should i make a game class and run instances it to play multiple games at once?


def game_round(player, deck): #deck = the dictionary of cards, player = player object, 
    #i'm gonna use popitem thus its gonna pull from the back of the deck
    bet = 0
    player.bet = 10     
    bet += player.bet 
    player.completed_hands = []
    
    # if player.true_count >= 3:
    #     player.bet = 200
    #     bet = player.bet
    
    player.hand(Hand([new_card(player,deck),new_card(player,deck)],bet))
    dealer_hand = [new_card(player,deck),deck.popitem()[1]]
    
    
    if (sum_cards(player.hands[0].cards)[0] == 21) and (sum_cards(dealer_hand)[0] == 21):
        count(player,dealer_hand[1].value)
        return "push"
    
    if (sum_cards(player.hands[0].cards)[0] != 21) and (sum_cards(dealer_hand)[0] == 21):
        player.bankroll -= bet 
        count(player,dealer_hand[1].value)
        return "oof"
   
    if (sum_cards(player.hands[0].cards)[0] == 21) and (sum_cards(dealer_hand)[0] != 21):
        
        player.bankroll += 1.5 * bet
        count(player,dealer_hand[1].value)
        return "blackjack"
    dealer_upcard = dealer_hand[0] 
    # count(player,dealer_upcard.value)
    # act = player.action(dealer_upcard) #player action (hit,stand,double,split)
    flag = True
    curr_hand = 0
    
    while player.hands:
        flag = True
        flag1 = False
        flag2 = False
        while flag:
            act = player.action(dealer_upcard,bet) #player action (hit,stand,double,split)
            if act == "hit":
                player.hands[0].cards.append(new_card(player,deck))
                
                   
            elif act == "double":
                if len(player.hands[0].cards) == 2:
                    player.hands[0].cards.append(new_card(player,deck))
                    
                    player.completed_hands.append(player.hands.pop(0))
                    flag = False 
                    curr_hand = 0
                    
                else:
                    player.hands[0].cards.append(new_card(player,deck))
                    
            elif act == "stand":
                flag = False
                
                player.completed_hands.append(player.hands.pop(0))
                
                curr_hand = 0
            elif act == "split":
                
                player.hands[-1].cards.append(new_card(player,deck))
                player.hands[-2].cards.append(new_card(player,deck))
                player.hands.pop(0)
                
                if ((sum_cards(player.hands[-1].cards)[0] == 21) and (sum_cards(dealer_hand)[0] != 21)):
                    player.bankroll += player.hands[-1].bet
                    player.hands[-1].bet = 0
                    flag = False
                    flag1 = True
                    
                if len(player.hands) > 1:
                    if ((sum_cards(player.hands[-2].cards)[0] == 21) and (sum_cards(dealer_hand)[0] != 21)):
                        player.bankroll += player.hands[-2].bet
                        # print('hooyah')
                        player.hands[-2].bet = 0
                        flag = False
                        flag2 = True
                       

                if flag1 and flag2:
                    player.completed_hands.append(player.hands.pop(-1))
                    player.completed_hands.append(player.hands.pop(-1))
                elif flag1:
                    player.completed_hands.append(player.hands.pop(-1))
                elif flag2:
                    player.completed_hands.append(player.hands.pop(-2))
        # curr_hand += 1
        # if curr_hand == 20:
        #     for i in player.hands:
        #         print('player cards are: ',end='')
        #         for j in i.cards:
        #             print(j.value,end=', ')
        #     print("\n totaling: ", sum_cards(i.cards)[0])
        #     print()
        #     time.sleep(10000)
        
            
        for j,comp in enumerate(player.completed_hands):
            p_total = sum_cards(comp.cards)[0]
            if p_total > 21:
               
                player.bankroll -= comp.bet 
                player.completed_hands.remove(comp)
    # for i in player.completed_hands:
    #     print('player cards are: ',end='')
    #     for j in i.cards:
    #         print(j.value,end=', ')
    #     print("\n totaling: ", sum_cards(i.cards)[0])
    #     print()

    # player_total = sum_cards(player.cards)[0]
    # print(player_total)
        
    count(player,dealer_hand[1].value)
    
    dealer_flag = True
    while sum_cards(dealer_hand)[0] <= 16:
        dealer_hand.append(new_card(player,deck))
    # while dealer_flag:
    #     dealer_total,dealer_vals = sum_cards(dealer_hand)
    #     if (dealer_total < 17):
    #         dealer_hand.append(new_card(player,deck))
    #     elif (dealer_total == 17) and (11 in dealer_vals):
    #         dealer_hand.append(new_card(player,deck))
    #     if (dealer_total > 17):
    #         dealer_flag = False
    #     if (dealer_total == 17) and (11 not in dealer_vals):
    #         dealer_flag = False

    dealer_total = sum_cards(dealer_hand)[0]
    # print(len(player.completed_hands))
    for comp_hand in player.completed_hands:
        player_total = sum_cards(comp_hand.cards)[0]
        # print("cards: ")
        # for card in comp_hand.cards:
        #     print(card.value,end=', ')
        # print()
        # print("total_sum_cards = ", sum_cards(comp_hand.cards)[0])
        # print("bet = ", comp_hand.bet)
        
        if (player_total > 21):
            player.bankroll -= comp_hand.bet 
            player.lose()
            
            result = "loss"
        elif (dealer_total > 21):
            
            player.bankroll += comp_hand.bet
            player.win()
           
            result = "win"
        elif (player_total > dealer_total):
            player.bankroll += comp_hand.bet 
            player.win()
            # print("hello")
            result = "win"
        elif (player_total < dealer_total): 
            player.bankroll -= comp_hand.bet
            player.lose()
            
            result = "loss"
        elif (player_total == dealer_total):
            player.push()
            
            result = "push"
        else:
            print("not good")
    


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
    for i in range(10): #run 10,000 sets of ~500 hands (till runs out of money each time up to 1000)
        tot_vals = []
        John = Player("John",1000,10)
        num_games = 0
        while (num_games < 50000) and (John.bankroll >= 0):
            if len(card_dict) < (0.25 * (num_decks*52)):
                card_dict = build_deck(num_decks)
                
                John.running_count = 0
                # print(John.true_count)
                John.true_count = 0
            
            John.true_counter(len(card_dict))
            
            game_round(John,card_dict)
            John.hands = []
            John.completed_hands = []
            # print("------------------")
            num_games += 1  
            tot_vals.append(John.bankroll)
            # print("total = ", John.bankroll)
            # print("running count = ", John.running_count)
        
        # print('total = ', John.bankroll)
        
        # print("number of rounds = ", num_games)
        
        tot_rounds.append(num_games)

        val_vals = np.arange(1,len(tot_vals)+1)
        true_count_indices = np.arange(1,len(John.true_count_hist)+1)
            # plt.grid()


        #plots main
        # fig,ax = plt.subplots()
        # ax.bar(true_count_indices,John.true_count_hist,color='orange')
        
        # ax.set_xlabel("hand number")
        # ax.set_ylabel("true count")
        # ax2 = ax.twinx()
        # ax2.scatter(val_vals,tot_vals,s=2)
        # ax2.set_ylabel("bankroll")
        # plt.grid()
        # plt.show()
        #end plot

        #plots
        # fig, (money, count_true) = plt.subplots(1, 2)
        # fig.suptitle('Horizontally stacked subplots')
        # money.scatter(val_vals, tot_vals,s=4)
        # money.grid()
        # count_true.scatter(true_count_indices, John.true_count_hist,s=8,color='orange')
        # count_true.grid()
        # plt.show()
        #end plot


        # plt.scatter(val_vals,tot_vals,s=2)
        # plt.scatter(true_count_indices,John.true_count_hist,s=3,color='orange')
        # plt.show()

        true_count_vals = John.true_count_hist 
        true_round = []
        
        
       
    #post process data
    freq_dict = {}
    for val in tot_rounds:
        freq_dict[val] = freq_dict.get(val,0) + 1
    print('average =', sum(tot_rounds) / len(tot_rounds))

    tot_rounds.sort()
    

    values = list(freq_dict.keys())
    freq = list(freq_dict.values())
    plt.bar(values,freq,width=500)
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

