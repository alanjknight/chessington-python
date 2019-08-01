"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        squares_y_axis=1
        if self.player.name=='BLACK':
            squares_y_axis=-1
        
        cur_pos = board.find_piece(self)
        checkIfUnmoved = (cur_pos.row == 1 and self.player.name == 'WHITE') or (cur_pos.row == 6 and self.player.name == 'BLACK')

        poss_moves = []
        board_cells=[]
        for row in range(0,len(board.board)):
            for cell in range(0,len(board.board[row])):
                board_cells.append([row,cell])

        #can move 1 space forward
        if board.valid_square (cur_pos.row + squares_y_axis, cur_pos.col):
            row_increment = cur_pos.row + squares_y_axis
        else:
            row_increment = cur_pos.row

        pawn=(Square.at(row_increment,cur_pos.col)) #move forward one square
        if board.get_piece(pawn) == None and pawn not in poss_moves:
            poss_moves.append(pawn)
       

        #can move 2 spaces forward if not yet moved, as long as its not obstructed 
        if checkIfUnmoved:
            if not board.get_piece(Square.at(cur_pos.row+1 * squares_y_axis, cur_pos.col)):
            
                if board.valid_square(cur_pos.row+2 * squares_y_axis, cur_pos.col):
                    pawn = Square.at(cur_pos.row + 2 * squares_y_axis, cur_pos.col)
                else:
                    pawn = Square.at(cur_pos.row, cur_pos.col)

                if board.get_piece(pawn) == None and pawn not in poss_moves:
                    poss_moves.append(pawn)
        return poss_moves
        
class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []