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
import requests

load_dotenv()

# Values from app registration
tenant_id = os.getenv("MS_GRAPH_TENANT_ID")
client_id = os.getenv("MS_GRAPH_CLIENT_ID")
client_secret = os.getenv("MS_GRAPH_CLIENT_SECRET")

user_principal_name = os.getenv("MS_ENTRA_ID_USER_PRINCIPAL_NAME")

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
        user = await graph_client.users.by_user_id(user_principal_name).get()
        if user:
            print(f'User: {user.display_name}')
            return user.id
    except APIError as e:
        print(f'Error: {e.error.message}')

# https://learn.microsoft.com/en-us/graph/tutorials/python-app-only?tabs=aad&tutorial-step=3
async def get_app_only_token():
    graph_scope = 'https://graph.microsoft.com/.default'
    access_token = credential.get_token(graph_scope)
    return access_token.token

async def get_todo_list():
    try:
        todo_lists = await graph_client.users.by_user_id(user_principal_name).todo.lists.get()
        # ERROR => https://github.com/microsoftgraph/msgraph-sdk-python/issues/910
        # :-(
                
        # todo_lists = await graph_client.me.todo.lists.by_todo_task_list_id('todoTaskList-id').get()
        
        # result = await graph_client.me.todo.lists.by_todo_task_list_id('todoTaskList-id').tasks.get()
        print(todo_lists)
    except APIError as e:
        print(f'Error: {e.error.message}')

async def get_todo_list_api(token, userid):
    # create graph api request directly as the sdk is not working
    # GET /users/{id|userPrincipalName}/todo/lists
    print(f'User ID: {userid}')
    url = f'https://graph.microsoft.com/v1.0/users/{userid}/todo/lists'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    print(response.json())

userid = asyncio.run(get_current_user())
token = asyncio.run(get_app_only_token())
#asyncio.run(get_todo_list())
asyncio.run(get_todo_list_api(token, userid))

