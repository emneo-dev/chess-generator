#!/usr/bin/env python3

import sys
import chess
import random

piece_list = ["R", "N", "B", "Q", "P"]

def pawn_on_promotion_square(pc, pr):
    if pc == "P" and pr == 0:
        return True
    elif pc == "p" and pr == 7:
        return True
    return False

def populate_board(brd, wp, bp):
    for x in range(2):
        if x == 0:
            piece_amount = wp
            pieces = piece_list
        else:
            piece_amount = bp
            pieces = [s.lower() for s in piece_list]
        while piece_amount != 0:
            piece_rank, piece_file = random.randint(0, 7), random.randint(0, 7)
            piece = random.choice(pieces)
            if brd[piece_rank][piece_file] == " " and pawn_on_promotion_square(piece, piece_rank) == False:
                brd[piece_rank][piece_file] = piece
                piece_amount -= 1

def fen_from_board(brd):
    fen = ""
    for x in brd:
        n = 0
        for y in x:
            if y == " ":
                n += 1
            else:
                if n != 0:
                    fen += str(n)
                fen += y
                n = 0
        if n != 0:
            fen += str(n)
        fen += "/" if fen.count("/") < 7 else ""
    chosen_side = random.choice(["w", "b"])
    fen += f" {chosen_side} - - 0 1"
    return fen

def place_kings(brd):
    while True:
        rank_white, file_white, rank_black, file_black = random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7)
        diff_list = [abs(rank_white - rank_black),  abs(file_white - file_black)]
        if sum(diff_list) > 2 or set(diff_list) == set([0, 2]):
            brd[rank_white][file_white], brd[rank_black][file_black] = "K", "k"
            break

def main() -> int:
    if len(sys.argv) != 2:
        return 84
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Look at the readme >:(")
        return 84
    for _ in range(int(sys.argv[1])):
        board = [[" " for x in range(8)] for y in range(8)]
        piece_amount_white, piece_amount_black = random.randint(0, 15), random.randint(0, 15)
        place_kings(board)
        populate_board(board, piece_amount_white, piece_amount_black)
        augh = fen_from_board(board)
        b = chess.Board(augh)
        stalemate = "s" if b.is_stalemate() else "."
        check = "c" if b.is_check() else "."
        checkmate = "C" if b.is_checkmate() else "."
        print(f"{augh[:-8]} {stalemate}{check}{checkmate}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
