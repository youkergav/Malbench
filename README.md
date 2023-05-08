# Malbench
Malbench is a command-line tool for testing and evaluating the effectiveness of malware detection tools (such as antivirus solutions). It does this by running a set of malware samples, and checking if the malware is flagged by the detection tool we are evaluating. Malbench is built to be modular and configurable, so it can be customized to meet the specific needs of different users and environments.
![Malbench Terminal Demo](https://i.imgur.com/oGQNU8i.gif)

## About
### Disclaimer 
**⚠ WARNING**: Malbench is a tool for testing antivirus software against real-world malware samples. While it does not contain any malware on its own, it is designed to run malware samples provided by the user. Use Malbench only in secure and isolated environments that you are authorized in doing so. Do **not** use Malbench on a computer or network that contains sensitive information or data that you are not willing to lose and/or become compromised. By using Malbench, you acknowledge the risks and assume full responsibility for any damages that may result.

**ℹ️ NOTE**: As stated above: *Malbench does not come with any malicious code installed*. It is the user's responsibility to provide their own samples for testing purposes. This is to ensure that Malbench is used responsibly and ethically, and that users have control over the types of malware being tested.

### Why Use Malbench
Malware detection tools are an essential component of any computer security strategy, but they are not foolproof. New techniques and methods are constantly being developed to evade detection. It is important to regularly test and evaluate the effectiveness of detection tools to ensure that we are keeping up with these evolving threats.

With all the different features and algorithms of modern antivirus solutions, it can be hard to find practical and objective results on what-all they defend against. Malbench can be leveraged to bulk-test known malware samples against antivirus solutions to deliver real and practical results. This is done by automatically launching multiple malware payloads on a system and seeing what samples are detected and which ones were evaded. With Malbench, users can customize their testing to meet their specific needs, selecting the malware samples they want to run, and the duration of a test.

### How Antivirus is Benchmarked
Malbench launches each malware sample selected by the user and monitors its execution. If the sample completes without error, it is flagged as `UNDETECTED`. If the sample is terminated with an error code, it is flagged as `DETECTED`, indicating that it was killed by the antivirus solution. If the sample is still running after a designated time (defaults to 2 seconds), Malbench forcibly kills the program and flags it as `UNDETECTED`, as the antivirus solution did not detect it in time.

After each sample is run, Malbench displays the detection rate. The detection rate is a percentage representing the amount of samples the antivirus successfully defended against. 

$$
\text{Detection rate} = \frac{\text{Number of samples flagged as detected}}{\text{Total number of samples}} \times 100\%
$$

## Installation
To install Malbench for general use, follow these simple steps:

1.  Ensure that the following is installed on your system: [Python 3.8.1+](https://www.python.org/downloads/), and [PIP](https://pypi.org/project/pip/) (included with most Python installations).
2.  Install Malbench via pip by running the following command:
    ```bash
    pip install malbench
    ```
3.  Confirm that Malbench has been installed:
    ```
    malbench --version
    ```

*If you are interested in installing Malbench for development, take a look at the [CONTRIBUTING.md](./CONTRIBUTING.md) file.*

## Usage
To use Malbench, simply run the following command inside your virtual environment:
```bash
python -m malbench /path/to/malware
```

Replace `/path/to/malware` with your `path` argument. The `path` argument should be the path to the malware samples you want to test. This can be either a single file or a folder containing multiple files. Only executable files will be ran by Malbench.

By default, Malbench will show a banner when it starts, and will prompt you to confirm that you understand the risks involved before running the malware samples. You can disable the banner using the `--no-banner` flag, and disable the confirmation prompt using the `--no-warning` flag (as seen in the demo).

Malware samples are run one by one, and Malbench will wait for each sample to be stopped by the detection software or reach the specified 2 second timeout before moving on to the next sample. This timeout can be changed with the `--timeout` flag. If a sample completes successfully, Malbench will print a red message with a `[-]` prefix, indicating it wasn't stopped by the detection software. If a sample has to be forcibly terminated by the detection software, Malbench will print a green message with a `[+]` prefix, indicating is was successfully detected and stopped.

A full list of arguments to use with Malbench are below. This can be displayed with `--help`.
```bash
usage: malbench [-h] [-v] [-t TIMEOUT] [-nB] [-nW] [-d] path

positional arguments:
  path                  file or folder path of malware executables

options:
  -h, --help            show this help message and exit
  -v, --version         shows malbench version number and exits
  -t TIMEOUT, --timeout TIMEOUT
                        malware TTL before being marked as failure (2 default)
  -nC, --no-color       disables colored output
  -nB, --no-banner      hides the banner logo
  -nW, --no-warning     bypasses user confirmation before running
  -d, --dev             enables stack tracing
```

## Contributing
Contributions to Malbench are welcomed! If you'd like to contribute, please read our [CONTRIBUTING.md](./CONTRIBUTING.md) to get started.

## License
This project is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html). See the [LICENSE.md](./LICENSE.md) file for details.

## Credits
Malbench was created by [Gavin Youker](mailto:youkergav@gmail.com).
