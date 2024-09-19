import random
from collections import defaultdict
from string import punctuation

class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            text.translate(str.maketrans("","", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        tokens = self._tokenize(text)
        for i, token in enumerate(tokens):
            if(len(tokens) -1) == i:
                break
            self.graph[token].append(tokens[i +1])
    
    def generate(self, prompt, length = 10):
        # get the last token from the prompt
        current = self._tokenize(prompt)[-1]
        # initialize the output
        output = prompt
        for i in range(length):
            # look up the options in the graph dictionary
            options = self.graph.get(current, [])
            if not options:
                continue
            # use random.choise method to pick a current option
            current = random.choice(options)
            #add the random choise to the output string
            output += f"{ current }"
            
        return output
