class Bayes:
    def __init__(self):
        self.container = {}
    def set(self, hypothesis, prior):
        self.container[hypothesis] = prior
    def mult(self, hypothesis, likelihood):
        self.container[hypothesis] *= likelihood
    def normalize(self):
        total = sum(self.container.values())
        for hypothesis in self.container:
            self.container[hypothesis] /= total
    def prob(self, hypothesis):
        return self.container[hypothesis]
bayes = Bayes()
bayes.set('碗1', 0.5)
bayes.set('碗2', 0.5)
bayes.mult('碗1', 0.75) # P(巧克力|碗1) = 3/4
bayes.mult('碗2', 0.5)  # P(巧克力|碗2) = 1/2
bayes.normalize()
print("来自碗1的概率:", bayes.prob('碗1'))