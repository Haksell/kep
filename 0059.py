def max_2(*args):
    args.remove(max(args))
    return max(args)
