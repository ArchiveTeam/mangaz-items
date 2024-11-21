import sys


def main(item_type: str, start: int, stop: int):
    with open('{}_{}-{}.txt'.format(item_type, start, stop), 'w') as f:
        for i in range(int(start), int(stop)+1):
            f.write('{}:{}\n'.format(item_type, i))

if __name__ == '__main__':
    main(*sys.argv[1:])

