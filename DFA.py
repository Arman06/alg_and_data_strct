# deterministic finite automata


class DFA:

    class State:
        def __init__(self, name, transition={}):
            self.name = name
            self.transition = transition

        def __eq__(self, other):
            return self.name == other.name

    def __init__(self, states, start_state, final_state):
        self.states = states
        self.start_state = states[start_state]
        self.final_state = states[final_state]
        self.current_state = None

    def execute(self, string):
        self.current_state = self.start_state
        for char in string:
            self.current_state = self.states[self.current_state.transition[char]]
        return self.current_state == self.final_state


def main():
    states = {"s1": DFA.State(name="s1", transition={"0": "s1", "1": "s2"}),
              "s2": DFA.State(name="s2", transition={"0": "s1", "1": "s2"})}
    test1 = DFA(states=states, start_state="s1", final_state="s2")
    print(test1.execute(string="1"))


main()
