# FortVerify
A simple, fast, and good Captcha bot for discord made in PyCord.

# Resources needed
The things you will need is:
- The captcha library
- The PyCord library
- The Dotenv library
- VS Code (Not needed but recommended)

# How to use
If you host the bot, 1st you need to make the bot's needed roles.
The first role needed is a role called member. It is case sensitive. The role needs to be called "Member" like this:
![Member role image](https://i.imgur.com/AegzSc3.png)

The second role that is needed is a role called verifying. It is also case sensitive. It needs to be called "verifying" like this:
![verifying role image](https://i.imgur.com/W9ozfzh.png)

Then, you need to create 2 things.
The first thing you need to create is a folder called all lowercase "captcha". this is also case sensitive.
It should look like this:
![captcha folder](https://i.imgur.com/7SJMiO4.png)

After that, you need to create the env. create a file and name it ".env". It should look like this:
![environment variables](https://i.imgur.com/qsyDX2p.png)

Inside the .env, you should put this:
TOKEN=your token
it should look like this:
![token in dotenv](https://i.imgur.com/1GO55Qa.png)

Then, you should have a directory that looks like this:
![directory](https://i.imgur.com/15Qgain.png)

# Commands
``/verify - verifies the user via captcha``

# Todo
- [x] Make the bot
- [ ] Make a setup command that automatically sets the roles up for the user
