#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  logo.py


import random

NoMoney_fonts = [
    r"""
   /$$   /$$           /$$      /$$                                        
  | $$$ | $$          | $$$    /$$$                                        
  | $$$$| $$  /$$$$$$ | $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$
  | $$ $$ $$ /$$__  $$| $$ $$/$$ $$ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$
  | $$  $$$$| $$  \ $$| $$  $$$| $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  | $$
  | $$\  $$$| $$  | $$| $$\  $ | $$| $$  | $$| $$  | $$| $$_____/| $$  | $$
  | $$ \  $$|  $$$$$$/| $$ \/  | $$|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$
  |__/  \__/ \______/ |__/     |__/ \______/ |__/  |__/ \_______/ \____  $$
                                                                  /$$  | $$
                                                                 |  $$$$$$/
                                                                  \______/ 
    """,
    r"""
    _   _           __  __                                
   | \ | |         |  \/  |                               
   |  \| |   ___   | \  / |   ___    _ __     ___   _   _ 
   | . ` |  / _ \  | |\/| |  / _ \  | '_ \   / _ \ | | | |
   | |\  | | (_) | | |  | | | (_) | | | | | |  __/ | |_| |
   |_| \_|  \___/  |_|  |_|  \___/  |_| |_|  \___|  \__, |
                                                     __/ |
                                                    |___/ 
    """,
    r"""
        ___           ___           ___           ___           ___           ___                 
       /__/\         /  /\         /__/\         /  /\         /__/\         /  /\          ___   
       \  \:\       /  /::\       |  |::\       /  /::\        \  \:\       /  /:/_        /__/|  
        \  \:\     /  /:/\:\      |  |:|:\     /  /:/\:\        \  \:\     /  /:/ /\      |  |:|  
    _____\__\:\   /  /:/  \:\   __|__|:|\:\   /  /:/  \:\   _____\__\:\   /  /:/ /:/_     |  |:|  
   /__/::::::::\ /__/:/ \__\:\ /__/::::| \:\ /__/:/ \__\:\ /__/::::::::\ /__/:/ /:/ /\  __|__|:|  
   \  \:\~~\~~\/ \  \:\ /  /:/ \  \:\~~\__\/ \  \:\ /  /:/ \  \:\~~\~~\/ \  \:\/:/ /:/ /__/::::\  
    \  \:\  ~~~   \  \:\  /:/   \  \:\        \  \:\  /:/   \  \:\  ~~~   \  \::/ /:/     ~\~~\:\ 
     \  \:\        \  \:\/:/     \  \:\        \  \:\/:/     \  \:\        \  \:\/:/        \  \:\
      \  \:\        \  \::/       \  \:\        \  \::/       \  \:\        \  \::/          \__\/
       \__\/         \__\/         \__\/         \__\/         \__\/         \__\/                
    """,
    r"""
    _  _         __  __                           
   | \| |  ___  |  \/  |  ___   _ _    ___   _  _ 
   | .` | / _ \ | |\/| | / _ \ | ' \  / -_) | || |
   |_|\_| \___/ |_|  |_| \___/ |_||_| \___|  \_, |
                                             |__/ 
    """,
    r"""
   ███▄    █  ▒█████   ███▄ ▄███▓ ▒█████   ███▄    █ ▓█████ ▓██   ██▓
   ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀  ▒██  ██▒
  ▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒▒███     ▒██ ██░
  ▓██▒  ▐▌██▒▒██   ██░▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄   ░ ▐██▓░
  ▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░░▒████▒  ░ ██▒▓░
  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ██▒▒▒ 
  ░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░ ▓██ ░▒░ 
     ░   ░ ░ ░ ░ ░ ▒  ░      ░   ░ ░ ░ ▒     ░   ░ ░    ░    ▒ ▒ ░░  
           ░     ░ ░         ░       ░ ░           ░    ░  ░ ░ ░     
                                                             ░ ░     
    """,
    r"""
  888b    888          888b     d888                                     
  8888b   888          8888b   d8888                                     
  88888b  888          88888b.d88888                                     
  888Y88b 888  .d88b.  888Y88888P888  .d88b.  88888b.   .d88b.  888  888 
  888 Y88b888 d88""88b 888 Y888P 888 d88""88b 888 "88b d8P  Y8b 888  888 
  888  Y88888 888  888 888  Y8P  888 888  888 888  888 88888888 888  888 
  888   Y8888 Y88..88P 888   "   888 Y88..88P 888  888 Y8b.     Y88b 888 
  888    Y888  "Y88P"  888       888  "Y88P"  888  888  "Y8888   "Y88888 
                                                                     888 
                                                                Y8b d88P 
                                                                 "Y88P"  
    """
]


def PrintLogo():
    print(random.choice(NoMoney_fonts))
    print('\033[1;35mNoMoney running: \033[0m')
