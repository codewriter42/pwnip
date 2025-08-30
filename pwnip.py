from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
import requests
import socket
import os
import subprocess

console = Console()


def ip_lookup(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,isp,org,query,as"
    try:
        res = requests.get(url, timeout=5).json()
        if res['status'] == 'success':
            table = Table(title=f"PwnIP - IP Lookup: {ip}")
            table.add_column("Field", style="cyan", no_wrap=True)
            table.add_column("Value", style="magenta")
            for key in ['query','country','regionName','city','isp','org','as']:
                table.add_row(key, str(res[key]))
            console.print(table)
        else:
            console.print(f"[red]IP sorgusu başarısız: {res['message']}[/red]")
    except Exception as e:
        console.print(f"[red]Hata: {e}[/red]")

def reverse_dns(ip):
    try:
        host = socket.gethostbyaddr(ip)
        console.print(f"[green]PwnIP - Reverse DNS: {host[0]}[/green]")
    except Exception as e:
        console.print(f"[red]Reverse DNS hatası: {e}[/red]")


def port_scan(ip, start_port=1, end_port=1024):
    console.print(f"[bold yellow]Scanning {ip} ports {start_port}-{end_port}...[/bold yellow]")
    open_ports = []
    for port in range(start_port, end_port+1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass
    if open_ports:
        table = Table(title=f"Open Ports on {ip}")
        table.add_column("Port", style="cyan")
        for port in open_ports:
            table.add_row(str(port))
        console.print(table)
    else:
        console.print(f"[red]No open ports found on {ip}[/red]")


def wifi_users(subnet="192.168.1."):
    console.print(f"[bold yellow]Scanning devices on subnet {subnet}0/24...[/bold yellow]")
    alive_hosts = []
    for i in range(1, 255):
        ip = f"{subnet}{i}"
        try:
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1", ip],
                stdout=subprocess.DEVNULL
            )
            if result.returncode == 0:
                alive_hosts.append(ip)
        except:
            pass
    if alive_hosts:
        table = Table(title="Devices Found in Wi-Fi")
        table.add_column("IP Address", style="magenta")
        for host in alive_hosts:
            table.add_row(host)
        console.print(table)
    else:
        console.print("[red]No devices found on the network[/red]")


def clear():
    os.system('clear')


def main():
    while True:
        clear()
        console.print(Panel.fit("[bold yellow]PwnIP v1.1[/bold yellow]\nBy: codewriter42", title="[bold green]Main Menu[/bold green]"))
        console.print("\n[cyan]1.[/cyan] IP Lookup")
        console.print("[cyan]2.[/cyan] Reverse DNS")
        console.print("[cyan]3.[/cyan] Port & Network Tools")
        console.print("[cyan]4.[/cyan] Exit")

        choice = Prompt.ask("Choose", choices=["1","2","3","4"])

        if choice == "1":
            ip = Prompt.ask("Enter IP")
            ip_lookup(ip)

        elif choice == "2":
            ip = Prompt.ask("Enter IP")
            reverse_dns(ip)

        elif choice == "3":
            while True:
                clear()
                console.print(Panel.fit("[bold yellow]Port & Network Tools[/bold yellow]", title="[bold green]Sub Menu[/bold green]"))
                console.print("\n[cyan]1.[/cyan] Port Scan")
                console.print("[cyan]2.[/cyan] Wi-Fi Users Discovery")
                console.print("[cyan]3.[/cyan] Back")

                sub_choice = Prompt.ask("Choose", choices=["1","2","3"])
                if sub_choice == "1":
                    ip = Prompt.ask("Enter target IP")
                    port_scan(ip)
                    input("\nPress Enter to continue...")
                elif sub_choice == "2":
                    subnet = Prompt.ask("Enter subnet (default 192.168.1.)", default="192.168.1.")
                    wifi_users(subnet)
                    input("\nPress Enter to continue...")
                elif sub_choice == "3":
                    break

        elif choice == "4":
            console.print("[bold red]Exiting...[/bold red]")
            break

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
