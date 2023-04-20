# Malbench
Malbench is a command-line tool for testing and evaluating the effectiveness of malware detection tools (such as antivirus solutions). It does this by running a set of malware samples, and checking if the malware is flagged by the detection tool we are evaluating. Malbench is built to be modular and configurable, so it can be customized to meet the specific needs of different users and environments.

### Disclaimer 
**:warning: WARNING**: Malbench is designed to run malicious code that can harm your computer. Malbench should only be run on secure and isolated environments by users who know what they are doing. Do **not** run Malbench on a computer or network that contains sensitive information or data that you are not willing to lose or become compromised. By downloading and/or using this software, you acknowledge and understand the risks of using this software; and assume full responsibility for any damages that may result from running Malbench.

**:information_source: NOTE**: It is important to note that Malbench does not include any malware samples. Therefore, users are expected to provide their own samples for testing purposes. This is to ensure that Malbench is used responsibly and ethically; and that users have control over the types of malware being tested.

### Why Use Malbench?
Malware detection tools are an essential component of any computer security strategy, but they are not foolproof. New techniques and methods are constantly being developed to evade detection. It is important to regularly test and evaluate the effectiveness of detection tools to ensure that we are keeping up with these evolving threats.

With all the different features and algorithms of modern antivirus solutions, it can be hard to find practical and objective results on what-all they defend against. Malbench can be leveraged to bulk-test known malware samples against antivirus solutions to deliver real and practical results. This is done by automatically launching multiple malware payloads on a system and seeing what samples are detected and which ones were evaded. With Malbench, users can customize their testing to meet their specific needs, selecting the malware samples they want to run, and the duration of a test.

## Installation
1.  Clone the repository:
    ```bash
    git clone https://github.com/youkergav/Malbench.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd malbench
    ```
3.  Install the required dependencies using [Poetry](https://python-poetry.org/):
    ```bash
    poetry install
    ```

    If you don't have Poetry installed, you can install it using the instructions on the official [Poetry website](https://python-poetry.org/docs/#installation).

## Usage
To use Malbench, simply run the following command inside your virtual environment:
```bash
python -m malbench /path/to/malware
```

Replace `/path/to/malware` with your `path` argument. The `path` argument should be the path to the malware samples you want to test. This can be either a single file or a folder containing multiple files. Only executable files will be ran by Malbench.

By default, Malbench will show a banner when it starts, and will prompt you to confirm that you understand the risks involved before running the malware samples. You can disable the banner using the `--no-banner` flag, and disable the confirmation prompt using the `--no-warning` flag.

Malware samples are run one by one, and Malbench will wait for each sample to be stopped by the detection software or reach the specified 2 second timeout before moving on to the next sample. This timeout can be changed with the `--timeout` flag. If a sample completes successfully, Malbench will print a red message with a `[-]` prefix, indicating it wasn't stopped by the detection software. If a sample has to be forcibly terminated by the detection software, Malbench will print a green message with a `[+]` prefix, indicating is was successfully detected and stopped.

A full list of arguments to use with Malbench are below.
```bash
usage: malbench [-h] [-v] [-t TIMEOUT] [-nB] [-nW] path

positional arguments:
path file or folder path to the malware samples

optional arguments:
-h, --help show this help message and exit
-v, --verbose prints additional info
-t TIMEOUT, --timeout TIMEOUT
malware TTL before being marked as failure (2 default)
-nB, --no-banner hides the banner logo
-nW, --no-warning Does prompt for user confirmation before running
```

## Contributing
Contributions to Malbench are always welcome! If you'd like to contribute, please fork the repository and create a new branch for your changes. Once you've made your changes, create a pull request and we'll review your changes. *For major changes, please open an issue first to discuss what you would like to change.*

Pull Request Checklist:
- New code follows similar coding styles of the existing codebase.
- New code is backed up by unit tests, with a minimum of 70% coverage.
- New code passes all linting and strict-typing rules.
- New code is well documented with docstrings and compiled in `/docs`.
- Updates are made to the README when applicable.

## License
This project is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html). See the [LICENSE.md](./LICENSE.md) file for details.

## Credits
Malbench was created by [Gavin Youker](mailto:youkergav@gmail.com).
