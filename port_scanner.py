import socket
import argparse

COMMON_PORTS = {21 : "FTP",
                22 : "SSH",
                23 : "Telnet",
                25 : "SMTP",
                53 : "DNS",
                80 : "HTTP",
                88 : "Kerberos",
                143 : "IMAP",
                443 : "HTTPS",
                3306 : "MySQL",
                3389 : "RDP"}

def port_checker(target_ip : str, start_port : int, end_port : id, timeout : float) :

    print(f"Scanning {target_ip} from {start_port} to {end_port}")

    for port in range(start_port, end_port + 1) :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect((target_ip, port))
            service = COMMON_PORTS.get(port, "unknown")
            print(f"{port}/tcp open -> Service : {service} ")
        except (socket.timeout, ConnectionRefusedError, OSError):
            pass
        finally:
            s.close()
    print("\n Scan Finished.")

def main() :
    parser = argparse.ArgumentParser(
        description = "Simple TCP port scanner."
    )
    parser.add_argument("--ip", required=True, help="IP Address to scan")
    parser.add_argument("--start", type=int, required=True, help="Beginning port")
    parser.add_argument("--end", type=int, required=True, help="End port")
    parser.add_argument("--timeout", type=float, default=1.5, help="Timeout in seconds")

    args = parser.parse_args()

    if args.start < 1 or args.end > 65535 or args.start > args.end:
        print("Range is invalid. Provide a range between 1 and 65535, with start <= end")
        return

    port_checker(args.ip, args.start, args.end, args.timeout)

if __name__ == "__main__":
    main()