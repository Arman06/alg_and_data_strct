class FSM:

    class State:
        def __init__(self, transition, funcs):
            self.transition = transition
            self.funcs = funcs

    def __init__(self, states, start_state, final_state=None):
        self.states = states
        self.start_state = start_state
        self.current_state = None
        self.finite_state = final_state

    def execute(self, string):
        self.current_state = self.states[self.start_state]
        out = []
        for char in string:
            keyy = None
            print(char)
            for key in self.current_state.funcs.keys():
                if char in key:
                    print(char, key)
                    keyy = key
                    break
            out.append(self.current_state.funcs[keyy])
            self.current_state = self.states[self.current_state.transition[keyy]]
        return out


class ConditionalParser:
    _chars = "_01234567890abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
    new_group_blueprint = {"vars": "", "op": "", "groups": [], "back": None}

    def __init__(self):
        states = {"start": FSM.State(transition={"(": "new group", "!<>=&|": "operator",
                                                 ")": "start", ConditionalParser._chars: "var"},
                                     funcs={"(": ["new group"], "!<>=&|": ["new operator"],
                                             ")": ["end group"], ConditionalParser._chars: ["new var"]}),
                  "new group": FSM.State(transition={"(": "new group", ConditionalParser._chars: "var"},
                                         funcs={"(": ["new group"], ConditionalParser._chars: ["new var"]}),
                  "var": FSM.State(transition={ConditionalParser._chars: "var",
                                                        ")": "start", "!><=&|": "operator"},
                                   funcs={ConditionalParser._chars: ["add char var"],
                                                    ")": ["end var", "end group"], "!><=&|": ["end var",
                                                                                            "add char operator"]}),
                  "operator": FSM.State(transition={"(": "new group",
                                                    ConditionalParser._chars: "var", "=": "operator"},
                                        funcs={"(": ["end operator", "new group"],
                                               ConditionalParser._chars: ["end operator", "new var"],
                                                "=": ["add char operator"]})
                  }
        self.fsm = FSM(states=states, start_state="start", final_state="start")

    def new_group(self, group, char):
        group["groups"].append(ConditionalParser.new_group_blueprint.copy())
        group["groups"][len(group["groups"]) - 1]["back"] = group
        return group["groups"][len(group["groups"]) - 1]

    def end_group(self, group, char):
        group = group["back"]
        return group

    def new_var(self, group, char):
        group["vars"] += char
        return group

    def end_var(self, group, char):
        group["vars"] += "/"
        return group

    def add_char_var(self, group, char):
        group["vars"] += char
        return group

    def new_op(self, group, char):
        group["op"] += char
        return group

    def add_char_op(self, group, char):
        group["op"] += char
        return group

    def end_op(self, group, char):
        group["op"] += "/"
        return group

    def parse(self, expression):
        if not expression:
            return
        expression = expression.replace(" ", "")
        func_dict = {"new group": self.new_group, "add char operator": self.add_char_op,
                     "new var": self.new_var, "end var": self.end_var,
                     "end group": self.end_group, "add char var": self.add_char_var,
                     "new operator": self.new_op, "end operator": self.end_op}
        funcs_arr = self.fsm.execute(expression)
        print(funcs_arr)
        tokenized = ConditionalParser.new_group_blueprint.copy()
        for char, funcs in zip(expression, funcs_arr):
            for func in funcs:
                print("input:", char, "|func:", func)
                tokenized = func_dict[func](tokenized, char)
                print(tokenized)
        return tokenized


def main():
    parser = ConditionalParser()
    # parsed = parser.parse("(a != b) & (c | d)")
    print(parser.parse("(c == b) & (a != b)"))
    # print(parsed["groups"])


main()
