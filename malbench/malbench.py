import time
import args
import messages
import samples
import metrics

args = args.Args()
message = messages.Message(args.verbose)

if not args.no_banner:
    message.banner()

print("Running sample malware...\n")
malware = {}
keys = []

# Start the malware samples.
message.info("Loading malware...")
for file in args.path:
    sample = samples.Sample(file)
    malware[sample.name] = sample

    if not sample.detected:
        keys.append(sample.name)
    else:
        message.good("Detected {}".format(sample.name)) if args.verbose else message.good(sample.name)

    time.sleep(.2)

# Monitor the malware processes for prevention.
message.info("Monitoring malware for detection...")
while len(keys):
    for name in keys:
        sample = malware[name]
        detected = sample.monitor()

        if detected != None:
            keys.remove(name)

            if detected:
                message.good("Detected {}".format(sample.name)) if args.verbose else message.good(sample.name)
            else:
                message.bad("Failed to detect {}".format(sample.name)) if args.verbose else message.bad(sample.name)
    
    time.sleep(.2)

# Calculate metrics and print results.
results = metrics.Metric(malware)
detection_rate = results.detection_rate()

if detection_rate == 100:
    print("\nDone. Detection rate: {}".format(message.green(str(detection_rate) + "%")))
else:
    failed = results.failed_samples()

    print("\nDone. Detection rate: {} ({} samples failed):".format(message.red(str(detection_rate) + "%"), len(failed)))

    for filename in failed:
        print(filename)
    print("")
