import os
import time


def main():
    return("Hello world!\n")

if __name__ == '__main__':
    file_path = os.path.dirname(os.path.dirname(__file__))+'/output/log.txt'
    with open(file_path, 'a') as f:
        for i in range(1,5):            
            print(f'Writing in {file_path}')
            f.write(main())
            i = i+1
            time.sleep(1)
    with open(file_path, 'r') as f:
        print(f.readlines())
