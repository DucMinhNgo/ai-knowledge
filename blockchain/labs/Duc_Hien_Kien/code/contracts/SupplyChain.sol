// SPDX-License-Identifier: MIT
pragma solidity >=0.6.12 <0.9.0;

contract SupplyChainManager {

    // State variables
    mapping(uint256 => Item) public items; // Maps item IDs to Item structs
    uint256 public nextItemId; // Counter for generating unique item IDs
    enum Status { CREATED, SHIPPED, DELIVERED } // Status of the item
    
    struct Item {
        uint256 id; // Unique identifier for the item
        address owner; // Current owner of the item
        string description; // Brief description of the item
        string location; // Current location of the item
        Status status;
    }

    // Constructor
    constructor() {
        nextItemId = 1;
    }

    // Creates a new item with the specified owner and description
    function createItem(string memory _description, address _owner) public {
        items[nextItemId] = Item({
            id: nextItemId,
            owner: _owner,
            description: _description,
            location: "Source",
            status: SupplyChainManager.Status.CREATED
        });
        nextItemId++;
    }

    // Updates the location of an item
    function updateLocation(uint256 _itemId, string memory _newLocation) public {
        require(items[_itemId].owner == msg.sender, "Only the owner can update location");
        items[_itemId].location = _newLocation;
    }

    // Changes the status of an item
    function updateStatus(uint256 _itemId, SupplyChainManager.Status _newStatus) public {
        require(items[_itemId].owner == msg.sender || _newStatus == SupplyChainManager.Status.DELIVERED, "Only the owner or delivery agent can change status to DELIVERED");
        items[_itemId].status = _newStatus;
    }

    // Transfers ownership of an item to a new address
    function transferOwnership(uint256 _itemId, address _newOwner) public {
        require(items[_itemId].owner == msg.sender, "Only the owner can transfer ownership");
        items[_itemId].owner = _newOwner;
    }

    // Gets the details of an item by its ID
    function getItem(uint256 _itemId) public view returns (Item memory) {
        return items[_itemId];
    }

    // Gets the number of items in the contract
    function getItemCount() public view returns (uint256) {
        return nextItemId - 1;
    }
}
