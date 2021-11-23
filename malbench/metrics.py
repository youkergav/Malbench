class Metric:
    def __init__(self, samples):
        self.samples = samples

    def detection_rate(self):
        failed = 0

        for sample in self.samples.values():
            if sample.detected == True:
                failed += 1
            
        if failed == 0:
            return 0

        return (failed / len(self.samples.values())) * 100

    def failed_samples(self):
        failed = []

        for name, sample in self.samples.items():
            if sample.detected == False:
                failed.append(name)

        return failed
