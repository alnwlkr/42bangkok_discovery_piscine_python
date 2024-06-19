from checkmate import checkmate
import sys

def main():
    f_lst = sys.argv
    f_lst.pop(0)
    nof = len(f_lst)
    # print(f_lst)
    for name in f_lst:
        try:
            f_temp = open(name,"r")
            # print(f_temp)
            # print(f_temp.read())
            checkmate(f_temp.read())
        except:
            print('Error')
        

if __name__ == "__main__":
    main()

# python3 main.py valid_board.chess | cat -e
# python3 main.py valid_board.chess valid_board2.chess | cat -e
# python3 main.py invalid_board.chess | cat -e
# python3 main.py invalid_board.chess valid_board2.chess | cat -e