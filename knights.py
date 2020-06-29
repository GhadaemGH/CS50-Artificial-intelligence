from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is a knight if and only if A is not a knave (cannot be both)
    #this following line will be in all puzzles with the different symbols A,B,C
    # it represents the background information
    Biconditional(AKnight, Not(AKnave)), 
    # A is a knight if and only if "I am both a knight and a knave" is true
    Biconditional(AKnight, And(AKnight, AKnave))
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Backgroung information
    Biconditional(AKnight, Not(AKnave)), 
    Biconditional(BKnight, Not(BKnave)), 
    # A is a knight if and only if "We are both knaves" is true
    Biconditional(AKnight, And(AKnave, BKnave)) 
)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
 # Backgroung information
  Biconditional(AKnight, Not(AKnave)),
  Biconditional(BKnight, Not(BKnave)),
  # A is a knight if and only if "We are the same kind" is true
  Biconditional(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),  
  # B is a knight if and only if "We are different kinds" is true
  Biconditional(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Backgroung information
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),

    # Inclusive Or
    Or(Biconditional(AKnight, AKnight), Biconditional(AKnight, AKnave)),
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
