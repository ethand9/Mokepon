import random  # RNG function
import time    # Sleep function


class Menu:  # Menu of options
   def intro(self):  # randomize encounter
       rnum = random.randrange(1, 4)  # random number 1-3
       if rnum == 1:
           print("Rival Gray has challenged you to a Mokepon battle!")
       elif rnum == 2:
           rlvl = random.randrange(5, 8)  # random number 5-7
           print("You encountered a level", rlvl, "pidgley!")  # random level
       elif rnum == 3:
           print("You challenged Gym Leader Borc to a Mokepon battle!")

       input("Press 'Enter' to summon your Mokepon.\n")  # wait until user presses enter
       print("Go Squittle!")
       time.sleep(1)  # wait 1 sec

       if rnum == 1:
           print("Rival Gray summoned Pidgley!\n")
           time.sleep(1)  # wait 1 sec
       elif rnum == 2:
           print("\n", end = "") # only one new line
       elif rnum == 3:
           print("Gym Leader Borc summoned Pidgley!\n")
           time.sleep(1)  # wait 1 sec

   def welcome(self, pg_life, sq_life, items, ap):    # user chooses an action
       # objects
       menu1 = Attack()     # menu for attacks
       menu2 = Bag()        # menu for items
       menu4 = Run()        # end program
       pidgley = Pidgley()  # enemy attacks

       while ((pg_life[0] > 0) and (sq_life[0] > 0)):  # while both alive
           again1 = True             # always run at least once
           while again1 == True:     # while user has not chosen action
               again = True          # always run at least once
               while again == True:  # loop until valid number
                   try:
                       print("1. Squittle\n"  # bring up set of attacks
                             "2. Bag\n"       # bring up items
                             "3. Mokepon\n"   # does nothing
                             "4. Run\n"       # flavor, does not do anything. Repeat code
                             "Squittle HP:", sq_life[0], end="")  # print hp without newline
                       if sq_life[3] == 1:  # if paralyzed
                           print(",\033[1;33;0m PAR\033[1;30;0m;", end="  ")  # print PAR in yellow text then revert to default color
                       elif sq_life[3] == 0:     # if normal
                           print(";  ", end="")  # separate health totals
                       print("Pidgley HP:", pg_life[0])  # pidgley hp

                       action = int(input("Enter the number of the action you want to take.\n"))  # take input
                       again = False  # don't loop again

                       if((action > 4) or (action < 1)):  # if invalid number
                           print("Please enter a valid number.")
                           again = True  # loop again
                   except ValueError:  # if invalid data type
                       print("Please enter a valid number.")
                       again = True  # loop again
                   print("\n")  # new lines

               if action == 1:  # Attack
                   again1 = menu1.menuAttack(pg_life, sq_life, ap)  # open up attacks, pass in life values and action points
               elif action == 2:  # Bag
                   again1 = menu2.menuBag(pg_life, sq_life, items, ap)  # open item menu, pass in lives, inventory, ap
               elif action == 3:  # Mokepon
                   print("You have no other Mokepons!\n")
                   time.sleep(1)  # wait 1 sec
                   again1 = True  # run again
               elif action == 4:  # Run
                   menu4.exit(pg_life, sq_life)  # exit program
                   again1 = False                # do not run again
               else:  # unexpected error
                   print("An error has occurred.")

           if((pg_life[0] > 0) and (sq_life[0] > 0)):  # while both alive
               # Enemy pidgley attacks
               rnum1 = random.randrange(1, 5)  # random number 1-4
               if rnum1 == 1:    # tackle
                   pidgley.tackle(sq_life)     # call tackle
               elif rnum1 == 2:  # peck
                   pidgley.peck(sq_life)       # call peck
               elif rnum1 == 3:  # screech
                   pidgley.screech(sq_life)    # call screech
               elif rnum1 == 4:  # body slam
                   pidgley.body_slam(sq_life)  # call body slam
               else:
                   print("An error has occurred.")

               if sq_life[0] <= 0:  # if user's mokepon died
                   print("Squittle fainted!\n"
                         "GAME OVER")


