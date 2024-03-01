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

## Installation

for installing download the project: install django and django-rest framework and google-auth packages
then go to the project directory and run 'python manage.py runserver'
this Project have API in address: api/sendmsg/
to use API you need:
1-FCM Token:Get by device yo want to send message to
2-Access Token: To generate Access Token you sould have json key file downloaded from firebase.google.com after add your project

Note:
This Api works as 'TokenAuthentication' so that you should get your token from :
api/auth-token/
and add your Token in header of POST request as 
'Authorization: Token {your_token}'


## Usage

for learning purposes

## Contributing

Guidelines for contributing to the project.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
