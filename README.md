#Test for Ready for sky

Requirements:
- Python 3.6
- virtualenv

*There is no need in preinstalled mySQL, cause I used cloud MySQL server*

##To setup server run:
`./setup.sh`

##To run server use
 `./run_server.sh`

##To run tests use
**There is no tests**

##To create or get your public_key in repo
Go to localhost:8000/?username=<your_username>
If there is no record with this username, it will be created. Else you will get
your current public_key

##P.S.
cloud MySQL can lose connection sometimes (cause it's free), so when you got error 500
just reload page.
