def main():
    # Given values
    L = int(input("Packet length in bytes = "))  # Packet length in bytes
    R = float(input("Transmission rate in bits per second = "))  # Transmission rate in bits per second
    d1 = int(input("Length of the first link in kilometers = "))  # Length of the first link in kilometers
    d2 = int(input("Length of the second link in kilometers = "))  # Length of the second link in kilometers
    d3 = int(input("Length of the third lin in kilometers = "))  # Length of the third lin in kilometers
    s = float(input("Propagation speed in meters per second = "))  # Propagation speed in meters per second
    d_proc = 3  # Processing delay in milliseconds

    # Transmission delay calculation for each link
    d_trans_1 = (L * 8) / R
    d_trans_2 = (L * 8) / R
    d_trans_3 = (L * 8) / R
    # Propagation delay calculation for each link
    d_prop_1 = (d1 * 10**3) / s
    d_prop_2 = (d2 * 10**3) / s
    d_prop_3 = (d3 * 10**3) / s

    # Total transmission delay
    total_trans_delay = (d_trans_1 + d_trans_2 + d_trans_3)*1000
    print(f"Total transmission delay = {round(total_trans_delay,2)} milliseconds")
    # Total propagation delay
    total_prop_delay = (d_prop_1 + d_prop_2 + d_prop_3)*1000
    print(f"Total propagation delay = {round(total_prop_delay,2)} milliseconds")
    # Total processing delay
    total_proc_delay = 2 * d_proc 
    print(f"Total processing delay = {round(total_proc_delay,2)} milliseconds")
    # Total end-to-end delay
    total_end_to_end_delay = total_trans_delay + total_prop_delay + total_proc_delay

    print(f"Total end-to-end delay of the packet: {round(total_end_to_end_delay,2)} milliseconds")
    
if __name__ == "__main__":
    main()

