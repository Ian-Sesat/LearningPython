import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics", help="first subject")
    parser.add_argument("--chemistry", help="second subject")
    parser.add_argument("--maths", help="third subject")

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.maths)

    n1=int(args.physics)
    n2=int(args.chemistry)
    n3=int(args.maths)
    
    result = None
    if args.physics and args.chemistry and args.maths != None:
        result=(n1+n2+n3)/3
    print('Average mark: {}'.format(result))
