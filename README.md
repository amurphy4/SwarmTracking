# SwarmTracking
Swarm robot tracking system - developed for use by the Swarm Lab at the University of Plymouth

# Getting Started
These instructions will show how to import this module and use this module

### Prerequisites
OpenCV 4.0 is required in order to identify the ArUco tags. ArUco detection a contrib module, and not included within base OpenCV
```
pip install opencv-contrib-python
```

### Installation
Clone/download this repository to the folder containing your project code

-OR-

Clone/download this repository to anywhere, then add its location to the PYTHONPATH in Terminal (macOS/GNU Linux)
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/this/repository"
```


### Usage
Import the TrackingController
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

NOTE: Any changes made to `new_tc` will also affect `tc`

`TrackingController` requires a callback method in order to return data about the bots, this can be set using the `set_callback()` method
```python
def callback(bots):
  # Handle data processing here
  
def main():
  tc = TrackingController.getInstance()
  
  tc.set_callback(callback)
```

`TrackingController` runs a thread to track the ArUco tags in the background, assessing each camera frame at 30fps. Starting and stopping the thread can be done as follows
```python
# Start the tracking thread
tc.start()

# Stop the tracking thread
tc.stop()

# Run the tracking thread for one frame only
tc.once()
```
