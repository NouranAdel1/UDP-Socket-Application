import socket

# Define the server address and port
server_address = ('localhost', 5555)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
server_socket.bind(server_address)

print("UDP server is listening...")

# Function to calculate BMI
def calculate_bmi(height, weight):
    try:
        height = float(height)
        weight = float(weight)
        bmi = weight / ((height / 100) ** 2)
        return f"Your BMI is: {bmi:.2f}"
    except ValueError:
        return "Invalid input. Please enter numeric values."

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)

    # Decode the received data
    choice = data.decode()

    # Perform actions based on the received choice
    if choice == '1':
        server_socket.sendto("Enter your height (in cm): ".encode(), client_address)
        height_data, _ = server_socket.recvfrom(1024)
        server_socket.sendto("Enter your weight (in kg): ".encode(), client_address)
        weight_data, _ = server_socket.recvfrom(1024)
        result = calculate_bmi(height_data.decode(), weight_data.decode())
        server_socket.sendto(result.encode(), client_address)
    elif choice == '2':
        import datetime
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        server_socket.sendto(f"Current date and time: {date_time}".encode(), client_address)
    elif choice == '3':
        server_socket.sendto("Enter temperature conversion option:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Kelvin to Celsius".encode(), client_address)
        option_data, _ = server_socket.recvfrom(1024)
        option = option_data.decode()
        if option == '1':
            server_socket.sendto("Enter temperature in Celsius: ".encode(), client_address)
            celsius_data, _ = server_socket.recvfrom(1024)
            celsius = float(celsius_data.decode())
            fahrenheit = (celsius * 9/5) + 32
            server_socket.sendto(f"The temperature in Fahrenheit is: {fahrenheit}".encode(), client_address)
        elif option == '2':
            server_socket.sendto("Enter temperature in Fahrenheit: ".encode(), client_address)
            fahrenheit_data, _ = server_socket.recvfrom(1024)
            fahrenheit = float(fahrenheit_data.decode())
            celsius = (fahrenheit - 32) * 5/9
            server_socket.sendto(f"The temperature in Celsius is: {celsius}".encode(), client_address)
        elif option == '3':
            server_socket.sendto("Enter temperature in Kelvin: ".encode(), client_address)
            kelvin_data, _ = server_socket.recvfrom(1024)
            kelvin = float(kelvin_data.decode())
            celsius = kelvin - 273.15
            server_socket.sendto(f"The temperature in Celsius is: {celsius}".encode(), client_address)
        else:
            server_socket.sendto("Invalid temperature conversion option.".encode(), client_address)
    else:
        server_socket.sendto("Invalid choice. Please select 1, 2, or 3.".encode(), client_address)
