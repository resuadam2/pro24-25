twit = input("Introduce un twit: ")

if len(twit) > 280:
    print("El twit es demasiado largo")
else:
    print("Twit correcto")
    
"""
twiteable = len(twit) <= 280
print(f"El twit es twiteable: {twiteable}")
"""