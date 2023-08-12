import sys
import requests
from colorama import init, Fore

class WAFs:
    def __init__(self):
        self.cloudflare = "https://www.cloudflare.com/favicon.ico"
        self.akamai = "https://www.akamai.com/site/favicon/favicon.ico"
        self.aws = "https://docs.aws.amazon.com/favicon.ico"
        self.imperva = "https://www.imperva.com/favicon.ico"
        self.f5 = "https://www.f5.com/favicon.ico"
        self.cloudflare_error = "Attention Required!"
        self.akamai_error = "Denied"
        self.aws_error = "Request blocked"
        self.imperva_error = "unsuccessful"
        self.f5_error = "Request Rejected"

def banner():
    print(Fore.LIGHTMAGENTA_EX + r"""
                 XOOkxdddddxxkOKXN
             NKkdo:loooooooooooo:lkK
           Nkooooo:loooooooooooo::oookX
         Nklc;ccccccccccccc:cccccccccclO
        Ndooo;loooooooooooo:oooooooooooodX
       Xdoooo;lod0KXXNN    NNXK0OdooooooocX
       occccc:cc0          NN        ccd
      OoooooooooO          XKX        loooooooX
      xoooooooood         XKKKXXN     cclloooooO
      xlllllcclllO       XKKKKKKX    cclllcllclO
      0oooool:ooooK      NXKKXN     Occccccccl:oX
      Ndooool:oooooO      N          x
       Xolllc;cllllclO   N            x
        Xdllllllllll:llxK0xccccccc;cccccoX
          Oooooooooo:oolcccccccccc:cccckN
           Nkooooool:loolccccccccc;clxX
             NOdllllllllllc::::::ldOX
                 X0Okxddddoldxk0KN

              [Test This WAF - v1.0]
                   [by AmoloHT]
""" + Fore.RESET)

def help():
    print("""\
usage: ttwaf [-h] --all ALL --bypassed VALIDS

options:
  -h, --help            show this help message and exit
  --all ALL,            show all
  --bypassed VALIDS     show only valid ones
""")

def make_req():
    waf = WAFs()
    init()  # Initialize colorama

    for arg in sys.argv:
        if arg == "-h" or arg == "--help":
            help()

        if arg == "--bypassed":
            for line in sys.stdin:
                line = line.strip()
                url_akamai = f"{waf.akamai}?a={line}"
                r_akamai = requests.get(url_akamai)
                r_akamai_text = r_akamai.text

                url_cloudflare = f"{waf.cloudflare}?a={line}"
                r_cloudflare = requests.get(url_cloudflare)
                r_cloudflare_text = r_cloudflare.text

                url_aws = f"{waf.aws}?a={line}"
                r_aws = requests.get(url_aws)
                r_aws_text = r_aws.text

                url_f5 = f"{waf.f5}?a={line}"
                r_f5 = requests.get(url_f5)
                r_f5_text = r_f5.text

                if waf.akamai_error not in r_akamai_text:
                    print(Fore.GREEN + f"[+] Akamai: Accepted [{line}]" + Fore.RESET)

                if waf.aws_error not in r_aws_text:
                    print(Fore.GREEN + f"[+] AWS: Accepted [{line}]" + Fore.RESET)

                if waf.cloudflare_error not in r_cloudflare_text:
                    print(Fore.GREEN + f"[+] Cloudflare: Accepted [{line}]" + Fore.RESET)

                if waf.f5_error not in r_f5_text:
                    print(Fore.GREEN + f"[+] F5: Accepted [{line}]" + Fore.RESET)
        
        if arg == "--all":
            for line in sys.stdin:
                line = line.strip()
                url_akamai = f"{waf.akamai}?a={line}"
                r_akamai = requests.get(url_akamai)
                r_akamai_text = r_akamai.text

                url_cloudflare = f"{waf.cloudflare}?a={line}"
                r_cloudflare = requests.get(url_cloudflare)
                r_cloudflare_text = r_cloudflare.text

                url_aws = f"{waf.aws}?a={line}"
                r_aws = requests.get(url_aws)
                r_aws_text = r_aws.text

                url_f5 = f"{waf.f5}?a={line}"
                r_f5 = requests.get(url_f5)
                r_f5_text = r_f5.text

                if waf.akamai_error in r_akamai_text:
                    print(Fore.RED + f"[-] Akamai: Denied [{line}]" + Fore.RESET)
                else:
                    print(Fore.GREEN + f"[+] Akamai: Accepted [{line}]" + Fore.RESET)

                if waf.aws_error in r_aws_text:
                    print(Fore.RED + f"[-] AWS: Denied [{line}]" + Fore.RESET)
                else:
                    print(Fore.GREEN + f"[+] AWS: Accepted [{line}]" + Fore.RESET)

                if waf.cloudflare_error in r_cloudflare_text:
                    print(Fore.RED + f"[-] Cloudflare: Denied [{line}]" + Fore.RESET)
                else:
                    print(Fore.GREEN + f"[+] Cloudflare: Accepted [{line}]" + Fore.RESET)

                if waf.f5_error in r_f5_text:
                    print(Fore.RED + f"[-] F5: Denied [{line}]" + Fore.RESET)
                else:
                    print(Fore.GREEN + f"[+] F5: Accepted [{line}]" + Fore.RESET)

if __name__ == "__main__":
    banner()
    while True:
        try:
            make_req()
        except:
            print(Fore.RED + "[-] There was a problem" + Fore.RESET)
        break
