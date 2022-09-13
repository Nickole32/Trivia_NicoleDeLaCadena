print("Bienvenido a mi trivia sobre computación")
print("Pondremos a prueba tus conocimientos")

nombre = input("Ingresa tu nombre:")

print("\nHola", nombre ,"responde a las siguientes preguntas escribiendo la letra de la alternativa y presionado 'Enter' para enviar tu respuesta\n")
print("1) ¿Cómo se llama el personaje principal de One Piece?")
print("a) Zoro")
print("b) Nami")
print("c) Luffy")
print("d) Robin")
print("e) Ussop")

respuesta_1 = input("\nTu respuesta:")
if respuesta_1 == "c":
    print("Muy bien")

while respuesta_1 not in ("c"):
  respuesta_1 = input("Incorrecto. Ingresa nuevamente tu respuesta:")

print("\n2) ¿Cuál es el nombre del último barco de Luffy?")
print("a) Thousand Sunny")
print("b) Going Luffy-senpai")
print("c) Naglfar")
print("d) Hakobune")
print("e) Going Merry")

respuesta_2 = input("\nTu respuesta:")
if respuesta_2 == "a":
    print("Muy bien")

while respuesta_2 not in ("a"):
  respuesta_2 = input("Incorrecto. Ingresa nuevamente tu respuesta:")

print("\nCulminaste con éxito las preguntas. ¡Gracias por participar!")