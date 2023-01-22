import argparse
from utils.providers import get_provider_from_uri

parser = argparse.ArgumentParser(
    prog="Arbitrage Scanner stream mode",
    description="The project enables users find arbitrage opportunities in evm blockchains in stream mode",
)


parser.add_argument("--pairs", type=str, default=None, required=True)
parser.add_argument("--provider-uri", type=str, default=None, required=True)

args = parser.parse_args()

batch_w3 = get_provider_from_uri(args.provider_uri, batch=True)

# <YOUR CODE GOES HERE>
# You can use any libraries you want
