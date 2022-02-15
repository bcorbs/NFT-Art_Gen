"""
Fill in your information in the configuration variables below. The traits must be types EXACTLY how the folders are labeled
"""

traits = [
    "Background", 
    "Glasses",
    "Headwear",
    "Mouth",
    "Nose",
    "Arm",
    "Eyes"
] # The different layers and the order that they will be used - MUST be same as trait layer folders
imageCount = 1 # Total number of images to create
nameFormat = "NFT #[NUMBER]" # The name of each NFT - '[NUMBER]' will be replaced with the NFT number
description = "" # Description of collection
royalty = 2.5 # Royalty percentage
royaltyAddress = "" # Address to pay the royalties to
collectionName = "" # Name of collection
collectionFamily = "" # Name of family (often same as collection)
symbol = "" # Symbol (often blank)
blockchain = "ETH" # ETH or SOL
