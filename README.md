# Brownie Boilerplate

## Installation and Setup

1. Download the code with `git clone URL_FROM_GITHUB`

2. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html) & [Ganache-CLI](https://github.com/trufflesuite/ganache-cli), if you haven't already.

3. Install smart contract dependencies

```
brownie pm install OpenZeppelin/openzeppelin-contracts@4.5.0
```

4. Install node dependencies (optional)

```
npm i
```

5. Configure Python virtual environment
   Run the following command once per computer:

```
pip3 install virtualenv
```

Run the following command per repo:

```
virtualenv venv
```

Run the following command when opening a new terminal:

```
source venv/bin/activate
pip3 install -r requirements.txt
```