class Attack:
   def menuAttack(self, pg_life, sq_life, ap):  # menu for attacks
       menu2 = Squittle()   # object menu2, call user's attacks

       again = True          # always run at least once
       while again == True:  # loop until valid number
           try:
               print("1. Tackle:", ap[0], "\n"
                     "2. Watergun:", ap[1], "\n"
                     "3. Tailwhip:", ap[2], "\n"
                     "4. Withdraw:", ap[3], "\n"
                     "5. Go back\n"
                     "Squittle HP:", sq_life[0], end="")  # print hp without newline
               if sq_life[3] == 1:  # if paralyzed
                   print(",\033[1;33;0m PAR\033[1;30;0m;", end="  ")  # print PAR in yellow text then revert to default color
               elif sq_life[3] == 0:     # if normal
                   print(";  ", end="")  # separate health totals
               print("Pidgley HP:", pg_life[0])  # pidgley hp

               action = int(input("Enter the number of the action you want to take.\n"))  # get input
               again = False  # don't loop again

               if ((action > 5) or (action < 1)):  # if invalid number
                   print("Please enter a valid number.")
                   again = True  # loop again
           except ValueError:  # if invalid data type
               print("Please enter a valid number.")
               again = True  # loop again
       time.sleep(.5)  # wait .5 sec

       # User attacks
       if((action >= 1) and (action <= 4)):  # if attacking
           if sq_life[3] == 1:  # if paralyzed
               rnum = random.randrange(1, 3)  # random range, 1 or 2
               if rnum == 1:   # 50% chance to be paralyzed
                   action = 0  # do not attack
           if action == 1:    # tackle
               menu2.tackle(pg_life, sq_life, ap)    # call tackle
           elif action == 2:  # watergun
               menu2.watergun(pg_life, sq_life, ap)  # call watergun
           elif action == 3:  # tailwhip
               menu2.tailwhip(pg_life, sq_life, ap)  # call tailwhip
           elif action == 4:  # withdraw
               menu2.withdraw(pg_life, sq_life, ap)  # call withdraw
           elif action == 0:  # paralyzed
               print("Squittle is paralyzed and can't move!\n")
               time.sleep(1)  # wait 1 sec
       elif action == 5:  # go back
           return True  # run loop again
       else:
           print("An error has occurred.")

       if(pg_life[0] <=0 and sq_life[0] <= 0):  # both die
           print("Both mokepon fainted!\n"
                 "It's a tie!")
       elif pg_life[0] <= 0:  # enemy dies
           print("Pidgley fainted!\n"
                 "Congratulations, you win!")
       elif sq_life[0] <= 0:  # user dies
           print("Squittle fainted!\n"
                 "GAME OVER")
       return False  # do not loop again


class Pidgley:  # enemy pokemon
   def __init__(self):
       rnum = random.randrange(1, 4)  # random number 1-3

       self.pg_hp = 29 + rnum  # random hp range, default 29
       self.pg_def = 6  # enemy defense

   def rtrn_val(self):
       pg_life = [self.pg_hp, self.pg_def]  # list of values
       return pg_life

   def tackle(self, sq_life):  # deal damage
       print("Pidgley used tackle!")
       time.sleep(1)  # wait 1 sec

       rnum = random.randrange(50, 61)     # random number from 50-60
       dmg = int(rnum * (1 / sq_life[1]))  # random range, lowered by defense
       print("Squittle lost", dmg, "hp.\n")
       time.sleep(1)  # wait 1 sec
       sq_life[0] -= dmg  # hp minus damage

   def peck(self, sq_life):  # deal damage
       print("Pidgley used peck!")
       time.sleep(1)  # wait 1 sec

       rnum = random.randrange(40, 71)     # random number from 40-70
       dmg = int(rnum * (1 / sq_life[1]))  # random range, lowered by defense
       print("Squittle lost", dmg, "hp.\n")
       time.sleep(1)  # wait 1 sec
       sq_life[0] -= dmg  # hp minus damage

   def screech(self, sq_life):  # lower user's attack
       print("Pidgley used screech!")
       time.sleep(1)  # wait 1 sec
       print("Squittle's attack decreased.\n")
       time.sleep(1)  # wait 1 sec

       sq_life[2] -= 1  # attack minus 1

   def body_slam(self, sq_life):  # deal minor damage and possible paralyze
       print("Pidgley used body slam!")
       time.sleep(1)  # wait 1 sec

       rnum = random.randrange(20, 61)  # random number from 20-60
       if rnum >= 30:  # 75% chance to be paralyzed
           print("Squittle has been paralyzed!")
           time.sleep(1)  # wait 1 sec
           sq_life[3] = 1  # set status to paralyzed

       dmg = int(rnum * (1 / sq_life[1]))  # random range, lowered by defense
       print("Squittle lost", dmg, "hp.\n")
       time.sleep(1)  # wait 1 sec
       sq_life[0] -= dmg  # hp minus damage


