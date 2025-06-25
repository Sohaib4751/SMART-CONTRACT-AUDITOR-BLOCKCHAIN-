// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AuditResults {
    struct Audit {
        address submitter;
        string contractAddress; // or file hash if local
        string aiSummaryHash;
        string timestamp;
    }

    Audit[] public audits;

    event AuditSubmitted(address indexed submitter, string contractAddress, string aiSummaryHash, string timestamp);

    function submitAudit(string memory contractAddr, string memory hash, string memory timestamp) public {
        audits.push(Audit(msg.sender, contractAddr, hash, timestamp));
        emit AuditSubmitted(msg.sender, contractAddr, hash, timestamp);
    }

    function getAuditCount() public view returns (uint) {
        return audits.length;
    }

    function getAudit(uint index) public view returns (Audit memory) {
        require(index < audits.length, "Invalid index");
        return audits[index];
    }
}
