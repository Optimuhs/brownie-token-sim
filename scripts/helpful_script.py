from distutils.command.config import config
from brownie import accounts, config, network

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]

def get_accounts(num_acc):
  if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or FORKED_LOCAL_ENVIRONMENTS:
    acc_list = []
    for i in range(num_acc):
      acc_list.append(accounts[i])
      
    return acc_list
  else:
    return accounts.add(config["wallets"]["from_key"])