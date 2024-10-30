# This is the starting of BhokLagyo App.Initially it's directed towards buidling a kind of app that helps indecisive people like me to decide what to eat when i am hungry
foods = [
    {'name': 'momo', 'texture': 'chewy', 'type': 'heavy', 'cravings': 'savory'},
    {'name': 'chatpat', 'texture': 'crunchy', 'type': 'light', 'cravings': 'spicy, snack'},
    {'name': 'burger', 'texture': 'softcrunch', 'type': 'heavy', 'cravings': 'hearty, fast food'},
    {'name': 'spicynoodles', 'texture': 'softchewy', 'type': 'moderate', 'cravings': 'spicy, comfort, umami'},
    {'name': 'junkies', 'texture': 'crunchy', 'type': 'light', 'cravings': 'snack, quick'}
]
hunger_lowlevel=[1,2,3,4]
hunger_midlevel=[5,6,7]
hunger_highlevel=[8,9,10]
def ask_hungryman():
    print("Hmmmm!! Looks like u are hungry but can't decide what to eat.")
    print("Don't Worry ! I'll help u find out what is that u want to eat")
    print("Before that let me ask you some questions..")
    while True: 
      try:
         hungry_level=int(input("On the scale of 1-10 how hungry are  you?"))
         if hungry_level < 1 or hungry_level > 10:
          raise ValueError
         break
      except ValueError:
        print("Please Enter any number in the range 1-10")
    if hungry_level in hunger_lowlevel:
        print("Poof! You are a human for now")
    elif hungry_level in hunger_midlevel:
        print("Alright! Helping u right now before u turn into a monster.")
    elif hungry_level in hunger_highlevel:
        print("In the name of Jesus..........")
    

    textures=[food['texture'] for food in foods]
    type={food['type'] for food in foods}
    cravings={food['cravings'] for food in foods}
    print(f'Textures:{','.join(textures)}')
    print(f'Type:{','.join(type)}')
    print(f'Cravings:{','.join(cravings)}')

    user_texture=input("Enter the texture u like to feel in your mouth:").lower()
    user_type=input("Enter the type of food u want to eat:").lower()
    user_cravings=input("Enter any specific cravings u have:").lower()
    while True:
        food_names=[food['name'] for food in foods if food["texture"]==user_texture and food['type']==user_type and food["cravings"]==user_cravings]
        if food_names:
          print(f"I'm sure u will love : {",".join(food_names)}")
        else:
         print("Ooops I can't help you with that")
      
  
        modifications=input("Do u want to change anythings").lower()
        if modifications=='yes':
         change_options=int(input("what do u like to change choose 1 for texture,2 for type,3 for cravingts"))
         if change_options==1:
            user_texture=input("Enter the texture u like to feel in your mouth:").lower()
         elif change_options==2:
            user_type=input("Enter the type of food u want to eat:").lower()
         elif change_options==3:
                user_cravings=input("Enter any specific cravings u have:").lower()
        else:
            print("Thank You! For Using BhokLagyo!!!!")
            break
    
ask_hungryman()