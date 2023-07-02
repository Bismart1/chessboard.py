def can_queen_take_king(king_square, queen_square):
    king_file, king_rank = king_square
    queen_file, queen_rank = queen_square
    if king_file == queen_file or king_rank == queen_rank or abs(ord(king_file) - ord(queen_file)) == abs(int(king_rank) - int(queen_rank)):
        return "Y"
    else:
        return "N"
num_test_cases = int(input())
for _ in range(num_test_cases):
    king_square, queen_square = input().split()
    result = can_queen_take_king(king_square, queen_square)
    print(result, end=" ")
