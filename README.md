#How I Fight Slavery
####By
###Eric Schles

##Intro - The Problem

* [A personal story](http://www.cracked.com/article_21538_5-things-i-learned-as-sex-slave-in-modern-america.html)
* [some statistics](http://www.havocscope.com/tag/human-trafficking/)

* In case you are interested:
	* [international statistics](http://www.unodc.org/unodc/en/human-trafficking/global-report-on-trafficking-in-persons.html)
	* [statistics - polaris project](http://www.traffickingresourcecenter.org/material-type/statistics)


##Some solutions 
* [Manhattan DA](http://manhattanda.org/human-trafficking-0)

* [DARPA](http://www.scientificamerican.com/article/human-traffickers-caught-on-hidden-internet/)

##My Toy:  Investa_gator 

Investa_gator makes use of machine learning, web scraping, and internal knowledge to find instances of human trafficking.  The assumption is law enforcement is getting the information it needs, hence this tool will help find more instances in order to build a case against those assumed to be traffickers.

##How to start the server:

python run.py 

(run.py can be found at the top level directory)

##Example non gross website to test out:

http://newyork.backpage.com/AdultJobs/midtown-spa-looking-for-nice-girls/36076717

##What you'll need to run my code:

[syncano v3](https://github.com/Syncano/syncano-python)

--Simply fork the repo and install OR enter a terminal and type `sudo pip install syncano --pre`

[requests](http://docs.python-requests.org/en/latest/)

--install with `sudo pip install requests`

[flask](http://flask.pocoo.org/)

--install with `sudo pip install flask`

[lxml](http://lxml.de/)

--install with `sudo pip install lxml`

[unidecode](https://pypi.python.org/pypi/Unidecode)

--install with `sudo pip install unidecode`

[textblob](http://textblob.readthedocs.org/en/dev/)

--install with [these instructions](http://stevenloria.com/how-to-build-a-text-classification-system-with-python-and-textblob/)

[postmark](https://postmarkapp.com/)

--install with `sudo pip install python-postmark` - this is a future dependency :)