class Squittle:  # User's pokemon
   def __init__(self):
       # life values
       self.sq_hp = 24  # hitpoints of squittle
       self.sq_def = 8  # defense of squittle
       self.sq_atk = 8  # attack of squittle
       self.sq_st = 0   # number indicates the status effect: 0 is normal, 1 is paralyzed
       self.sq_life = [self.sq_hp, self.sq_def, self.sq_atk, self.sq_st]  # list of life values

       # action points
       self.tkAP = 3  # tackle action poiints
       self.wgAP = 3  # watergun ap
       self.twAP = 3  # tailwhip ap
       self.wdAP = 3  # withdraw ap
       self.ap = [self.tkAP, self.wgAP, self.twAP, self.wdAP]  # list of action points

   def rtrn_val(self):
       return(self.sq_life, self.ap)  # return life values

   def tackle(self, pg_life, sq_life, ap):  # deal damage
       if ap[0] > 0:  # if action has points
           print("Squittle used tackle!")
           time.sleep(1)  # wait 1 sec

           rnum = random.randrange(50, 76)  # random number from 50-75

           if rnum > 70:  # critical hit, multiply damage
               print("It was a critical hit!")
               time.sleep(1)  # wait 1 sec
               dmg = int((sq_life[2]/8) * (1.5 * (rnum * (1/pg_life[1]))))  # random range affected by attack and defense
           else:  # if not high damage
               dmg = int((sq_life[2]/8) * (rnum * (1/pg_life[1])))  # random range affected by attack and defense
           ap[0] -= 1  # minus one action point
       else:  # if no ap
           print("That move does not have any action points!")
           time.sleep(1)  # wait 1 sec
           print("Squittle used struggle!")
           time.sleep(1)  # wait 1 sec
           print("Squittle lost 5 hp to recoil.")
           time.sleep(1)  # wait 1 sec
           sq_life[0] -= 5  # user hp minus 5
           dmg = 5  # damage = 5

       print("Pidgley lost", dmg, "hp.\n")
       time.sleep(1)  # wait 1 sec
       pg_life[0] -= dmg  # hp minus dmg

   def watergun(self, pg_life, sq_life, ap):  # deal damage
       if ap[1] > 0:  # if have ap
           print("Squittle used watergun!")
           time.sleep(1)  # wait 1 sec

           rnum = random.randrange(65, 101)  # random number from 65-100
           if rnum > 90:  # if high damage
               print("It was a critical hit!")
               time.sleep(1)  # wait 1 sec
               dmg = int((sq_life[2]/8) * (1.5 * (rnum * (1/pg_life[1]))))  # random range affected by attack and defense
           else:  # if not high damage
               dmg = int((sq_life[2]/8) * (rnum * (1/pg_life[1])))  # random range affected by attack and defense
           ap[1] -= 1  # minus one from action point
       else:  # if no ap
           print("That move does not have any action points!")
           time.sleep(1)  # wait 1 sec
           print("Squittle used struggle!")
           time.sleep(1)  # wait 1 sec
           print("Squittle lost 5 hp to recoil.")
           time.sleep(1)  # wait 1 sec
           sq_life[0] -= 5  # user hp - 5
           dmg = 5  # 5 damage

       print("Pidgley lost", dmg, "hp.\n")
       time.sleep(1)  # wait 1 sec
       pg_life[0] -= dmg  # enemy hp - damage

   def tailwhip(self, pg_life, sq_life, ap):  # lower enemy defense
       if ap[2] > 0:  # if have ap
           print("Squittle used tailwhip!")
           time.sleep(1)  # wait 1 sec
           print("Pidgley's defense decreased.\n")
           time.sleep(1)  # wait 1 sec

           pg_life[1] -= 1  # pidgley defense decreased by 1
           ap[2] -= 1       # minus one action point
       else:  # if no ap
           print("That move does not have any action points!")
           time.sleep(1)  # wait 1 sec
           print("Squittle used struggle!")
           time.sleep(1)  # wait 1 sec
           print("Squittle lost 5 hp to recoil.")
           time.sleep(1)  # wait 1 sec
           sq_life[0] -= 5  # minus 5 from user hp
           dmg = 5  # 5 damage

           print("Pidgley lost", dmg, "hp.\n")
           time.sleep(1)  # wait 1 sec
           pg_life[0] -= dmg  # deal damage to enemy hp

   def withdraw(self, pg_life, sq_life, ap):  # increase user hp
       if ap[3] > 0:  # if ap have
           print("Squittle used withdraw!")
           time.sleep(1)  # wait 1 sec
           print("Squittle's defense increased.\n")
           time.sleep(1)  # wait 1 sec

           sq_life[1] += 1  # squittle defense increased by 1
           ap[3] -= 1       # minus one action point
       else:  # no ap
           print("That move does not have any action points!")
           time.sleep(1)  # wait 1 sec
           print("Squittle used struggle!")
           time.sleep(1)  # wait 1 sec
           print("Squittle lost 5 hp to recoil.")
           time.sleep(1)  # wait 1 sec
           sq_life[0] -= 5  # damage to user hp
           dmg = 5          # 5 to enemy hp

           print("Pidgley lost", dmg, "hp.\n")
           time.sleep(1)  # wait 1 sec
           pg_life[0] -= dmg  # enemy hp minus damage


