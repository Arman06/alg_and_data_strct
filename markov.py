class MarkovAlgorithm:
    class Rule:
        def __init__(self, l_part, r_part, terminal=False):
            self.l_part = l_part
            self.r_part = r_part
            self.terminal = terminal

    __special_symbol = "*"

    def __init__(self, rules):
        self.rules = rules

    def execute(self, word):
        word = " " + word
        while True:
            for rule in self.rules:
                if rule.l_part in word:
                    new_word = word.replace(rule.l_part, rule.r_part, 1)
                    if word != new_word and not rule.terminal:
                        print(word + " - > " + new_word)
                        word = new_word
                        break
                    elif word != new_word and rule.terminal:
                        print(word + " - > " + new_word)
                        word = new_word
                        return word
                    elif word == new_word and rule is self.rules[-1]:
                        return word
                elif rule is self.rules[-1]:
                    return word


# keep in mind, that " " is an empty symbol
def main():
    rules1 = [MarkovAlgorithm.Rule("aa", "a"), MarkovAlgorithm.Rule("bb", "b")]
    markov1 = MarkovAlgorithm(rules1)
    print(markov1.execute("aabbaaa"))
    rules2 = [MarkovAlgorithm.Rule("*a", "b*"), MarkovAlgorithm.Rule("*b", "a*"),
              MarkovAlgorithm.Rule("*", " ", terminal=True), MarkovAlgorithm.Rule(" ", "*")]
    markov2 = MarkovAlgorithm(rules2)
    print(markov2.execute("abaa"))
    rules3 = [MarkovAlgorithm.Rule("*a", "a*"), MarkovAlgorithm.Rule("*b", "b*"),
              MarkovAlgorithm.Rule("a*", "aa", terminal=True), MarkovAlgorithm.Rule("b*", "bb", terminal=True),
              MarkovAlgorithm.Rule("*", " ", terminal=True), MarkovAlgorithm.Rule(" ", "*")]
    markov3 = MarkovAlgorithm(rules3)
    print(markov3.execute("abba"))


main()


