import pstats # this tool lets us read the output from cProfile

def main():
    '''read in some prfile data nad display it'''
    p = pstats.Stats('profile_output')
    p.print_stats()

if __name__ == '__main__':
    main()