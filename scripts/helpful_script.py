from distutils.command.config import config
from typing import NewType
from brownie import accounts, config, network

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]

def get_accounts():
  if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or FORKED_LOCAL_ENVIRONMENTS:
    return accounts[0]
  else:
    return accounts.add(config["wallets"]["from_key"])