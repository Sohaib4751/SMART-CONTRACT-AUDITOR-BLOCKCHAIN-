import { ethers } from "ethers";

const contractAddress = "0xYourContractAddressHere"; // 🔁 Replace with real one
const abi = [/* Your contract ABI here */];

export const getContract = () => {
  if (window.ethereum) {
    const provider = new ethers.BrowserProvider(window.ethereum);
    const signer = provider.getSigner();
    return new ethers.Contract(contractAddress, abi, signer);
  } else {
    console.error("Please install MetaMask!");
  }
};
