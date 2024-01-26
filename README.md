# Backup do Obsidian para o Google Drive

Este script em Python automatiza o processo de backup de notas do Obsidian para o Google Drive. Ele garante que suas notas do Obsidian estejam sincronizadas e salvas em uma pasta específica no Google Drive.

## Pré-requisitos

Antes de executar o script, certifique-se de ter as bibliotecas Python necessárias instaladas. Você pode instalá-las usando:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```
### Criar Token de acesso:
1. Crie um Projeto no Console de Desenvolvedores do Google:
- Acesse [Google Cloud Console](https://console.cloud.google.com/).
- Crie um novo projeto (ou selecione um projeto existente).

2. Ativar a API do Google Drive:
- No Console de Desenvolvedores do Google, navegue até "API e Serviços" > "Biblioteca".
- Pesquise e ative a "API de Drive API".

3. Crie Credenciais para a API:   
- No Console de Desenvolvedores, vá para "APIs e Serviços" > "Credenciais".
- Crie credenciais de "ID do Cliente OAuth" para um aplicativo da área de trabalho. Isso resultará em um arquivo JSON de credenciais.

## Configuração

Antes de executar o script, é necessário configurar alguns parâmetros diretamente no script:

1. **OBSIDIAN_NOTES_PATH:** O caminho local onde suas notas do Obsidian estão armazenadas.
2. **GOOGLE_DRIVE_FOLDER_ID:** O ID da pasta no Google Drive onde você deseja armazenar seus backups.
3. **CREDENTIALS_FILE:** O nome do arquivo para armazenar as credenciais da API do Google Drive.

Certifique-se de substituir essas configurações pelos seus caminhos e IDs de pasta específicos.

## Como Executar

1. Certifique-se de ter o Python instalado no seu sistema.
2. Instale as bibliotecas necessárias conforme mencionado na seção "Pré-requisitos".
3. Execute o script:

```bash
python seu_nome_de_script.py
```

O script fará a autenticação com o Google Drive, listará os arquivos na pasta especificada e fará o upload de quaisquer novas notas do Obsidian que ainda não estejam presentes no Google Drive.

## Observações

- O script utiliza OAuth 2.0 para autenticação e armazena as credenciais em um arquivo token.json.
- A API do Google Drive é utilizada para interagir com o Google Drive para listagem de arquivos e upload.

Sinta-se à vontade para personalizar o script conforme suas necessidades específicas ou integrá-lo ao seu fluxo de trabalho.
