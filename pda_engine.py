"""
Pushdown Automata (PDA) Engine for Password Pattern Validation
Author: K. Divakar (RA2411026050022)
"""
from typing import Set, Dict, Tuple, List, Any, Optional

class PDA:
    def __init__(self, states: Set[str], input_alphabet: Set[str],
                 stack_alphabet: Set[str],
                 transitions: Dict[Tuple[str, str, str], List[Tuple[str, Tuple[str, ...]]]],
                 start_state: str, start_stack_symbol: str, accept_states: Set[str]):
        self.states = set(states)
        self.input_alphabet = set(input_alphabet)
        self.stack_alphabet = set(stack_alphabet)
        self.transitions = transitions
        self.start_state = start_state
        self.start_stack = start_stack_symbol
        self.accept_states = set(accept_states)

    def accepts_deterministic(self, input_str: str) -> Tuple[bool, List[Tuple]]:
        current_state = self.start_state
        stack: List[str] = [self.start_stack]
        w = input_str
        history = [(0, current_state, w, list(reversed(stack)))]

        step = 0
        while True:
            step += 1
            top_stack = stack[-1] if stack else None
            if top_stack is None:
                break

            symbol = w[0] if w else None
            key = (current_state, symbol, top_stack) if symbol else None

            if key and key in self.transitions:
                next_state, push_tokens = self.transitions[key][0]
                stack.pop()
                if push_tokens:
                    for token in reversed(push_tokens):
                        stack.append(token)
                w = w[1:]
                current_state = next_state
                history.append((step, current_state, w, list(reversed(stack))))
            elif (current_state, "", top_stack) in self.transitions:
                next_state, push_tokens = self.transitions[(current_state, "", top_stack)][0]
                stack.pop()
                if push_tokens:
                    for token in reversed(push_tokens):
                        stack.append(token)
                current_state = next_state
                history.append((step, current_state, w, list(reversed(stack))))
            else:
                break

        accepted = (w == "" and current_state in self.accept_states)
        return accepted, history
