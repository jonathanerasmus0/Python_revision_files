from argparse import Argumentparser, Namespace

parser = Argumentparser()

parser.add_argument("echo", help="echos the given string")

args : Namespace = parser.parse_args()

print(args.echo)
