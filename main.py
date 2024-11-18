saludo = input("Hola.")

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "RIZZ": "Tener charisma y asi atraer a la gente",
            "SIGMA": "Alguien independiente, carismático y asombroso",
            "AURA": "Que tan bien te sientes en ese momento"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("No se encuentra esa palabra")
