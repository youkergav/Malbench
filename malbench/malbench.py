import time
import args
import messages
import samples
import metrics

args = args.get_args()

message = messages.Message(args.verbose)

if not args.no_banner:
    message.banner()

print("Running sample malware...\n")
malware = {}
keys = []

# Start the malware samples.
message.info("Loading malware...")
for file in args.path:
    sample = samples.run(file)
    malware[file] = sample

    if not sample["detected"]:
        keys.append(file)
    else:
        message.good("Detected {}".format(file)) if args.verbose else message.good(file)

    time.sleep(.2)

# Monitor the malware processes for prevention.
message.info("Monitoring malware for detection...")
while len(keys):
    for key in keys:
        detected = samples.monitor(malware[key])

        if detected != None:
            malware[key]["detected"] = detected
            keys.remove(key)

            if detected:
                message.good("Detected {}".format(key)) if args.verbose else message.good(key)
            else:
                message.bad("Failed to detect {}".format(key)) if args.verbose else message.bad(key)
    
    time.sleep(.2)

# Calculate metrics and print results.
detection_rate = metrics.detection_rate(malware)

if detection_rate == 100:
    print("\nDone. Detection rate: {}".format(message.green(str(detection_rate) + "%")))
else:
    failed = metrics.failed_samples(malware)

    print("\nDone. Detection rate: {} ({} samples failed):".format(message.red(str(detection_rate) + "%"), len(failed)))

    for filename in failed:
        print(filename)
    print("")