from audioop import add
from webbrowser import get
from brownie import MyToken, accounts, exceptions, network
import pytest
from scripts.helpful_script import get_accounts, LOCAL_BLOCKCHAIN_ENVIRONMENTS, FORKED_LOCAL_ENVIRONMENTS
from scripts.deploy import deploy_token

def test_deploy():
  if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or FORKED_LOCAL_ENVIRONMENTS:
    # Arrange
    account = accounts[0]
    # Act
    my_token = deploy_token(account)
    #my_token = MyToken.deploy({"from": account}) 
    # Assert
    assert account == my_token.owner()
  else:
     pytest.skip("Only for locala tests")

def test_token_mint():
  # Arrange
  tokens = 100
  account = accounts[0]
  account1 = accounts[1]
  # Act
  my_token = deploy_token(account)
  #my_token = MyToken.deploy({"from": account})

  my_token.mintTokens(tokens, account)
  my_token.mintTokens(tokens, account1)
  # Assert
  assert tokens == my_token.balanceOf(account)
  assert tokens == my_token.balanceOf(account1)

def test_batch_mint():
  # Arrange
  tokens = 100
  acc_list = get_accounts(5)
  # Act
  my_token = deploy_token(acc_list[0])
  #my_token = MyToken.deploy({"from": })
  add_accounts(my_token, acc_list)
  my_token.batchMint(tokens)
  
  # Assert
  assert tokens == my_token.balanceOf(acc_list[1])
  assert tokens == my_token.balanceOf(acc_list[2])
  assert tokens == my_token.balanceOf(acc_list[3])
  assert tokens == my_token.balanceOf(acc_list[4])

def add_accounts(contract, acc_list):
  for i in range(len(acc_list)):
    contract.addToUsersArr(acc_list[i])

def test_transfer_tokens():
  # Arrange
  tokens = 100
  acc_list = get_accounts(5)
  # Act
  my_token = deploy_token(acc_list[0])
  #my_token = MyToken.deploy({"from": acc_list[0]})
  add_accounts(my_token, acc_list)
  my_token.batchMint(tokens)
  my_token.transferTokens(acc_list[2], acc_list[1], 20)
  my_token.transferTokens(acc_list[3], acc_list[4], 50)
  # Assert
  assert tokens - 20 == my_token.balanceOf(acc_list[1])
  assert tokens + 20 == my_token.balanceOf(acc_list[2])
  assert tokens + 50 == my_token.balanceOf(acc_list[3])
  assert tokens - 50 == my_token.balanceOf(acc_list[4])

def test_only_owner_batch_mint():
  acc_list = get_accounts(2)
  owner_acc = acc_list[0]
  bad_actor = acc_list[1]
  my_token = deploy_token(owner_acc)
  my_token = MyToken.deploy({"from": owner_acc})
  with pytest.raises(exceptions.VirtualMachineError):
    my_token.batchMint(100, {"from": bad_actor})