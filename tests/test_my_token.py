from webbrowser import get
from brownie import myToken, accounts, exceptions, network
import pytest
from scripts.helpful_script import get_accounts

def test_deploy():
  # Arrange
  account = accounts[0]
  # Act
  my_token = myToken.deploy({"from": account}) 
  # Assert
  assert account == my_token.owner()

def test_token_mint():
  # Arrange
  tokens = 100
  account = accounts[0]
  account1 = accounts[1]
  # Act
  my_token = myToken.deploy({"from": account})
  my_token.mintTokens(tokens, account)
  my_token.mintTokens(tokens, account1)
  # Assert
  assert tokens == my_token.balanceOf(account)
  assert tokens == my_token.balanceOf(account1)

def test_batch_mint():
  # Arrange
  tokens = 100
  # Act
  my_token = myToken.deploy({"from": accounts[0]})
  add_accounts(my_token)
  my_token.batchMint(tokens)

  # Assert
  assert tokens == my_token.balanceOf(accounts[1])
  assert tokens == my_token.balanceOf(accounts[2])
  assert tokens == my_token.balanceOf(accounts[3])
  assert tokens == my_token.balanceOf(accounts[4])

def add_accounts(contract):
  for i in range(1, 5):
    contract.addToUsersArr(accounts[i])

def test_transfer_tokens():
  # Arrange
  tokens = 100
  # Act
  my_token = myToken.deploy({"from": accounts[0]})
  add_accounts(my_token)
  my_token.batchMint(tokens)
  my_token.transferTokens(accounts[2], accounts[1], 20)
  my_token.transferTokens(accounts[3], accounts[4], 50)
  # Assert
  assert tokens - 20 == my_token.balanceOf(accounts[1])
  assert tokens + 20 == my_token.balanceOf(accounts[2])
  assert tokens + 50 == my_token.balanceOf(accounts[3])
  assert tokens - 50 == my_token.balanceOf(accounts[4])

def test_only_owner_batch_mint():
  owner_acc = get_accounts()
  bad_actor = accounts.add()
  my_token = myToken.deploy({"from": owner_acc})
  with pytest.raises(exceptions.VirtualMachineError):
    my_token.batchMint(100, {"from": bad_actor})