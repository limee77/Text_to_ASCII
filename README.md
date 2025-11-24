# Plain text to ASCII Microservice
Microservice that converts plain text to ASCII (currently only supports font='slant')

To run:
```
python3 -m venv myenv 
source myenv/bin/activate
pip install zmq pyfiglet  
```
Terminal 1:\
`python3 ASCII.py`

Terminal 2:\
`python3 test_client.py`

