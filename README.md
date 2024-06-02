# UDP-Socket-Application

**Description:**
UDPSocketApp is a Python-based server-client application that uses UDP sockets to perform various tasks such as calculating BMI, providing the current date and time, and converting temperatures. The server listens for client requests and responds accordingly.

**Features:**
- **BMI Calculator:** Calculates BMI based on height and weight provided by the user.
- **Date and Time:** Provides the current date and time.
- **Temperature Conversion:** Converts temperatures between Celsius, Fahrenheit, and Kelvin.
- **UDP Communication:** Uses UDP protocol for client-server communication.

**Files:**
1. **server.py** - This file contains the server-side code:
    - Listens for incoming client requests.
    - Handles BMI calculation, date and time, and temperature conversion based on client requests.

2. **client.py** - This file contains the client-side code:
    - Sends user requests to the server.
    - Receives and displays responses from the server.
