# Python_Wrapper_For_Zolix
Driver wrapper in Python for Omni-λ Zolix monochromator

OS: Windows 10

Python version: 3.8

## Introduction ##

Based in Beijing (China), Zolix Instruments Co. Ltd develops optical instruments for industry and research such as spectrographs, detectors and monochromators.

The [Omni-λ monochromators](http://zolix.com.cn/en/prodcon_370_376_741.html) from Zolix can be used to generate and to tune a monochromatic beam over UV to NIR in order, for example, to illuminate samples in fluorescence.

C++ and Delphi drivers allow users to control the Zolix monochromators and to design their own acquisition programs.

In this project, we implemented a Python-based driver to control the Omni-λ monochromators. This repository contains all files you need.

## Principle ##

The principle of the driver wrapper consists in using a server conected to the Omni-λ monochromator with OmniSpec USB drivers. And, the server communicates instruction through a Python code.

![principle](https://user-images.githubusercontent.com/109954983/182817681-e01ca204-67ed-4063-b23f-8a0a64f46ede.png)

> **_NOTE:_** Up to now, the computer where the server is hosted, is running on Windows OS. 

## Installation ##

Please follow these steps:

Install the Microsoft .NET Framework 4.0 using this link [dotNetFx40_Full_x86_x64](Dependencies).

Download the folder with the USB driver for Zolix instruments using this link [USB_driver_folder](Dependencies/Driver_USB_Zolix). To install the driver, locate the folder where USB driver is stored in your computer (e.g. C:\Users\%currentuser%\Desktop\Driver98-2k-xp-w7) after plugging the Zolix instrument.

Install the OmniSpec SDK setup [“Setup.exe”](Dependencies/OmniSpec-Setup).

Install the Zolix server setup using this link [Setup Serveur Zolix v1.0.0](Dependencies).

Download the Zolix gateway library using this link [zolix_gateway library](Dependencies/Python_Zolix_Gateway). Include it into your Python folder. 

## Quick start ##

### Launch the server connection ###

First, make sure that the Zolix monochromator is connected to the PC. And, make sure it has been turned on.

Run the Zolix server by double clicking on the icon Serveur Zolix.

![server_app](https://user-images.githubusercontent.com/109954983/182817992-c83d428b-ffe5-4205-83ca-6b21ee097e2d.PNG)

After lauching the Zolix server, click on the "démarrer" button in the user interface.

![server_gui](https://user-images.githubusercontent.com/109954983/182818212-74fab258-bb9d-4e29-a309-c1385cedaa43.png)

The server communication is now working.

> **_NOTE:_** Up to now, the user interface of the Zolix server is in French. We are implementing an English version. 

### Communicate using Python ###

You can first communicate with the Zolix monochromator using the example python script [example.py](Dependencies/Python_Zolix_Gateway/zolix/app) and follow the instructions. 

Then, you can use more functions available in the library zolix/app folder [zolix_gateway](Dependencies/Python_Zolix_Gateway/zolix/app). More information about these functions can be retrieved here [EN-OperationManual_ZolixOmniSpec](documentation/EN-OperationManual_ZolixOmniSpec.pdf)

## About us ##

Photonics Bretagne is a research and technology organisation (RTO), based in Lannion (France). In partnership with Arvalis institute, the biophotonic team of Photonics Bretagne aims at increasing the development of light-based technologies for life sciences such as agriculture, biomedical, agri-food, and environment. More information are available on our [website](https://www.photonics-bretagne.com/en/about-photonics-bretagne/).

In France, Zolix instruments are distributed by [Idil Fibres Optiques](https://www.idil-fibres-optiques.com/fr/product/zolix-instruments-france-2/).
