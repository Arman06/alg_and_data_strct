class MealyMachine:

    class State:
        def __init__(self, transition={}, output={}):
            self.transition = transition
            self.output = output

    def __init__(self, states, start_state, final_state=None):
        self.states = states
        self.start_state = start_state
        self.current_state = None

    def execute(self, string):
        self.current_state = self.states[self.start_state]
        out = ""
        for char in string:
            out += self.current_state.output[char]
            self.current_state = self.states[self.current_state.transition[char]]
        return out


def main():
    states = {"s1": MealyMachine.State(transition={"0": "s1", "1": "s2"}, output={"0": "0", "1": "0"}),
              "s2": MealyMachine.State(transition={"0": "s1", "1": "s2"}, output={"0": "1", "1": "1"})}
    test1 = MealyMachine(states=states, start_state="s2")
    print(test1.execute(string="011"))


main()
