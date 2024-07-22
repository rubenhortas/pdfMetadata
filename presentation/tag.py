from colorama import Fore, Style


class Tag:
    error = f"[{Style.BRIGHT}{Fore.RED}ERROR{Style.RESET_ALL}]"
    exception = f"[{Style.BRIGHT}{Fore.RED}EXCEPTION{Style.RESET_ALL}]"
    info = f"[{Style.BRIGHT}{Fore.GREEN}*{Style.RESET_ALL}]"
