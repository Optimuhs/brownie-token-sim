// SPDX-Licence-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract myToken {

  struct Set{
    address[] users;
    mapping(address => bool) userAdded;
    mapping(address => uint256) userTokenMap;
  }
  
  Set userSet;

  uint256 public totalSupply = 100000;
  uint256 public releasedSupply = 0;
  uint256 public batchTokens = 0;
  address public owner;

  constructor () public {
    owner = msg.sender;
  }

  function mintTokens(uint256 _amount, address _user) public {
    require(releasedSupply + _amount <= totalSupply);
    userSet.userTokenMap[_user] += _amount;
    if(userSet.userAdded[_user] != true){
      userSet.userAdded[_user] = true;
      userSet.users.push(_user);
    }
  }
  
  function addToUsersArr(address _user) public{
    require(userSet.userAdded[_user] != true);
    userSet.userAdded[_user] = true;
    userSet.users.push(_user);
  }

  function batchMint(uint256 _amount) onlyOwner payable public {
    for(uint256 j = 0; j < userSet.users.length; j++){
      mintTokens(_amount, userSet.users[j]);
      batchTokens += _amount;
    }
  }

  function transferTokens(address _receiver, address _user, uint256 _amount) public{
    require(_user != _receiver, "Cannot send tokens to yourself");
    require(_amount > 0, "Amount of tokens being sent needs to be more than 0");
    userSet.userTokenMap[_user] -= _amount;
    userSet.userTokenMap[_receiver] += _amount;
    if (userSet.userAdded[_receiver] != true){
      userSet.userAdded[_receiver] = true;
      userSet.users.push(_receiver);
    }
  }

  function balanceOf(address user) public view returns(uint256){
    return(userSet.userTokenMap[user]);
  }

  modifier onlyOwner {
    require(owner == msg.sender);
    _;
  }


}