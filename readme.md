<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

# Accenture Places Booking Automation

Welcome to the Accenture Places Booking Automation project. This project is designed to automate the process of booking a place at Accenture. It is composed of several Python scripts that work together to navigate the booking website, select the desired parameters, and complete the booking process.

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The project is composed of several Python scripts:

- `__main__.py`: This is the main script that orchestrates the entire booking process. It initializes the booking automation, loads the booking page, makes a reservation, changes the location, types in the location, chooses the floor, chooses the starting and finishing time, searches for available slots, applies filters, and finally books the seat.

- `cron.py`: This script is responsible for scheduling the execution of the booking process. It uses the `schedule` library to run the booking process at specific times.

- `booking.py`: This script contains the `BookingAutomation` class which encapsulates all the steps involved in the booking process. It uses the Selenium WebDriver to interact with the booking website.

- `date.py`: This script contains the `DateCalculator` and `DateAdapter` classes which are used to calculate and format the dates used in the booking process.

- `setup.py`: This script is responsible for setting up the environment by installing the necessary Python packages.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

For this project I used Python and Selenium Webdriver and its patched version undetected-chromedriver

* [Python](https://www.python.org/)
* [Selenium WebDriver](https://www.selenium.dev/)
* [Schedule](https://schedule.readthedocs.io/)
* [Undetected Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo using HTTPS:
   ```sh
   git clone https://github.com/paydos/BookingAutomation.git
   ```
   Or with SSH:
   ```sh
   git clone git@github.com:paydos/BookingAutomation.git
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

These scripts are designed to be run on Windows. To run them as a background process (daemon) whenever the computer starts, you can create a Windows service. Here is an example of how to do this:

1. Open the Windows Command Prompt as an administrator.
2. Use the `sc` command to create a new service that will start the Python script at boot. Replace `path_to_python` and `path_to_script` with the paths to your Python executable and the `__main__.py` script respectively:
   ```sh
   sc create BookingAutomation binPath= "path_to_python path_to_script" start= auto
   ```

Please note that the script will not run if you manually start your computer. The service will start the script only when the system boots up.

_For more examples, please refer to the [Documentation](https://github.com/paydos/BookingAutomation)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/paydos/BookingAutomation/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

If you have any questions or suggestions, feel free to reach out to me:

- Instagram: [@ruizblancoo](https://www.instagram.com/ruizblancoo)
- Email: [darru2002@gmail.com](mailto:darru2002@gmail.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/paydos/BookingAutomation.svg?style=for-the-badge
[contributors-url]: https://github.com/paydos/BookingAutomation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/paydos/BookingAutomation.svg?style=for-the-badge
[forks-url]: https://github.com/paydos/BookingAutomation/network/members
[stars-shield]: https://img.shields.io/github/stars/paydos/BookingAutomation.svg?style=for-the-badge
[stars-url]: https://github.com/paydos/BookingAutomation/stargazers
[issues-shield]: https://img.shields.io/github/issues/paydos/BookingAutomation.svg?style=for-the-badge
[issues-url]: https://github.com/paydos/BookingAutomation/issues
[license-shield]: https://img.shields.io/github/license/paydos/BookingAutomation.svg?style=for-the-badge
[license-url]: https://github.com/paydos/BookingAutomation/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/daniel-ruiz-blanco-93474b171/
