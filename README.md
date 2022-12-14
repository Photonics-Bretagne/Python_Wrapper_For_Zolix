# Python_Wrapper_For_Zolix
Driver wrapper in Python for Omni-λ Zolix monochromator

OS: Windows 10

Python version: 3.8

## Introduction ##

Based in Beijing (China), Zolix Instruments Co. Ltd develops optical instruments for industry and research such as spectrographs, detectors and monochromators.

The [Omni-λ monochromators](http://zolix.com.cn/en/prodcon_370_376_741.html) from Zolix can be used to generate and to tune a monochromatic beam over UV to NIR in order, for example, to illuminate samples in fluorescence.

C++ and Delphi drivers allow users to control the Zolix monochromators and to design their own acquisition programs.

In this project, we implemented a Python-based driver to control the Omni-λ monochromators.

## Principle ##

The principle of the driver wrapper consists in using a server conected to the Omni-λ monochromator with OmniSpec USB drivers. And, the server communicates the instructions through Python commands.

<p align="center">
<img src="imgs/principle.png" alt="principle_driver" width="500"/>
</p>

> **_NOTE:_** Up to now, the computer where the server is hosted is running on Windows OS. 

## Installation ##

Please follow these steps:

Install the [Microsoft .NET Framework 4.0 x64](Dependencies/Microsoft_NET_Framework/dotNetFx40_Full_x86_x64.exe).

Download the [USB driver folder](Dependencies/Driver_USB_Zolix/) for Zolix instruments. To install the driver, locate the folder path (e.g., C:\Users\\%currentuser%\Desktop\Drivers\98-2k-xp-w7) after plugging the Zolix instrument.

Install the [OmniSpec SDK setup](Dependencies/OmniSpec/setup.exe).

Install the [Zolix server](Dependencies/Zolix_Server/Setup%20Serveur%20Zolix%20v1.0.0.exe).

Download the [Zolix gateway library](Dependencies/Python_Zolix_Gateway). Include it into your Python folder. 

## Quick start ##

### Launch the server connection ###

First, make sure that the Zolix monochromator is connected to the PC. And, make sure it has been turned on.

Run the Zolix server by double clicking on the icon Serveur Zolix.

<p align="center">
<img src="imgs/server_app.PNG" alt="server_app" width="400"/>
</p>
After lauching the Zolix server, click on the "démarrer" button in the user interface.

<p align="center">
<img src="imgs/server_gui.png" alt="server_gui" width="600"/>
</p>

The server communication is now working.

> **_NOTE:_** Up to now, the user interface of the Zolix server is in French. We are implementing an English version. 

### Communicate using Python ###

You can first communicate with the Zolix monochromator using the [example python script](Dependencies/Python_Zolix_Gateway/zolix/app/example.py) and follow the instructions.

Then, you can use more functions available in the library [zolix/app folder](Dependencies/Python_Zolix_Gateway/zolix/app). More information about these functions can be retrieved here [EN-OperationManual_ZolixOmniSpec](documentation/EN-OperationManual_ZolixOmniSpec.pdf)

## Funding ##

This project was partially funded by FEDER (grant number 1110/EU001051/00065007) and by Région Bretagne.

## About us ##

Photonics Bretagne is a research and technology organisation (RTO), based in Lannion (France). In partnership with Arvalis institute, the biophotonic team of Photonics Bretagne aims at increasing the development of light-based technologies for life sciences such as agriculture, biomedical, agri-food, and environment. More information are available on our [website](https://www.photonics-bretagne.com/en/about-photonics-bretagne/).

In France, Zolix instruments are distributed by [Idil Fibres Optiques](https://www.idil-fibres-optiques.com/fr/product/zolix-instruments-france-2/).
