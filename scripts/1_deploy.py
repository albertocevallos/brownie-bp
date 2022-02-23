from brownie import (
    convert,
    accounts,
    network,
    interface,
)
import os
import sys
import signal
from datetime import datetime
from rich.console import Console
console = Console()


def main():
    # setup
    dev = connect_account()

    # args

    # deploy

    # wireup



def connect_account():
    console.print(f"\nnetwork: {network.show_active()}")
    accts = accounts.load()
    console.print("\n[green]Accounts:[/green]")
    for acct in accts:
        console.print(f"\t{acct}")
    name = input("\nEnter account name: ").strip()
    owner = accounts.load(name)
    return (name, owner)