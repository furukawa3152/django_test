from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import requests

# hagakureTopページ
def index(request):
    return render(request, 'index.html')

# hagakure参加者の声ページ
def voice(request):
    return render(request, 'voice.html')


# transformersagaページ
def saga_bot(request):
    return render(request, 'saga_bot.html')

# API
@require_http_methods(["POST"])
def trans_sagaben(request):
    user_message = request.POST.get('message')
    try:
        response = requests.post("https://9z6fdi7vqg.execute-api.ap-northeast-1.amazonaws.com/default/Transformer_saga", # グローバルIPとポート番号を修正
                                 json={"message": user_message})
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        return render(request, "saga_bot.html", {"messages": [{"sender": "bot", "text": "An error occurred while processing your request. Please try again later."}]})
    else:
        return render(request, "saga_bot.html", {"messages": response.json()["messages"]})
    
# T5説明ページ
def indext5explain(request):
    return render(request, 'indext5explain.html')