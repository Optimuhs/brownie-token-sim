# brownie-token-sim
Simulation of how a token would work

This is a simulation of how a token would work conceptually.

The deployer of the contract will be deemed as the owner and only that address will be able to change the following owner of the contract.

The contract uses a struct to simulate a Set (as they are not present in Solidity at this moment) in order to ensure that a user address has
been given tokens throught mint or by another address. This would allow us to track the amount of tokens held by those who have recieved them
at some point in time.

I have also added a batch mint function so that if desired the users who have been confirmed to have or have had a token at some point will
be able to qualify for the airdropo (batch mint).

Finally it would not be a token without the ability to make transactions, therefore we use mappings to track the transactions and make the 
transfers. 

An improvement would be to add events that would log these transactions, mints, batch mints, and user additions to our set. 
