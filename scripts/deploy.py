from brownie import MyToken
from scripts.helpful_script import get_accounts
from dotenv import load_dotenv

load_dotenv()

def deploy_token(account):
  token = MyToken.deploy({'from': account})
  return token

def main():
  deploy_token()