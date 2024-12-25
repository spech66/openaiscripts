import os
import sys
import asyncio
from datetime import datetime
from azure.identity import ClientSecretCredential, DeviceCodeCredential
from msgraph.graph_service_client import GraphServiceClient
from kiota_abstractions.api_error import APIError
from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv()

# Values from app registration
tenant_id = os.getenv("MS_GRAPH_TENANT_ID")
client_id = os.getenv("MS_GRAPH_CLIENT_ID")
client_secret = os.getenv("MS_GRAPH_CLIENT_SECRET")

# Application Permissions - User.Read.All -> No me endpoints and user id needed
scopes = ['https://graph.microsoft.com/.default']
credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
graph_client = GraphServiceClient(credential, scopes)

# Delegate Permissions - User.Read -> me endpoint without user id
# credential = DeviceCodeCredential(client_id, tenant_id = tenant_id)
# graph_client = GraphServiceClient(credential, ["User.Read", "Tasks.Read"])

# async def get_current_user():
#     user = await graph_client.me.get()
#    print(user)

async def get_current_user():
    try:
        user_principal_name = os.getenv("MS_ENTRA_ID_USER_PRINCIPAL_NAME")
        user = await graph_client.users.by_user_id(user_principal_name).get()
        if user:
            print(f'User: {user.display_name}')
    except APIError as e:
        print(f'Error: {e.error.message}')
        
asyncio.run(get_current_user())
