import ipaddress
import random

def random_ip():
    rfc1918 = [
        ("10.0.0.0",8),
        ("172.16.0.0",12),
        ("192.168.0.0",16)
    ]

    ip, prefix = random.choice(rfc1918)


    # random prefix
    cidr = random.randint(prefix + 1,30)

    # Generate network within the range
    network = ipaddress.ip_network(f"{ip}/{prefix}",strict=False)
    ip_int = int(network.network_address) + random.randint(1,network.num_addresses - 2)
    ip_rnd = ipaddress.IPv4Address(ip_int)
    

    return ip_rnd, cidr


def test():
    ip, cidr = random_ip()
    subnet = ipaddress.ip_network(f"{ip}/{cidr}",strict=False)

    print("\nTest your subnetting skills\n")
    print(f"IP Address: {ip}")
    print(f"Subnet Mask: /{cidr} ({subnet.netmask})")

    user_net_id = input(("What is the Network ID? "))
    user_broadcast = input("What is the Broadcast Address? ")
    user_first_host = input("What is the First Usable IP? ")
    user_last_host = input("What is the Last Usable IP? ")
    print("\n")

    # correct answers
    correct_net_id = str(subnet.network_address)
    correct_broadcast = str(subnet.broadcast_address)
    hosts = list(subnet.hosts())
    correct_first = str(hosts[0])
    correct_last = str(hosts[-1])

    if user_net_id == correct_net_id:
        print("Network ID: Correct")
    else:
        print("Network ID: Incorrect")
    
    if user_broadcast == correct_broadcast:
        print("Broadcast: Correct")
    else:
        print("Broadcast: Incorrect")
    
    if user_first_host == correct_first:
        print("First Usable IP: Correct")
    else:
        print("First Usable IP: Incorrect")
    
    if user_last_host == correct_last:
        print("Last Usable IP: Correct")
    else:
        print("Last Usable IP: Incorrect")
    

def main():
    print("Welcome to the IP Subnetting Practice Tool:")
    while True:
        test()
        do_it_again = input("\n Do another? (y/n) ").strip().lower()

        if do_it_again != "y":
            print("\nBYE!!\n")
            break

if __name__ == "__main__":
    main()


