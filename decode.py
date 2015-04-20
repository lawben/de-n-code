import sys
import argparse
from operator import xor


# Helper functions

def ord_to_string(char_values):
    """Convert list of int values to corresponding string."""
    return ''.join(chr(c) for c in char_values)


def string_to_ord(string):
    """Convert string to corresponding list of int values."""
    return [ord(char) for char in string]


def get_function_by_name(name):
    """Convert command line argument to function."""
    function_name = name + 'ed'
    return globals()[function_name]


# En-/decoding functionality

def decode(cipher, decode_function, range_top=256, range_bottom=0):
    cipher_values = string_to_ord(cipher)
    for decode_value in range(range_bottom, range_top):
        decoded_values = decode_function(cipher_values, decode_value)
        print ord_to_string(decoded_values)


def encode(string, encode_function, encode_value):
    string_values = string_to_ord(string)
    encoded_values = encode_function(string_values, encode_value)
    print ord_to_string(encoded_values)


def xored(char_values, xor_value):
    return [xor(c, xor_value) for c in char_values]


def caesared(char_values, shift_value):
    # % 256 for printable ASCII range
    return [(c + shift_value) % 256 for c in char_values]


def main(args):
    method = get_function_by_name(args.method)
    if args.decode:
        decode(args.string, method, args.top, args.bottom)
    elif args.encode:
        if args.key is not None:
            encode(args.string, method, args.key)
        else:
            sys.exit("A numeric key is required for encoding. Option -k/--key")
    else:
        sys.exit("No en-/decoding could be executed!")


if __name__ == '__main__':
    tool_description = "Small tool to en-/decode with XOR or Caesar cipher."
    parser = argparse.ArgumentParser(description=tool_description)
    group = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument('string',
                        help="The plain text or cipher string to be used.")

    parser.add_argument('method',
                        help="Select 'xor' or 'caesar' to use the \
                        corresponding method.",
                        choices=['xor', 'caesar'])

    group.add_argument('-d', '--decode',
                       help="Selct to decode a cipher text.",
                       action='store_true')

    group.add_argument('-e', '--encode',
                       help="Select to encode a plain text.",
                       action='store_true')

    parser.add_argument('-t', '--top',
                        help="Set top of range for decoding. \
                              Default: %(default)s",
                        type=int,
                        default=256)

    parser.add_argument('-b', '--bottom',
                        help="Set bottom of range for decoding. \
                              Default: %(default)s",
                        type=int,
                        default=0)

    parser.add_argument('-k', '--key',
                        help="Set key value for encoding.",
                        type=int)

    args = parser.parse_args()
    main(args)
