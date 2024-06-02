import socket

# Define the server address and port
server_address = ('localhost', 5555)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print("Choose an option:")
    print("1. BMI Calculator")
    print("2. Date and Time")
    print("3. Temperature Conversion")
    choice = input("Enter your choice (1, 2, or 3): ")

    # Send the choice to the server
    client_socket.sendto(choice.encode(), server_address)

    # Receive the response from the server
    data, _ = client_socket.recvfrom(1024)
    
    # Check if the choice is for BMI and print the appropriate prompts
    if choice == '1':
        if data.decode().startswith("Enter your height"):
            height = input("Enter your height (in cm): ")
            client_socket.sendto(height.encode(), server_address)
            weight_data, _ = client_socket.recvfrom(1024)
            if weight_data.decode().startswith("Enter your weight"):
                weight = input("Enter your weight (in kg): ")
                client_socket.sendto(weight.encode(), server_address)
                bmi_result, _ = client_socket.recvfrom(1024)
                print(f"Received from server: {bmi_result.decode()}")
                print("Press 0 for the main menu")
                choice_back = input()
                if choice_back == '0':
                    continue
        else:
            print(f"Received from server: {data.decode()}")
            print("Press 0 for the main menu")
            choice_back = input()
            if choice_back == '0':
                continue
    elif choice == '2':
        print(f"Received from server: {data.decode()}")
        print("Press 0 for the main menu")
        choice_back = input()
        if choice_back == '0':
            continue
    elif choice == '3':
        print(f"Received from server: {data.decode()}")
        option = input("Enter your temperature conversion choice (1, 2, or 3): ")
        client_socket.sendto(option.encode(), server_address)
        if option in ['1', '2', '3']:
            temp_data, _ = client_socket.recvfrom(1024)
            temperature = input(temp_data.decode())
            client_socket.sendto(temperature.encode(), server_address)
            temp_result, _ = client_socket.recvfrom(1024)
            print(f"Received from server: {temp_result.decode()}")
            print("Press 0 for the main menu")
            choice_back = input()
            if choice_back == '0':
                continue
        else:
            print("Invalid choice. Returning to the main menu.")
    else:
        print(f"Invalid choice. Please select 1, 2, or 3.")
