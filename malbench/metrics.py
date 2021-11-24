class Metric:
    def __init__(self, samples):
        self.samples = samples

    def detection_rate(self):
        failed = 0

        for sample in self.samples:
            if sample.detected == True:
                failed += 1
            
        if failed == 0:
            return 0

        return (failed / len(self.samples)) * 100

    def failed_samples(self):
        failed = []

        for sample in self.samples:
            if sample.detected == False:
                failed.append(sample.name)

        return failed
