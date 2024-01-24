<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/paydos/BookingAutomation">
    <img src="images/image.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Accenture Places Booking Automation</h3>

  <p align="center">
    An automated solution to book your place at Accenture.
    <br />
    <a href="https://github.com/paydos/BookingAutomation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/paydos/BookingAutomation">View Demo</a>
    ·
    <a href="https://github.com/paydos/BookingAutomation/issues">Report Bug</a>
    ·
    <a href="https://github.com/paydos/BookingAutomation/issues">Request Feature</a>
  </p>
</div>
<br />

## Accenture Places Booking Automation

Hello! I'm Daniel Ruiz Blanco, a data scientist intern at Accenture and the creator of the Accenture Places Booking Automation project. I embarked on this journey to simplify the process of booking a place at Accenture, which I found to be quite lengthy and often resulted in missing out on bookings due to high demand.

While commuting to and from the office, I found myself with some spare time. As a developer who enjoys problem-solving, I decided to utilise this time to code a solution that could assist others.

This project is a collection of Python scripts that work in harmony to complete the booking process. It's my solution to a problem many of us face, and I hope it will be as helpful to my colleagues as it has been to me.

I'm pleased to announce that this project now supports worldwide locations. This feature has been implemented and is ready for use.

Thank you for your interest in this project. I'm looking forward to hearing your feedback and suggestions.

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

- `__main__.py` script is the main driver of the application. It initializes the booking automation process, loads the booking page, makes a reservation, changes the location, types in the location, chooses the floor, chooses the starting and finishing time, searches for available slots, applies filters, and finally books the seat. It uses the `BookingAutomation` class from the `lib/booking.py` module to perform these tasks.
- The `BookingAutomation` class uses the Selenium WebDriver to interact with the booking website. It also uses the `DateCalculator` and `DateAdapter` classes from the `lib/date.py` module to calculate and format the dates used in the booking process.
- The `cron.py` script in the lib directory is responsible for scheduling the execution of the booking process. It uses the `schedule` library to run the booking process at specific times. It also logs the execution of the scheduled tasks and checks for scheduled tasks every minute.

- The `setup.py` script in the lib directory is responsible for setting up the environment by installing the necessary Python packages. It uses the `AutoInstaller` class to automate this process. The `AutoInstaller` class also manages the parameters for the booking, adds the application to the system startup, and provides options to remove the application from the system startup and delete all related files, reinstall the application, and upgrade the application to the latest version.

- The `installer.py` script utilizes the `AutoInstaller` class from the `lib/setup.py` module to automate the installation of required modules and adds the application to the system startup. It accepts two required arguments: `--location` and `--floor`, which are used to specify the location for the booking and the preferred floor number. It also accepts optional arguments for booking preferences, uninstalling the service, reinstalling the application, and upgrading the application to the latest version.

- The `paths.py` script in the lib directory defines the file paths used throughout the project, such as the log file path, the requirements file path, the installation log path, and the parameters file path. It also defines the paths for the log folder, scripts folder, and parameters folder.

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

### Download

1. Download the repository using HTTPS:
   ```sh
   git clone https://github.com/paydos/BookingAutomation.git
   ```
   Or with SSH:
   ```sh
   git clone git@github.com:paydos/BookingAutomation.git
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

The `installer.py` script simplifies the setup process by automating the installation and setup of necessary services and dependencies. Here's how to use it:

1. Run the `installer.py` script with the required `--location` and `--floor` arguments. Additional optional arguments include `--heightdesk` and `--monitor` for booking preferences, `--remove` to uninstall the service, `--reinstall` to reinstall the application, and `--upgrade` to upgrade the application to the latest version. This script performs the following tasks:
   - Installs necessary Python packages from `requirements.txt`.
   - Sets up the BookingAutomation service to run at startup.
   - Configures booking location and floor parameters.
   - Reinstalls the application if `--reinstall` is set to True. This will remove the current installation and install it again, ensuring you have a clean setup.
   - Upgrades the application to the latest version if `--upgrade` is set to True. This will fetch the latest version from the repository and replace your current version with it.

To run the installer with custom location and floor:
   ```sh
   python installer.py --location "Your Location" --floor YourFloorNumber
   ```
   
To run the installer with custom location, floor, and optional parameters:
   ```sh
   python installer.py --location "Your Location" --floor YourFloorNumber --heightdesk True --monitor True
   ```

To reinstall the application with a new location and floor (useful for changing locations or fixing bugs). You can also include optional parameters:
   ```sh
   python installer.py --location "New Location" --floor NewFloorNumber --heightdesk True --monitor True --reinstall True
   ```


To only upgrade the application:
   ```sh
   python installer.py --upgrade True
   ```

2. After the `installer.py` script has finished running, simply reboot your computer. Upon startup, the BookingAutomation service will automatically run in the background without any further action required from you.

This approach eliminates the need for manual configuration and ensures that all necessary components are correctly installed and configured.

_For more examples, please refer to the [Documentation](https://github.com/paydos/BookingAutomation)_


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
 - [ ] Implement automated check-in feature.
 - [ ] Enhance scheduling system to handle scenarios where the user's computer is not active by the designated time.
 - [ ] Develop a user notification system within the GUI to inform about successful seat reservations (or another way of notifying the user about the booked place).
 - [ ] Extend the seat selection algorithm to include multiple floors, improving the chances of finding an available seat.
 - [X] Introduce user-configurable settings during installation to set preferred location and floor.
 - [ ] Address the issue where the automated driver update process stalls if Chrome is already running.
 - [X] Update logging (Log file generates too much data)
 - [X] Add reinstaller
 - [X] Add automatic upgrader
 
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
