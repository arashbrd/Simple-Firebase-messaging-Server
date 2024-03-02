# Simple Firebase Messaging Server

## Description

implement messaging server using Google Firebase API
in this project you can select the user and send Notification to their devices
for running this project you should add a project in firebase console at:
console.firebase.google.com
and then get key file as json for upload to your server
after that you need FCM token for users to send notification.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Pics](#pics)
## Installation

- For installing download the project: `pip install -r requirements.txt`.
- Then go to the project directory and run `python manage.py runserver`
- This Project has API in address: /api/sendmsg/
- To use API, you need:

  - 1-FCM Token:Get by device you want to send message to
  - 2-Access Token: To generate Access Token you sould have json key file downloaded from firebase.google.com
    after add your project

- Note:
  This Api works as 'TokenAuthentication' so that you should get your token from :
  api/auth-token/
  and add your Token in header of POST request as
  'Authorization: Token {your_token}'

## Usage

- For learning purposes and who want to send message notification manually using Google Firebase
- For more info please refer to : https://firebase.google.com/docs/cloud-messaging/send-message#python


## License

This project is licensed under the terms of the [MIT License](LICENSE).

## Pics

- my web panel:

![Project Image](https://github.com/arashbrd/Simple-Firebase-messaging-Server-with-django/blob/main/pics/web.png)

- guide for getting key file from google firebase:

![Project Image](https://github.com/arashbrd/Simple-Firebase-messaging-Server-with-django/blob/main/pics/get%20Private%20Key.png)
