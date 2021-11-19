def detection_rate(samples):
    failed = 0
    total = 0

    for sample in samples.values():
        if sample["detected"] == True:
            failed += 1

        total += 1

    if failed == 0:
        return 0

    return (failed / total) * 100

def failed_samples(samples):
    failed = []

    for filepath, sample in samples.items():
        if sample["detected"] == False:
            failed.append(filepath)

    return failed