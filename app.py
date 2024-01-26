import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Configurações
OBSIDIAN_NOTES_PATH = r"caminho\pasta\obsidian"
GOOGLE_DRIVE_FOLDER_ID = "id da pasta do drive"
CREDENTIALS_FILE = "token.json"

# Configuração da API do Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate_google_drive():
    creds = None
    if os.path.exists(CREDENTIALS_FILE):
        creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open(CREDENTIALS_FILE, 'w') as token:
            token.write(creds.to_json())

    return creds

def list_drive_files(folder_id):
    creds = authenticate_google_drive()
    drive_service = build('drive', 'v3', credentials=creds)

    query = f"'{folder_id}' in parents"
    results = drive_service.files().list(q=query).execute()
    files = results.get('files', [])

    return files

def upload_to_google_drive(file_path, folder_id):
    creds = authenticate_google_drive()
    drive_service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]
    }

    media = MediaFileUpload(file_path,
                            mimetype='text/plain',
                            resumable=True)

    request = drive_service.files().create(body=file_metadata,
                                           media_body=media,
                                           fields='id')

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f'Enviado {int(status.progress() * 100)}%')

    print(f'Envio completo! ID do arquivo: {response.get("id")}')

def main():
    # Listar arquivos no Google Drive
    drive_files = list_drive_files(GOOGLE_DRIVE_FOLDER_ID)
    drive_file_names = {file['name'] for file in drive_files}

    # Listar arquivos no Obsidian Vault
    obsidian_files = [f for f in os.listdir(OBSIDIAN_NOTES_PATH) if os.path.isfile(os.path.join(OBSIDIAN_NOTES_PATH, f))]

    # Identificar arquivos que não estão no Google Drive e fazer o upload
    files_to_backup = [obsidian_file for obsidian_file in obsidian_files if obsidian_file not in drive_file_names]

    if not files_to_backup:
        print("Nenhum backup necessário. Todos os arquivos estão atualizados no Google Drive.")
        return

    for obsidian_file in files_to_backup:
        obsidian_file_path = os.path.join(OBSIDIAN_NOTES_PATH, obsidian_file)
        upload_to_google_drive(obsidian_file_path, GOOGLE_DRIVE_FOLDER_ID)

    print("Backup concluído!")

if __name__ == "__main__":
    main()