# Snagger-CLI
The Username Availability Checker For Social Media

```
# Snagger - Username Availability Checker

Snagger is a powerful Python tool designed to assist hackers and security researchers in identifying available usernames across multiple social media platforms. Utilizing advanced techniques including proxy support and multi-threading, Snagger provides a fast and efficient way to scout for unused handles on some of the internet's most popular sites.

## Features

- **Support for Multiple Platforms**: Check username availability on platforms like Twitter, Instagram, YouTube, Facebook, LinkedIn, TikTok, Snapchat, Reddit, Pinterest, and Discord.
- **Custom URL Checks**: Easily extendable to include any platform by specifying a custom URL template.
- **Proxy Support**: Integrated proxy handling to bypass IP bans and rate limits.
- **Multi-threading**: Utilizes multi-threading to maximize the efficiency and speed of checks.
- **Configurable**: Everything from the number of threads to use, proxies, and the specific sites to check can be adjusted in the configuration file.

## Prerequisites

Before you begin using Snagger, ensure you have the following:
- Python 3.6+
- `requests` library installed

```bash
pip install requests

```Installation
Clone the repository to your local machine

```git clone https://github.com/SleepTheGod/Snagger-CLI/
cd snagger

```Usage
Configuration: Adjust snagger_config.ini to set your preferences (e.g., targeted sites, proxies, and thread count).
Prepare Word List: Place your word list in the word_lists directory. This should contain one username per line.
Now we run the tool python Snagger.py
Results will be outputted to the file specified in the configuration file (AVAILABLE.txt by default).

Contributing
Contributions to Snagger are welcome! Here's how you can help:

Fork the Repository: Click the 'Fork' button on the top right of this page.
Clone Your Fork: Clone the repository to your local machine.
Create a New Branch: Make your changes in a new git branch.
Submit a Pull Request: Push your branch and changes back up to your fork on GitHub and submit a pull request.
We appreciate your efforts to improve Snagger and actively welcome pull requests.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Disclaimer
Usage of Snagger for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

Enjoy hunting for usernames responsibly!
