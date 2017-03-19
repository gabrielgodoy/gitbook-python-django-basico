Se você está no mac você pode instalar o Python com o [brew](https://brew.sh/)

```bash
brew install python3
```

Depois de instalar a versão correta para o seu sistema operacional, você precisará certificar-se de que ele está configurado corretamente. Abra um terminal e digite:

```
python3
```

Você deve ver algo parecido com o seguinte:

```bash
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Este é o shell interativo do Python. Pressione `CTRL + D` para sair desse shell

---

## Configurando o ambiente

Para evitar poluir nosso escopo global com pacotes de Python, vamos usar um ambiente virtual para armazenar nossos pacotes para esse projeto específico. O gerenciador de ambiente virtual que vamos usar é o [virtualenv](https://virtualenv.pypa.io/en/stable/). E junto com ele vamos usar o [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) que é uma extensão do virtualenv que tornam os comandos do virtualenv muito mais fáceis através de atalhos.

Vamos usar o gerenciador de pacotes do Python `pip` para instalar este e outros pacotes como o Django, que precisaremos mais tarde. Primeiro, vamos instalar o virtualenv e o virtualenvwrapper.

```bash
pip install virtualenv
pip install virtualenvwrapper
```

Agora é preciso configurar as váriaves de ambiente no seu sistema operacional. Caso esteja no Mac, é preciso adicionar algumas linhas no arquivo de configuração de shell que você usa. **Mude os caminhos de acordo com as suas configurações.**

Edite o arquivo de acordo com o shell que você usa, Exemplo: `~/.bashrc`, `~/.zshrc`, etc...

```bash
# virtualenvwrapper

# Every virtualenv created will use this python
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3

# Path to virtualenv executable
export VIRTUALENVWRAPPER_VIRTUALENV=/Library/Frameworks/Python.framework/Versions/3.6/bin/virtualenv

# Path to virtualenvs
export WORKON_HOME=$HOME/.virtualenvs

# Path to virtualenv project folders
export PROJECT_HOME=$HOME/Documents/python-venv-projects

# Runs virtualenvwrapper script
source /Library/Frameworks/Python.framework/Versions/3.6/bin/virtualenvwrapper.sh
```

Caso tenha dúvidas na configuração do virtualenvwrapper, ou precise instalar em outros sistemas operacionais, [veja mais detalhes aqui](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

Depois de instalados e configurados, crie um ambiente para o seu projeto:

```
mkproject [NOME_DO_PROJETO]
```

Esse comando acima cria um novo virtualenv na pasta definida em `WORKON_HOME`, e um novo diretório em `PROJECT_HOME`. Esse comando também irá ativar o ambiente virtual, e já irá te levar para a pasta do projeto que você acabou de criar.

---

## Instalando o Django

Com o seu ambiente virtual ativado, digite:

```bash
pip install django
```
