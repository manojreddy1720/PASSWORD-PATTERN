"""
Advanced Password Pattern Validation via Pushdown Automata and Context-Free Grammars
Author: C. Manoj Reddy (RA2411026050038)
"""
from pda_engine import PDA

def build_passphrase_bracket_dpda() -> PDA:
    states = {"q0", "q1", "qf"}
    inputs = {"(", ")", "[", "]", "{", "}"}
    stack_alph = {"(", "[", "{", "Z0"}
    trans = {}

    trans[("q0", "(", "Z0")] = [("q1", ("(", "Z0"))]
    trans[("q0", "[", "Z0")] = [("q1", ("[", "Z0"))]
    trans[("q0", "{", "Z0")] = [("q1", ("{", "Z0"))]

    for opener in ["(", "[", "{"]:
        for X in ["(", "[", "{", "Z0"]:
            trans[("q1", opener, X)] = [("q1", (opener, X))]

    trans[("q1", ")", "(")] = [("q1", ())]
    trans[("q1", "]", "[")] = [("q1", ())]
    trans[("q1", "}", "{")] = [("q1", ())]

    trans[("q1", "", "Z0")] = [("qf", ("Z0",))]

    return PDA(states, inputs, stack_alph, trans, "q0", "Z0", {"qf"})

def validate_structural_passphrase_brackets(pw: str) -> bool:
    brackets = "".join(c for c in pw if c in "()[]{}")
    if not brackets:
        return True
    dpda = build_passphrase_bracket_dpda()
    acc, _ = dpda.accepts_deterministic(brackets)
    return acc

def is_mirrored_palindrome(pw: str) -> bool:
    cleaned = pw.lower()
    if len(cleaned) < 4:
        return False
    if len(cleaned) % 2 == 0:
        mid = len(cleaned) // 2
        if cleaned[:mid] == cleaned[mid:][::-1]:
            return True
    mid = len(cleaned) // 2
    if cleaned[:mid] == cleaned[mid+1:][::-1]:
        return True
    return False

def validate_passphrase_comprehensive(pw: str) -> bool:
    if len(pw) < 8 or len(pw) > 32:
        return False
    if is_mirrored_palindrome(pw):
        return False
    if not validate_structural_passphrase_brackets(pw):
        return False
    return True
