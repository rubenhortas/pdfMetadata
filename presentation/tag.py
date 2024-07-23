from colorama import Fore, Style


class Tag:
    error: str = f"[{Style.BRIGHT}{Fore.RED}ERROR{Style.RESET_ALL}]"
    exception: str = f"[{Style.BRIGHT}{Fore.RED}EXCEPTION{Style.RESET_ALL}]"
    info: str = f"[{Style.BRIGHT}{Fore.GREEN}*{Style.RESET_ALL}]"
