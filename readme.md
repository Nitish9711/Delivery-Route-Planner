# **QuickToll**

#### *An autotmatice Toll System*

</br>

![Toll System](Website/static/img/2.jpg)

## Table of Contents

- [**QuickToll**](#quicktoll)
  - [*An autotmatice Toll System*](#an-autotmatice-toll-system)
  - [Table of Contents](#table-of-contents)
  - [demo](#demo)
  - [About](#about)
  - [Installation Prerequisites](#installation-prerequisites)
  - [How to Run this Project](#how-to-run-this-project)
  - [Contributors](#contributors)

## demo

[Click Here to See the PPT](https://drive.google.com/file/d/1jW2ijnGPyzz21Du5PvrWpJDr2dBdprRz/view?usp=sharing)
[Click Here to See the DEMO VIDEO](https://drive.google.com/file/d/1YGqgEKVqMO1hXLBKZKEgxSOJsFISC_IQ/view?usp=sharing)

## About

Traffic congestions at toll booths are a phenomenon noticed at all tollbooths situated between major cities around the world. Traffic conjunction nearby toll stations cause wastage of time due to large queues and a large amount of air and sound pollution.

The main objective of this Automatic toll system is to implement a user-friendly stop free system where you don’t have to stop at the toll plaza in-order to manually pay the toll fee which in order saves time and reduces traffic conjunction which wastes a lot of journey time and fuel.

This Project has the following functionalities :

* *Vehicle Number Plate is detected by Deep Learning Model Trained.

- The users  can register their  complaints about anything to the admin.
- the users  can pay the toll tax online using the website.

This program detects and extract the Vehicle Number using TESSERACT OCR ENGINE. Image undergoes different operations to extract the image.
</br>
</br>

1. First it take image as input.

   ![Sample image](assets/3.jpg)
   <br>
2. Then it detects number plate and crop it.

   ![Plate Detection](assets/1.png)
   <br>
3. Then it passes the image for processing as follows to extract vehicle Number.

   ![Number Plate Processing](assets/2.png)
   <br>
4. Website User Login Page

   ![Website Login Page](assets/4.png)
   <br>
5. Payment Page

   ![Website Payment Page](assets/5.png)
   <br>
   </br>

## Installation Prerequisites

- python

> To Download python  [Go to the python Download Website](https://www.python.org/downloads/).

- Tesseract

> To install Tesseract 32 bit version click on the [link](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20200328.exe)

> To install Tesseract 64 bit version click on the [link](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe)

- Mongodb

> To install Mongodb [Go to this Website](https://docs.mongodb.com/manual/administration/install-community/)

- Paypal accounts

> Create Paypal sandbox developer account and make two different sandbox accounts one business and one personal.
> Now create a new project via dashboard and copy and paste client_Id key and client sceret key in ``` Website/app.py```.

- Prequisites Folders

> To download models and datasets click on the [link](https://drive.google.com/drive/folders/1Do0C_qO-JSEAD6Nw98XP3o8HJ21IagS2?usp=sharing)
>>>Download the QuickToll Prequisites folder.
>>> Extract the folder and paste all the folder inside it in number_plate folder(models, logs, train, weight).

---

## How to Run this Project

1. Clone this Repo to your Local Machine.
2. Open The Terminal/CMD in the folder QuickToll.
3. Type ```py -m pip install -r requirements.txt' ```to install all the required libraries.
4. Enter your mail id and password in ```Website/config.json``` and ```number_plate/config.json ```.
5. Now create a new project via dashboard and copy the paste client_Id key.
6. Type ```mongod``` in your Terminal to Run mongodb Server (Ignore if already Running).
7. To Detect number plate.
   a. Open terminal in the root folder.
   b. Type ```cd number_plate``` and hit enter.
   c. Type ```python main.py ``` and run.

## Contributors

[Nitish Kumar](https://github.com/Nitish9711)

[Naveen Kumar](https://github.com/Rajat10Kumar)
