from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
import requests

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Preparar dados para enviar à API
            data = {
                'nome': form.cleaned_data['nome'],
                'senha': form.cleaned_data['senha']
            }

            # Enviar formulário para a API (exemplo)
            api_response = requests.post('https://api-python-tarde-37668b622097.herokuapp.com/login', json=data)
            # Lógica de tratamento da resposta da API#joga para view index

            if api_response.status_code == 200:
                # Se a resposta da API foi bem-sucedida (status code 200)
                # Exemplo: receber dados da API (JSON)
                api_data = api_response.json()
                sucess_message = 'login bem sucedido.'
                # Exemplo: passar os dados para a próxima página
                return render(request, 'index.html', {'api_data': api_data,'sucess_message':sucess_message})

            else:
                # Se a resposta da API não foi bem-sucedida
                # Exemplo: exibir mensagem de erro para o usuário
                error_message = 'Falha ao processar o formulário. Tente novamente.'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})

            
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Enviar formulário para a API (exemplo)
            api_response = requests.post('https://api-python-tarde-37668b622097.herokuapp.com/register', data=form.cleaned_data)
            # Lógica de tratamento da resposta da API#joga para view index
            if api_response.status_code == 200:
                # Se a resposta da API foi bem-sucedida (status code 200)
                # Exemplo: receber dados da API (JSON)
                api_data = api_response.json()

                # Exemplo: passar os dados para a próxima página
                return render(request, 'index.html', {'api_data': api_data})

            else:
                # Se a resposta da API não foi bem-sucedida
                # Exemplo: exibir mensagem de erro para o usuário
                error_message = 'Falha ao processar o formulário. Tente novamente.'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})