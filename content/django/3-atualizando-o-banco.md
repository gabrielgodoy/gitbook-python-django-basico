# Atualizando o banco de dados

Para cada novo app criado, ou quando você altera models existentes é preciso atualizar o banco de dados

```bash
# Crie os arquivos de migração com as mudanças que foram feitas nos models (comandos SQL)
python manage.py makemigrations [APP_NAME]
```

```bash
# Para visualizar os comandos que o makemigrations criou escreva
python manage.py sqlmigrate [APP_NAME] [MIGRATION_ID]
```

```bash
# Aplique a migração criada pelo makemigrations
python manage.py migrate
```