
                                  xx
                               xxx xx
                             xxx    x
                            xx      x                   xxx xxxxxxxx            xxx
                            x      x                xxxxx           x          xx
                            x      x             xxx                          x
                            x      x        xxxx                             xx
                             xxxx  x   xxxxx                                 x
                                xxxxxxx                                     x
                                                                           xx
                                 x                                         x
       xxxxxxxx       x                                                    x
      xx    xx        x         x                                         x
     xx     x        x         x                                          x
    xx     xx       xx        xxxxxxxx                                   xx
 xxx       x       xx         x              xxxxx       xxxxxxx         x
          xx      xx        x              xxx   xx    xxx     x  xxx   x
          x       x        x              xx      x   xx      xx xx xx  x
          x      x        x              x       xx  xx      xx xx   xx x
          x    xx         x              x    xxx   xx     xxx  x     xxx
          xx xxx        xx                xxxxx     xx   xxx    x     xxx
           xxx         xx                            xxxxx      xx  xxxx
                                                                 xxxxxx
                                                                           xxxxxxxxx
                xxxxxx                                          xxxxxxxxxxx         xx
          xxxxxx                                      xxxxxxxxxx                    xx
        xxx                             xxxxxxxxxxxxxx                            xxx
        x                     xxx xxxxxx                                      xxxx
        xxxxx        xxxxxxx x                                             xxxx
            xxxxxxxxx

-------------------------------------------------------
Pre-requisites:
- Have MySQL 8.0 Installed
- Have the ufood database imported

-------------------------------------------------------

How to install pre-requisites:

Windows:
- Navigate to https://dev.mysql.com/downloads/workbench/ and install MySQL Workbench.
- After installing, create a Database called "uFood"
- Into this database, import the content from the "ufooddb.mysql" file
- In MYSQL Workbench, create a user (username = "dbread", password = "6stooges") with SELECT and UPDATE rights.

-------------------------------------------------------

To run the software, 
- Extract the "uFood.zip" file to your machine.
- Navigate to the unzipped folder
- Double-click "uFood.exe" to run the application

-------------------------------------------------------

Make commands:

- venv:        create virtual environment
- install:     install required python libraries
- installed:   print currently installed python libraries
- clean:       remove coverage reports and pycache files
- clean-doc:   deletes generated doc files
- clean-all:   deletes coverage reports, pycache files, and doc files
- unittest:    prints unittest run
- coverage:    runs unittests and prints coverage report
- pylint:      runs pylint on all files
- flake8:      runs flake8 on all files
- pdoc:        generates doc files
- pyreverse:   generates UML class diagrams
- radon-cc:    prints radon cc metrics
- radon-mi:    prints radon mi metrics
- radon-raw:   prints raw radon metrics
- radon-hal:   prints radon hal metrics
- lint:        runs pylint and flake8 on all files
- test:        runs pylint, flake8, and then generates coverage report

=======================================================

ENJOY!