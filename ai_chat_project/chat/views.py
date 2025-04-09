from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from openai import OpenAI

client = OpenAI(
    base_url=settings.OPENAI_BASE_URL,
    api_key=settings.OPENAI_API_KEY,
)

def chat_view(request):
    return render(request, 'chat/chat.html')

def chat_api(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": request.build_absolute_uri('/'),
                "X-Title": "AI Chat Project",
            },
            model=settings.DEFAULT_MODEL,
            messages=[{
                "role": "user",
                "content": message,
            }]
        )
        
        return JsonResponse({
            'response': completion.choices[0].message.content
        })
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
