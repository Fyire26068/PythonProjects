def page128():
    """Displays page 128 (comes from 46) (leads to page pages 75, 114, 102, 111; Map on page 47)"""
    print("""\n	You remember how easy it is to climb to the top of
the wall. Whether or not you want to get to the other
side is a different story. Before deciding what to do
next, you look at your map and see that three roads
lead away from the wall. The road north goes to Riva,
the road wesi leads to the Land of Volcas, and the
southwestern road leads toward the coast.\n""")#Story text
    print("""(1) Take the road toward Riva
(2) Head toward the Land of Volcas
(3) Go southwest, toward the coast
(4) Climb over the wall
(5) Check Map\n""")#choices
    choice = input("1, 2, 3, 4, 5")
    if choice == 1:
        page = 75
    elif choice == 2:
    	page = 114
    elif choice == 3:
    	page = 102
    elif choice == 4:
        page = 111
    elif choice == 5:
        page = 128
        print(page47)#should print the map graphic NEEDS TO BE UPDATED WHEN ART IS DONE
    

#page 129 created by Anthony Garrard 10/21/20
def page129():
    """Diplays page 129 (comes from page 88) (leads to page 7 or page 130) """
    print("\n	Once again you have reached the beautiful village of Medea.")#Story text
    if stolenSail == true: #checking if the player has stolen the sailboat NEEDS TO BE UPDATED LATER
    	page = 7
    else:
        print("""\n	The friendly bird woman greets you with open
wings. This time she takes you to an ancient creature
named Mi.""")#Story Text if the boat wasn't stolen
        page = 130

  
#page 130 and 131 except graphic created by Anthony Garrard 10/21/20
def page130():
    """Displays pages 130 and 131 (comes from page 129) (leads to page 133)"""
    print("""\n	Mi sits cross-legged on a mat. She has lost most olers,
her feateand her skin has shrunk so much that in
places it has split, revealing patches of bloodless blue
flesh. For a long lime she stares at you until you wonder whether she is still conscious, or even alive. But
finally she speaks.\n""") #page130 story
    print(""" "Yes, I know where Zindor is-just east of the
Keona Volcano, so close that the crogocides dare not
visit it. But between here and there is a swamp you
can never cross. To reach Zindor you must find Chawakelamptha. lt lies to the north, in the Dazzling
Mountains."\n""") #page131 story
    #print(page131) #should display graphic on pages 130 and 131 NEEDS TO BE UPDATED WHEN GRAPHICS ARE DONE
    page133() #sets next page
    

                   
#page 132 created by Anthony Garrard 10/21/20  
def page132():
    """Displays page 132 (comes from page ??? )(leads to page 88 or page 62, map on page 63) """
    print("""\n	You decide not to stay long in Sera. lnstead, you
plan to move on to one of the nearby villages along
the shore of Lake Shonra in search of new information about the route to Zindor.\n""") #story text
    print("""(1) Take a boat west to Medea\n
    (2) Hike around the lake to Shar\n
    (3) Check Map""") #choices
    choice = input("1, 2, 3") #getting input
    if choice == 1:
        page = 88
    elif choice == 2:
        page = 62
    elif choice == 3:
        page = 132
        print("page63") #should print the map graphic NEEDS TO BE UPDATED WHEN ART IS DONE
    
  
#page 133 created by Anthony Garrard 10/21/20 
def page133():
    """Displays page 133 (comes from page 131)(leads to page 85 or page 55, map on page 63) """
    print("""\n	Mi falls silent; you know you have learned all you
can from her. The next morning you set out again to
reach the Dazzling Mountains. Since you'll have to
go around the western end of Lake Shonra, you follow the road west. After walking several hours you
come to a fork in the road.\n""") #Story Text
    print("""   (1) Take the road to the left or\n
(2) Continue straight ahead
(3) Check Map""") #Choices
    choice = input("1, 2, 3") #getting input for user choice
    if choice == 1:
    	curPage = 85
    elif choice == 2:
    	curPage = 55
    elif choice == 3:
    	curPage = 133 #reinitializing current page
    print("page63") #should print the map graphic NEEDS TO BE UPDATED WHEN ART IS DONE

                   
                   

#Logic is yet to come.
page130()
