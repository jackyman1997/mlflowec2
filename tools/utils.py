import argparse

def argparse_to_dict(argparse_namespace: argparse.Namespace) -> dict:
    return vars(argparse_namespace)