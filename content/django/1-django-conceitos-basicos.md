# Conceitos básicos 

Ao iniciar com o Django se cria um projeto, e dentro deste projeto se criam múltiplos apps.

## Projeto e App, e suas diferenças

App é um pedaço da aplicação web que realiza uma função, como por exemplo uma enquete, um fórum, uma seção de player de vídeo.
  
Projeto é uma coleção de configuração e apps para um site. **Um projeto pode conter múltiplos apps. E um app pode se reutilizado em múltiplos projetos.**

Cada app criado dentro de um projeto Django deve realizar uma coisa específica, e todos os modelos dentro do app devem ter relação.

## Views baseadas em classes

Django possui algumas classes para views que tornam padrões repetitivos mais fáceis de serem feitos, como listar um grupo de objetos do banco de dados, ou mostrar detalhes de um único objeto.

Essas classes servem como atalhos, e elas são importadas da seguinte maneira:

`from django.views import generic`

Algumas das classes de view são **generic.ListView** e **generic.DetailView**

### [Criando models de form para interação do usuário com os dados](https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/)

Models de forms são usados para um usuário realizar as seguintes ações em algum objeto ou objetos: 

- criar (CreateView)
- editar (UpdateView)
- deletar (DeleteView)

Essas views herdam do **SingleObjectTemplateResponseMixin** que usam **template_nome_sufixo** para construir o **template_nome**, baseado no model.

**CreateView** e **UpdateView** usam meuapp/somemodel_form.html

**DeleteView** usa meuapp/somemodel_confirm_delete.html

Se deseja ter templates separados para **CreateView** e **UpdateView**, você pode setar tanto template_name como template_name_suffix na sua classe de view.
