# Note et Idea
---
<br>

- **homeopathy**
- **nutriton**
- **physical exercise**
- **meditation yoga**
- ** **
- ** **



## Sources:

https://www.lovethegarden.com/uk-en/article/plants-benefits

https://leroutardresistant.com/wp-content/uploads/2022/03/remedes-naturels-maison.pdf

https://gomedica.org/remedes-naturels-guide/#78_remedes_naturels_pour_les_maux_de_tous_les_jours_Un_guide_de_guerison_holistique



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


































---
---
---
---
---
---
---

to keep history

from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")
chat = client.chats.create(model="gemini-2.0-flash")

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)


faster

from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=["Explain how AI works"]
)
for chunk in response:
    print(chunk.text, end="")