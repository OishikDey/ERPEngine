# ERPEngine
An automated response system that sends messages to the emergency services and attracts nearby people to the injured for rescue. 
This is a project for the course ENGI 1020: Introduction to Programming.
Note: Some module file has been imported into the main code. The modules' names & docs are given below.

# Used Module
**Engi1020**: This module contains the functions to communicate with our Arduino. Docs: https://pypi.org/project/engi1020/.

**Time**: We only import the sleep function from this module to delay the program and timeout counter. Docs: https://docs.python.org/3/library/time.html.

**Logging**: This module creates a log file that describes the sensor data readings & every step implemented. Docs: https://docs.python.org/3/library/logging.html.

**Datetime**: Record the date & time of the engine initiation and step implementation (detection, alarm trigger, button press, etc.). Docs: https://docs.python.org/3/library/datetime.html.

**EngineModule**: This module contains the engine functions defined by ourselves. 

