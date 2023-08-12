<h1 align="center">「🧱」About TTWAF (py)</h1>

<p align="center"><img src="assets/logo.png"></p>
<p align="center">[TTWAF](https://github.com/AmoloHT/TTWAF) is a tool designed for testing Web Application Firewalls (WAFs) to identify bypass vulnerabilities. It allows you to test a list of payloads including XSS, LFI, RCE, and SQLI, with the goal of finding payloads that can bypass the WAF protection.
The original version of TTWAF was implemented in Rust for faster testing. However, this section provides instructions on converting the Rust script to Python.</ṕ> 

## Usage:
Install the necessary Python packages:
pip install requests colorama
Run the script with the desired options:

    To show all responses:

    python ttwaf.py --all < payloads.txt

To show only valid responses:

python ttwaf.py --bypassed < payloads.txt

The results will be displayed in the terminal, with accepted responses shown in green and denied responses in red.


