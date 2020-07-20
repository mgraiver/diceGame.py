import random

def dice_roll():
    '''
    () -> Int

    Displays the sum of the result of rolling 2 six sided dice
    
    >>> dice_roll(27483)
    5
    >>> random.seed(278)
    >>> dice_roll()
    7
    >>> random.seed(5)
    >>> dice_roll()
    8
    >>> random.seed(3123)
    >>> dice_roll()
    10
    >>> random.seed(862)
    >>> dice_roll()
    11
    
    '''
    dice_1=random.randint(1,6)
    dice_2=random.randint(1,6)
    
    return int(dice_1 + dice_2)
    
# print result of each
def second_stage(point):
    '''
    (int)--> str
    Returns result of each roll until the player wins or loses 
    
    >>> random.seed(56)
    >>> second_stage(5)
    6 10 8 9 8 4 6 9 8 3 7
    >>> random.seed(56)
    >>> second_stage(2)
    6 10 8 9 8 4 6 9 8 3 7
    >>> random.seed(56)
    >>> second_stage(9)
    6 10 8 9
    >>> random.seed(56)
    >>> second_stage(6)
    6 
    >>> random.seed(2329)
    >>> second_stage(9)
    7 
    '''
#   variable representing result of individual roll  
    new_roll=""
#   variable representing result of all rolls
    total_roll=""
    
    while True:
        
        new_roll=dice_roll()

        total_roll += (str(new_roll)+ ' ')
        
        if new_roll==point or new_roll==7:
            break
        
    print (total_roll)
       
    return new_roll

def can_play (players_money,players_bet):
    
    '''
    (float,float)-->boolean

    Returns true if player has enough money to place a bet, false if otherwise

    >>>can_play(0.00,0.00)
    False
    >>>can_play(3.00,0.00)
    False
    >>>can_play(13.83,17.24)
    False
    >>>can_play(15.15,-15.15)
    False
    >>>can_play(5.00,5.00)
    True
    >>>can_play(16.00,13.00)
    True

    '''
    if players_bet<=players_money and players_bet>0:
        return True
    else:
        return False
    
def pass_line_bet(players_money,players_bet):
    '''
    (float,float)--> float
    
    Displays result of all rolls and whether the player wins or loses,
    and returns total money the player has left after the game
    
    >>> random.seed(56)
    pass_line_bet(6,3)
    A 6 has been rolled. Roll again.
    10 8 9 8 4 6 
    You win.
    9.0
    >>> random.seed(3934)
    >>> pass_line_bet(5.00,5.00)
    A 3 has been rolled. You lose!
    0.0
    >>> random.seed(374)
    >>> pass_line_bet(100.00,52.00)
    A 5 has been rolled. Roll again.
    11 4 12 10 6 9 9 12 6 8 9 5 
    You win.
    152.0
    >>> random.seed(374)
    >>> pass_line_bet(135.0343,5.0231)
    A 5 has been rolled. Roll again.
    11 4 12 10 6 9 9 12 6 8 9 5 
    You win.
    140.0574
    >>> random.seed(42)
    >>> pass_line_bet(0.00,0.00)
    A 7 has been rolled. You win!
    0.0
    
    '''    
    roll_1=dice_roll()
    
#   money_left will equal Total_Lost or Total_Won and result of second_stage()
    Total_Lost=float(players_money-players_bet)
    Total_Won=float(players_money+players_bet)
    
    if roll_1 in (7,11):
        print("A", roll_1,  "has been rolled. You win!")
        money_left= Total_Won
        
        
    elif roll_1 in (2,3,12):
        print("A", roll_1,  "has been rolled. You lose!")
        money_left= Total_Lost
    
    else:
        print("A", roll_1,  "has been rolled. Roll again.")
        roll_2=second_stage(roll_1)
             
        if roll_2==roll_1:
            money_left= Total_Won
            print("\nYou win.")
            
        elif roll_2==7:
            print("\nYou lose.")
            money_left=Total_Lost
        
    return money_left
        
def play():
    '''
    ()--> NoneType
    Determines if player can play, if yes, runs Craps

    >>> play()
    Please enter your money here: $9.092
    How much would you like to bet? $10.00
    Insufficient funds. You cannot play.
    >>> play()
    Please enter your money here: $9.5111
    How much would you like to bet? $9.5112
    Insufficient funds. You cannot play.
    >>> play()
    Please enter your money here: $0.00
    How much would you like to bet? $0.00
    Insufficient funds. You cannot play.
    >>> play()
    Please enter your money here: $0.00
    How much would you like to bet? $7.09
    Insufficient funds. You cannot play.
    >>> play()
    Please enter your money here: $900
    How much would you like to bet? $0
    Insufficient funds. You cannot play.
    >>> random.seed(782)
    >>> play()
    Please enter your money here: $9.03
    How much would you like to bet? $2.88
    A 7 has been rolled. You win!
    You now have $ 11.91
    >>> random.seed(827)
    >>> play()
    Please enter your money here: $10.00
    How much would you like to bet? $10.00
    A 6 has been rolled. Roll again.
    9 6 
    You win.
    You now have $ 20.0
    >>> random.seed(828)
    >>> play()
    Please enter your money here: $273
    How much would you like to bet? $2.19
    A 4 has been rolled. Roll again.
    7 
    You lose.
    You now have $ 270.81
    >>> random.seed(2839)
    >>> play()
    Please enter your money here: $28.091
    How much would you like to bet? $28.02
    A 8 has been rolled. Roll again.
    8 
    You win.
    You now have $ 56.11
    '''
    
    players_money=float(input("Please enter your money here: $"))
    players_bet=float(input("How much would you like to bet? $"))

    can_play (players_money,players_bet)
    
    if can_play (players_money,players_bet)== True:
        money_left= pass_line_bet(players_money,players_bet)
        print("You now have $", (round(money_left,2)))
        
    if can_play (players_money,players_bet)== False:
        print("Insufficient funds. You cannot play.")
        


    
        
