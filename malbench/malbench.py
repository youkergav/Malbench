import os
import time
import args
import cprint
import samples
import metrics

args = args.get_args()

if not args.no_banner:
    cprint.banner()

print("Running sample malware...\n")
malware = {}
keys = []

# Start the malware samples.
for file in args.path:
    sample = samples.run(file)
    malware[file] = sample

    if not sample["detected"]:
        keys.append(file)
    else:
        cprint.good(file)

    time.sleep(.2)

# Monitor the malware processes for prevention.
while len(keys):
    for key in keys:
        detected = samples.monitor(malware[key])

        if detected != None:
            malware[key]["detected"] = detected
            keys.remove(key)

            if detected:
                cprint.good(key)
            else:
                cprint.bad(key)
    
    time.sleep(.2)

# Calculate metrics and print results.
detection_rate = metrics.detection_rate(malware)

if detection_rate == 100:
    print("\nDone. Detection rate: {}".format(cprint.green(str(detection_rate) + "%")))
else:
    failed = metrics.failed_samples(malware)

    print("\nDone. Detection rate: {} ({} samples failed):".format(cprint.red(str(detection_rate) + "%"), len(failed)))

    for filename in failed:
        print(filename)
    print("")