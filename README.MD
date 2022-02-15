Follow these Steps to make thousands of custom NFTs:
1. Clone the repo by running `git clone https://github.com/bcorbs/NFT-Art_Gen`
2. Enter the downloaded directory by typing `cd NFT-Art_Gen`
3. Install the dependencies by running `pip install -r requirements.txt`
4. Add all your layer files in the 'traits' folder. They should be separated in different layer folders.
5. Add the probability of each trait. You can do this by adding the number after a '#' in the file name. For example, if the 'Background' layer had two files called 'Black#50.png' and 'White#50.png' then there would be a 50% chance of each being selected.
6. Edit the `config.py` file with your settings.
7. Run `generator.py`

:warning: **Important:** you can't use the traits files provided in the repo
