<a name="readme-top"></a>

# Bitly URL Shortener

<details>
<summary><h2>Table of Contents</h2></summary>

  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project objectives](#project-objectives)
  - [License](#license)
</details>

## Overview

**Bitly URL Shortener** is an advanced utility designed to enhance digital marketing and online presence efforts by providing users with the capability to create and monitor shortened URLs using the Bitly API. This tool proves essential for digital marketers, bloggers, and professionals seeking to track the performance of their shared links, understanding user engagement and reach. The program seamlessly interacts with the Bitly API to shorten lengthy URLs and to fetch vital statistics such as click counts. With a straightforward command-line interface, users can effortlessly manage and analyze their Bitly links without needing to navigate the Bitly website.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

- **URL shortening:** easily turn long, cumbersome links into concise Bitly links with a simple command.
- **Click tracking:** determine the number of clicks a Bitly link has received, offering insight into link engagement.
- **Bitly link verification:** ascertain if a link is a Bitly link before proceeding with any operations.
- **User-friendly interface:** straightforward command-line inputs make it simple for users to create and manage their Bitly links.
- **Error handling:** comprehensive error management system, notifying users of HTTP and request-related issues.
- **Security:** the tool securely interfaces with the Bitly API using access tokens, ensuring data privacy and safety.
- **Streamlined code structure:** functions like `shorten_link`, `count_clicks`, and `is_bitlink` make the codebase modular and maintainable.
- **Environment variable integration:** the tool leverages the `dotenv` package, allowing users to securely store and access API tokens.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation

To install Countries Workload Bot, follow these steps:

### 1. 🐍 Environment setup

First of all, make sure you have Python 3 installed, version `3.8.0` or higher. If not, visit the [official Python website](https://www.python.org/) and download the latest version.

The command to check your Python version should show a version no lower than `3.5.0`. You might need to use aliases such as `python`, `py`, `python3.8`, or onwards up to `python3.12` instead of `python3`.

```
$ python --version
Python 3.8.10
```

### 2. 📥 Repository cloning

Clone the repository using the command below:

```
git clone https://github.com/WarLikeLaux/bitly-url-shortener
```

Then, navigate to the project folder:

```
cd bitly-url-shortener
```

### 3. 🧩 Dependencies installation

Use pip (or pip3, if there's a conflict with Python2) to install the dependencies:

```
pip install -r requirements.txt
```

### 4. 🗝️ Environment variables setup

To set up your environment variables, you'll need to create a `.env` file in the root directory of the project. If you already have a `.env.example` file, you can simply copy with rename it to `.env` using the command `cp .env.example .env`. Once you've done this, add or/and fill the following lines by values in your `.env` file:

- **`BITLY_ACCESS_TOKEN`**:
    - This is your unique token for accessing the bit.ly API.
    - To obtain it:
        1. Register on [bit.ly](https://bitly.com/).
        2. Once registered, navigate to [this settings page](https://app.bitly.com/settings/api/).
        3. Enter your password in the "Enter password" field.
        4. Click on "Generate token".
        5. You'll be provided with a token - this is your `BITLY_ACCESS_TOKEN`.
    - Place this token in your `.env` file as:
        ```
        BITLY_ACCESS_TOKEN=your_generated_token_here
        ```
		Replace `your_generated_token_here` with the token you obtained from the bit.ly settings page.

Please ensure that each environment variable is assigned the correct value.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

To use Bitly URL shortener, follow these steps:

**1. To shorten a link::**
```
python main.py [your_unshortened_link]
```

**2. To retrieve the number of clicks for a shortened Bitly link:**
```
python main.py [your_bitly_link]
```

Replace `[your_unshortened_link]` with the link you wish to shorten, and `[your_bitly_link]` with the Bitly link for which you want to retrieve click counts.

Based on your input link, the tool will either:
- Return a shortened Bitly link if you provided an unshortened link.
- Display the total number of clicks the Bitly link has received if you provided a Bitly link.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project objectives

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

This code is open-source and free for any modifications, distributions, and uses. Feel free to utilize it in any manner you see fit.

<p align="right">(<a href="#readme-top">back to top</a>)</p>