from django.shortcuts import render

from .forms import InputForm

import gpt4all

ptj = gpt4all.GPT4All(
    model_name="wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin",
    allow_download=True,
)


# Create your views here.
def index(request):
    input_form = InputForm()
    context = {
        'input_form': input_form,
    }
    if request.method == 'POST':
        text = InputForm(request.POST)
        message = [
            {"role": "user",
             "content": text}
        ]
        response = gpt4all.chat_completion(message)
        context |= {
            'text': text,
            'response': response,
        }

    return render(request, 'chat/index.html', context)
