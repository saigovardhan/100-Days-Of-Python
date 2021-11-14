print("Welcome to Treasure Island.\nYour mission is to find the Treasure")
direction = input("left or right? ")
direction_lower = direction.lower()
if(direction_lower == "right"):
  print("Game Over")
elif(direction_lower =="left"):
  action = input("Swim or wait? ")
  action_lower = action.lower()
  if(action_lower == "swim"):
    print("Game over")
  elif(action_lower=="wait"):
    way = input("Whick door? Red, Blue, Yellow ")
    way_lower = way.lower()
    if(way_lower == "red"or way_lower =="blue"):
      print("Game over")
    elif(way_lower=="yellow"):
      print("YOU WIN!!")
