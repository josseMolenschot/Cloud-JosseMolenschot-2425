import ipaddress
import math
import pandas as pd

def calculate_subnet_info(number_of_hosts):
    try:
        # Validate input type
        if not isinstance(number_of_hosts, int):
            raise ValueError("The input must be an integer.")
        
        # Validate the number of hosts
        if not (2 <= number_of_hosts <= 250):
            raise ValueError("The number of hosts must be between 2 and 250.")

        # Calculate required subnet prefix
        needed_bits = math.ceil(math.log2(number_of_hosts + 2))  # +2 for network and broadcast addresses
        prefix_length = 32 - needed_bits
        subnet_mask = str(ipaddress.IPv4Network(f'0.0.0.0/{prefix_length}').netmask)
        total_addresses = 2 ** needed_bits
        usable_addresses = total_addresses - 2 if total_addresses > 2 else 0

        # Base network: 192.168.0.0/24
        base_network = ipaddress.IPv4Network("192.168.0.0/24", strict=False)
        subnets = list(base_network.subnets(new_prefix=prefix_length))

        # Prepare subnet data for Excel output
        subnet_data = []
        for subnet in subnets:
            first_host = str(next(subnet.hosts()))
            last_host = str(list(subnet.hosts())[-1])
            broadcast_address = str(subnet.broadcast_address)
            subnet_data.append({
                "Subnet": str(subnet),
                "Network Address": str(subnet.network_address),
                "First Host": first_host,
                "Last Host": last_host,
                "Broadcast Address": broadcast_address,
                "Total Addresses": total_addresses,
                "Usable Addresses": usable_addresses,
                "Subnet Mask": subnet_mask,
                "Prefix Length": prefix_length
            })

        # Save to Excel
        df = pd.DataFrame(subnet_data)
        excel_file = "subnet_details.xlsx"
        df.to_excel(excel_file, index=False)
        print(f"Subnet details saved to {excel_file}.")

        # Print the first subnet's details as an example
        first_subnet = subnet_data[0]
        print("Example Subnet Information:")
        print(f"Subnet Mask: {first_subnet['Subnet Mask']}")
        print(f"Prefix Length: /{first_subnet['Prefix Length']}")
        print(f"Total Addresses: {first_subnet['Total Addresses']}")
        print(f"Usable Addresses: {first_subnet['Usable Addresses']}")
        print(f"Network Address: {first_subnet['Network Address']}")
        print(f"First Host: {first_subnet['First Host']}")
        print(f"Last Host: {first_subnet['Last Host']}")
        print(f"Broadcast Address: {first_subnet['Broadcast Address']}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # User input for the number of hosts
    try:
        num_hosts = int(input("Enter the number of hosts required (between 2 and 250): "))
        calculate_subnet_info(num_hosts)
    except ValueError:
        print("Please enter a valid integer for the number of hosts.")
