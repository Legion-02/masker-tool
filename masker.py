import argparse
import hashlib
import sys
from banner import print_banner

def hash_string(algorithm, text):
    try:
        h = hashlib.new(algorithm)
        h.update(text.encode("utf-8"))
        return h.hexdigest()
    except ValueError:
        return f"Error: Unsupported algorithm '{algorithm}'"

def verify_hash(algorithm, text, hash_value):
    return hash_string(algorithm, text) == hash_value

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Masker: Simple hashing & verifying tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Hash command
    hash_parser = subparsers.add_parser("hash", help="Generate hash for input text")
    hash_parser.add_argument("algorithm", help="Hash algorithm (e.g., md5, sha256, sha512)")
    hash_parser.add_argument("text", help="Input text to hash")

    # Verify command
    verify_parser = subparsers.add_parser("verify", help="Verify text against a given hash")
    verify_parser.add_argument("algorithm", help="Hash algorithm")
    verify_parser.add_argument("text", help="Input text")
    verify_parser.add_argument("hash", help="Hash value to compare against")

    args = parser.parse_args()

    if args.command == "hash":
        print(hash_string(args.algorithm, args.text))
    elif args.command == "verify":
        result = verify_hash(args.algorithm, args.text, args.hash)
        print("Match" if result else "No Match")

if __name__ == "__main__":
    main()
