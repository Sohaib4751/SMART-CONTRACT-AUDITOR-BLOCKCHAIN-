// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Vulnerable {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function withdraw() public {
        require(tx.origin == owner);  // 🚨 bad practice: tx.origin
        payable(msg.sender).transfer(address(this).balance);
    }

    receive() external payable {}
}
