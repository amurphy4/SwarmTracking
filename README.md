# SwarmTracking
Swarm robot tracking system - developed for use by the Swarm Lab at the University of Plymouth

# Getting Started
These instructions will show how to import this module and use this module

## Prerequisites
OpenCV 4.0 is required in order to identify the ArUco tags. ArUco detection is a contrib module, and not included within base OpenCV. OpenCV Contrib can be installed through pip
```
pip install opencv-contrib-python
```

## Installation
Clone/download this repository to the folder containing your project code

-OR-

Clone/download this repository to anywhere, then add its location to the PYTHONPATH in Terminal (macOS/GNU Linux)
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/this/repository"
```


## Usage
Import the `TrackingController`
```python
from SwarmTracking import TrackingController
```

`TrackingController` follows the Singleton design pattern, creating an instance of it can be done in one of two ways
```python
tc = TrackingController()
```

OR

```python
tc = TrackingController.getInstance()
```
Using the `getInstance()` method of `TrackingController` will return the instance if it exists, and if not it will create an instance and return it.

Attempting to invoke multiple instances of `TrackingController` will result in an error
```python
tc = TrackingController.getInstance()

new_tc = TrackingController()

Exception: Invalid invocation of singleton class "TrackingController"
```

Accessing the instance using the `getInstance()` method multiple times however will not cause an issue
```python
tc = TrackingController.getInstance()

new_tc = TrackingController.getInstance()
```

**Note: Any changes made to** `new_tc` **will also affect** `tc`

`TrackingController` requires a callback method in order to return data about the bots, this can be set using the `set_callback()` method. The callback will receive a list of the [bots](objects/bot.py) found in the frame, and the camera frame itself. Each bot in the list of bots contains the pixel co-ordinate of each corner of the ArUco tag, and the centre of the tag. The frame itself can be used for further image processing (e.g. OpenCV object detection)
```python
def callback(bots, frame):
  # Handle data processing here
  
def main():
  tc = TrackingController.getInstance()
  
  tc.set_callback(callback)
```

`TrackingController` runs a thread to track the ArUco tags in the background. Starting and stopping the thread can be done as follows
```python
# Start the tracking thread
tc.start()

# Stop the tracking thread
tc.stop()

# Run the tracking thread for one frame only
tc.once()
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