class Bag:  # Backpack of items
   def __init__(self):
       # inventory
       self.oran1 = 1      # number of oran berries
       self.potion1 = 1    # number of potions
       self.ether1 = 1     # number of ether potions
       self.fullheal1 = 1  # number of full heal potions
       self.items = [self.oran1, self.potion1, self.ether1, self.fullheal1]  # list of items

       self.sq_hp = 24  # same as user hp, default 24

   def rtrn_val(self):
       return self.items

   def menuBag(self, pg_life, sq_life, items, ap):  # menu of items
       print("You open your backpack.")

       again2 = True             # always run at least once
       while again2 == True:     # while user has not made action
           again = True          # always run at least once
           while again == True:  # loop until valid number
               try:
                   print("1. Oran Berry:", items[0], "\n"  # Display options and items available
                         "2. Potion:", items[1], "\n"
                         "3. Ether:", items[2], "\n"
                         "4. Full Heal:", items[3], "\n"
                         "5. Go back\n"
                         "Squittle HP:", sq_life[0], end="")  # print hp without newline
                   if sq_life[3] == 1:  # if paralyzed
                       print(",\033[1;33;0m PAR\033[1;30;0m;", end="  ")  # print PAR in yellow text then revert to default color
                   elif sq_life[3] == 0:     # if normal
                       print(";  ", end="")  # separate health totals
                   print("Pidgley HP:", pg_life[0])  # pidgley hp

                   action = int(input("Enter the number of the action you want to take.\n"))
                   again = False  # don't loop again

                   if((action > 5) or (action < 1)):  # if invalid number
                       print("Please enter a valid number.")
                       again = True  # loop again
               except ValueError:  # if invalid data type
                   print("Please enter a valid number.")
                   again = True  # loop again
               print("\n")

           if action == 1:       # oran berry
               if items[0] > 0:  # item exists
                   self.oran(sq_life, items)  # call oran
                   again2 = False  # do not loop again
               else:
                   print("You have run out of that item!\n")
                   time.sleep(1)  # wait 1 sec
                   again2 = True  # loop again
           elif action == 2:     # potion
               if items[1] > 0:  # item exists
                   self.potion(sq_life, items)  # call potion
                   again2 = False  # do not loop again
               else:
                   print("You have run out of that item!\n")
                   time.sleep(1)  # wait 1 sec
                   again2 = True  # loop again
           elif action == 3:     # ether
               if items[2] > 0:  # item exists
                   again2 = self.ether(ap, items)  # user ether, loop again depending on choice
               else:
                   print("You have run out of that item!\n")
                   time.sleep(1)  # wait 1 sec
                   again2 = True  # loop again
           elif action == 4:     # full heal
               if items[3] > 0:  # item exists
                   self.fullheal(sq_life, items)  # call full heal
                   again2 = False  # do not loop again
               else:
                   print("You have run out of that item!\n")
                   time.sleep(1)  # wait 1 sec
                   again2 = True  # loop again
           elif action == 5:  # go back
               return True  # loop again
           else:  # unexpected error
               print("An error has occurred.")
       return False  # do not loop again

   def oran(self, sq_life, items):  # heal for 5
       print("Squittle ate the oran berry.")
       time.sleep(1)  # wait 1 sec

       if sq_life[0] >= 20:  # if heal for less than 5
           heal = self.sq_hp - sq_life[0]  # heal for max hp minus current hp
           sq_life[0] = self.sq_hp  # current hp set to max
       else:  # if can heal for 5
           heal = 5  # heal for 5
           sq_life[0] += heal  # heal for this amount
       items[0] -= 1  # minus 1 item of oran
       print("Squittle healed", heal, "hitpoints.\n")
       time.sleep(1)  # wait 1 sec

   def potion(self, sq_life, items):  # heal for 10
       print("You used the potion on Squittle")
       time.sleep(1)  # wait 1 sec

       if sq_life[0] >= 15:  # if heal for less than 10
           heal = self.sq_hp - sq_life[0]  # max hp minus current hp
           sq_life[0] = self.sq_hp  # set to max hp
       else:  # if heal for 10
           heal = 10  # heal for 10
           sq_life[0] += heal  # add 10 to hp
       items[1] -= 1  # minus one item of potion
       print("Squittle healed", heal, "hitpoints.\n")
       time.sleep(1)  # wait 1 sec

   def ether(self, ap, items):  # restore ap to a move
       again = True  # loop again
       while again == True:  # loop until valid number
           try:
               print("1. Tackle:", ap[0], "\n"  # Display options and items available
                     "2. Watergun:", ap[1], "\n"
                     "3. Tailwhip:", ap[2], "\n"
                     "4. Withdraw:", ap[3], "\n"
                     "5. Go back\n")

               action = int(input("Enter the number of the move you want to restore.\n"))  # get input
               again = False  # do not loop again

               if ((action > 5) or (action < 1)):  # if invalid number
                   print("Please enter a valid number.")
                   again = True  # loop again
           except ValueError:  # if invalid data type
               print("Please enter a valid number.")
               again = True  # loop again
           print("\n")  # multiple line breaks

       if(action > 0) and (action < 5):  # if using item
           items[2] -= 1  # minus 1 item of full heal
           print("You used the ether on Squittle.")
           time.sleep(1)  # wait 1 sec
           if action == 1:  # tackle
               ap[0] = 3  # set ap to 3
               print("The action points for tackle have been restored.\n")
           if action == 2:  # watergun
               ap[1] = 3  # set ap to 3
               print("The action points for watergun have been restored.\n")
           if action == 3:  # tailwhip
               ap[2] = 3  # set ap to 3
               print("The action points for tailwhip have been restored.\n")
           if action == 4:  # withdraw
               ap[3] = 3  # set ap to 3
               print("The action points for withdraw have been restored.\n")

           time.sleep(1)  # wait 1 sec
           return False   # do not run again
       if action == 5:  # if go back
           return True  # run again

   def fullheal(self, sq_life, items):  # cure status effects
       items[3] -= 1  # minus 1 item of full heal
       print("You used the full heal on Squittle.")
       time.sleep(1)  # wait 1 sec
       print("Squittle has been cured of all its status effects!\n")
       time.sleep(1)  # wait 1 sec
       sq_life[3] = 0  # set status to normal


class Run:  # Run away
   def exit(self, pg_life, sq_life):  # exit game
       print("You successfully ran away from the battle!")
       time.sleep(.5)  # wait .5 sec
       pg_life[0] = 0  # enemy hp to 0
       sq_life[0] = 0  # user hp to 0

