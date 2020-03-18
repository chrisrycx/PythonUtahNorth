## Equipment
- MDL
- Raspberry Pi
- CSI Logger
- TPH sensor
- RMYoung
- SP-110
- RS485-USB
- Dyacon Laptop w/ converter

## Outline
- What is a datalogger?
    - A device that communicates with sensors and records data.
    - Demo: Different examples of dataloggers and features
        - Interfacing to different devices (MDL, Pi, CSI)
    - Demo: Different kinds of sensors
    - Demo: Reading and logging a sensor using Modbus Reader
    - Typical datalogger features
        - Table:
- Databear
    - Open-source, Python based datalogger software.
        - Hardware independent
        - Easily configured
    - Features so far
        - Table:
    - Installation/Configuration
        - Demo: Databear repository, pip install to windows
        - Demo: Configuration with YAML
        - Demo: Databear on Raspberry Pi
    - Code overview
        - Schedule library
        - Sensor interface
            - Optional Demo: Code RMYoung interface
            - Factory method
        - Processing
        - Output CSV
    - Issues
        - Threading
        - Measurement timing
- Open source projects
    - Packaging code - structure and workflow
        - Local benefits - paths
    - PYPI - accounts
    - Deploying to PYPI
    - Demo: Deploy to test PYPI

    ### Ideal Datalogger Features vs Data Bear 1.2
| Ideal Feature                                  | Data Bear       |
| -------------                                  | ---------       |
| Can be used with multiple instruments simultaneously  | &#9745; |
| Compatible with a variety of sensor types             | &#9745; |
| Adjustable sampling rates for all measurements        | &#9745; |
| Adjustable rates of data storage                      | &#9745; |
| Concurrent measurement of all sensors                 |         |
| Store metadata associated with data values.           | &#9745; |
| Configure settings without changing code              | &#9745; |
| Error handling                                        | &#9745; |
| Data accessible by other programs (ie an LED display) |  |
| Process sensor measurements using custom algorithms (ie Average, Max, Min).  | &#9745; |
| Change sensors and settings on the fly                |  |
| Easy transfer of data off of the device.              | &#9745; |
| Control activation of equipment associated with a sensor (ie wiper, sleep).  |  |



