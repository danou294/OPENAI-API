# Assurez-vous d'avoir la bibliothèque openai installée
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Initialisez votre clé d'API OpenAI
openai.api_key = 'YOUR-API-KEY'
@csrf_exempt
def chat(request):
    if request.method == 'POST':
        # Récupérer le corps de la requête JSON
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        # Récupérer le message envoyé par l'utilisateur depuis le corps JSON
        user_message = body_data.get('message')

        # Imprimer le message pour le débogage
        print("Message de l'utilisateur:", user_message)

        # Appeler l'API ChatGPT pour obtenir une réponse
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Utilisez un modèle valide et pris en charge
            prompt=user_message,
            max_tokens=50  # ou toute autre configuration souhaitée
        )

        # Récupérer la réponse de l'API et la renvoyer au client sous forme de JSON
        chat_response = response.choices[0].text.strip()
        print("Réponse de l'API:", chat_response)
        return JsonResponse({'response': chat_response})

    # Gérer les autres méthodes HTTP (par exemple, GET)
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)