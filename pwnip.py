from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
import requests
import whois
import socket
import os

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

def whois_lookup(domain_or_ip):
    try:
        w = whois.whois(domain_or_ip)
        table = Table(title=f"PwnIP - WHOIS Lookup: {domain_or_ip}")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="magenta")
        for key, value in w.items():
            table.add_row(str(key), str(value))
        console.print(table)
    except Exception as e:
        console.print(f"[red]WHOIS hatası: {e}[/red]")

def reverse_dns(ip):
    try:
        host = socket.gethostbyaddr(ip)
        console.print(f"[green]PwnIP - Reverse DNS: {host[0]}[/green]")
    except Exception as e:
        console.print(f"[red]Reverse DNS hatası: {e}[/red]")



def clear():
    os.system('clear')



def main():
    while True:
        clear()
        console.print(Panel.fit("[bold yellow]PwnIP v1.0[/bold yellow]\nBy: Kanka Labs", title="[bold green]Ana Menü[/bold green]"))
        console.print("\n[cyan]1.[/cyan] IP Lookup")
        console.print("[cyan]2.[/cyan] WHOIS Lookup")
        console.print("[cyan]3.[/cyan] Reverse DNS")
        console.print("[cyan]4.[/cyan] Çıkış")
        
        choice = Prompt.ask("Seçiminiz", choices=["1","2","3","4"])
        
        if choice == "1":
            ip = Prompt.ask("IP adresini gir")
            ip_lookup(ip)
        elif choice == "2":
            domain = Prompt.ask("Domain veya IP gir")
            whois_lookup(domain)
        elif choice == "3":
            ip = Prompt.ask("IP adresini gir")
            reverse_dns(ip)
        elif choice == "4":
            console.print("[bold red]Çıkış yapılıyor...[/bold red]")
            break
        
        console.print("\n[bold green]Devam etmek için Enter tuşuna basın...[/bold green]")
        input()


if _name_ == "_main_":
    main()
