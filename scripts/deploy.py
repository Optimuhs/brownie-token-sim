from brownie import accounts,  myToken, network
from scripts.helpful_script import get_accounts
import os
from dotenv import load_dotenv

load_dotenv()

def deploy_token():
  account = get_accounts()
  token = myToken.deploy({'from': account})


def main():
  deploy_token()