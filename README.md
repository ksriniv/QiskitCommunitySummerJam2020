## Q4CMusic - Quantum Computing for Carnatic Music

An open source Quantum Computing Application to generate patterns for mridangam

To learn more about Carnatic music : [Click Here](https://en.wikipedia.org/wiki/Carnatic_music)

To learn more about mridanagam : [Click Here](https://en.wikipedia.org/wiki/Mridangam)

### Prerequisites

OS - Ubuntu 18.04 LTS or higher

Python 3.7 

Qiskit - Information about Qiskit can be found [here](https://qiskit.org)

Information about installing Qiskit can be found [here](https://qiskit.org/documentation/install.html)

Pyglet Open source application for media play back - Information about Pyglet can be found [here](https://www.programsinformationpeople.org/runestone/static/publicPIP/Pyglet/Pyglet.html) 

To install Pyglet:
```
pip3 install pyglet
```

Note that pyglet needs to be callable from the Anaconda environment that runs QisKit.

### Application

#### To run the application

1.  Use `git clone` to clone this repository into your Anaconda environment
2.  Change directory into the application and run
    ```    
    python3 Application.py <NumberofStrokes> <Loop>
    ```

For example:
  ```
  python3 Application.py 8 4
  ```    
will generate 8 strokes and repeat the pattern 4 times.

#### Usage

The application can take 2 arguments from the command line.  


Argument 1 : Number of Strokes to generate within the range (1 - 32)

Argument 2 : How many times to repeat the generated pattern (1 - MAXINT)


### Disclaimer

This application has been only tested on Ubuntu 18.04 LTS and Python 3.7. Testing for other OS environments are in progress.



 
