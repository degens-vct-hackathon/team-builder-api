import zipfile
import boto3
import json
import os
from pathlib import Path
import urllib.request
import hashlib
import base64

def main():
    while True:
        print('1. Pull remote functions')
        print('2. Push local functions')
        print('3. Exit')
        choice = input('Enter your choice: ')
        choice, *options = choice.split()
        if choice == '1':
            if '-y' in options or '-f' in options:
                pull_remote_functions(confirmed=True)
            else:
                pull_remote_functions()
        elif choice == '2':
            if '-y' in options or '-f' in options:
                push_local_functions(confirmed=True)
            else:
                push_local_functions()
        elif choice == '3':
            break
        else:
            print('Invalid choice!')

def zip_lambda_function(function):
    with zipfile.ZipFile(f'{function}.zip', 'w') as z:
        root = Path(__file__).parent / 'functions' / function
        for curr, _, files in os.walk(root):
            curr = Path(curr)
            for file in files:
                f = curr / file
                z.write(f, f.relative_to(root))

def update_lambda_function(function):
    zip_lambda_function(function)
    client = boto3.client('lambda', region_name = os.getenv("AWS_REGION"))
    response = client.update_function_code(
        FunctionName=function,
        ZipFile=open(f'{function}.zip', 'rb').read(),
    )
    os.remove(f'{function}.zip')
    print(json.dumps(response, indent=2))

def get_local_functions():
    return [f.name for f in (Path(__file__).parent / 'functions').iterdir()]

def fetch_lambda_functions():
    client = boto3.client('lambda', region_name = os.getenv("AWS_REGION"))
    response = client.list_functions()
    return [f['FunctionName'] for f in response['Functions']]

def pull_remote_function():
    client = boto3.client('lambda', region_name = os.getenv("AWS_REGION"))
    response = client.get_function(FunctionName=function)
    with urllib.request.urlopen(response['Code']['Location']) as f:
        with open(f'{function}.zip', 'wb') as z:
            z.write(f.read())
    with zipfile.ZipFile(f'{function}.zip', 'r') as z:
        z.extractall(Path(__file__).parent / 'functions' / function)
    os.remove(f'{function}.zip')

def pull_remote_functions(confirmed=False):
    local_functions = get_local_functions()
    remote_functions = fetch_lambda_functions()
    client = boto3.client('lambda', region_name = os.getenv("AWS_REGION"))
    for function in remote_functions:
        if function not in local_functions:
            inp = 'y' if confirmed else input(f'Pull {function} (y/n)? ')
            if inp.lower() == 'y':
                pull_remote_function(function)
                print(f'{function} pulled!')
            else:
                print(f'{function} skipped!')

def push_local_functions(confirmed=False):
    for function in get_local_functions():
        inp = 'y' if confirmed else input(f'Push {function} (y/n)? ')
        if inp.lower() == 'y':
            update_lambda_function(function)
            print(f'{function} pushed!')
        else:
            print(f'{function} skipped!')

if __name__ == '__main__':
    main()
