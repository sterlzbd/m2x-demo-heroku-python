# M2X Heroku Python Demo


## Introduction

This repo provides a framework for a [Heroku](https://www.heroku.com) application with Python code that reports data to [AT&T M2X](https://m2x.att.com). The application reports the current stock price of AT&T's stock (ticker symbol "T") every minute.

Please note that the Heroku machine and M2X are using times in UTC, not in your local time zone.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Pre-Requisites

You will need to have an account on [Heroku](https://www.heroku.com/). Because this example application uses only one Heroku dyno, it should be free for you to use, no matter how many other applications you have.

You will also need an account on AT&amp;T's M2X service ([m2x.att.com](https://m2x.att.com)), which is currently free to everyone. (Future plans call for M2X to keep a free "Developer" plan, but to charge for very large volumes of data.)

You will need the [Heroku Toolbelt](https://toolbelt.heroku.com/) installed and configured with your Heroku login credentials.

## Installation

### Creating Your Application

```bash
$ git clone https://github.com/attm2x/m2x-demo-heroku-python.git
$ cd m2x-demo-heroku-python
$ heroku apps:create APPNAME
```

### M2X API Key

Next you'll need to get your M2X API Master Key. Log into M2X, and click your name in the upper right-hand corner, then the "Account Settings" dropdown, then the "Master Keys" tab. [Here's a direct link](https://m2x.att.com/account#master-keys).

Then you'll need to set the environment variable  and push the codebase to Heroku.

```bash
$ heroku config:set MASTER_API_KEY=<your_master_api_key>
$ git push heroku master
```

### Scaling Your Application
Now your code should be uploaded. However, because you're using the "Clock" process type, your code isn't running automatically. You'll need to scale the number of clock workers to 1:

```
heroku ps:scale clock=1
```

## Testing

Your stockreport.py should now be reporting the price of AT&T's stock to AT&T M2X every minute. (Please note that the NYSE is open from 9:30 AM to 4 PM Eastern Time, and the stock price reported outside those hours will not change.)

If there are any errors from stockreport.py, they will be logged via Heroku's log system. Use ```heroku logs --tail``` to see the live output from your application.

## License

This library is released under the MIT license. See ``LICENSE`` for the terms.
