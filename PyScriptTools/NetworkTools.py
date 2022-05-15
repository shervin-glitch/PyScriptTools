"""

    MIT License

    Copyright (c) 2022 Shervin Badanara

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:\n

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.\n

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    NetworkTools
    ============
    version : 4.3.5\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/

"""


try:
    import os
    import socket
    import requests
    import json
    import psutil
    import getmac
    import colorama
    import platform
    
    from .exceptions import *

except:
    raise ModuleNotFoundError


class NetworkTools:
    localIP = str(socket.gethostbyname(socket.gethostname()))
    publicIPLoader = requests.get('https://api.myip.com').content
    loadedIP = json.loads(publicIPLoader)
    publicIP = str(loadedIP['ip'])
    ipAddrs =  psutil.net_if_addrs()
    
    @classmethod
    def ShowLocalIP(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Local IP_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.localIP
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod
    def ShowPublicIP(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Public IP_
        """
        if (type(show) is bool):
            if (show is True):
                try:
                    return cls.publicIP
                except ConnectionError:
                    pass
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod
    def ShowMacAddress(cls , show : bool = False , network_request : bool = True) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.
            network_request (bool): _Use Internet To get MacAddress(better to use True)_. Defaults to True.

        Returns:
            str: _MAC Address_
        """
        if (type(show) is bool and type(network_request) is bool):
            if (show is True):
                try:
                    return getmac.get_mac_address(ip = socket.gethostbyname(socket.gethostname()) , network_request = network_request)
                except ConnectionError:
                    pass
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod
    def ShowNetworkInfo(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Shows Some of Your Network Information_
        """
        if (type(show) is bool):
            if (show is True):
                for interfaceName , interfaceAddresses in cls.ipAddrs.items():
                    for address in interfaceAddresses:
                        print(f"{colorama.ansi.Fore.GREEN}=== Interface :{colorama.ansi.Fore.MAGENTA} {interfaceName} {colorama.ansi.Fore.GREEN}===")
                        if (str(address.family) == "AddressFamily.AF_INET"):
                            print(f"{colorama.ansi.Fore.WHITE}IP Address : {address.address}")
                            print(f"Netmask : {address.netmask}")
                            print(f"Broadcast IP : {address.broadcast}")
                        elif (str(address.family) == "AddressFamily.AF_PACKET"):
                            print(f"Mac Address : {address.address}")
                            print(f"Netmask : {address.netmask}")
                            print(f"Broadcast MAC : {address.broadcast}")
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod
    def ShowSavedNetworks(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Shows Saved Networks_
        """
        if (type(show) is bool):
            if (show is True):
                if (platform.system()[0].upper() == 'W'):
                    for i in os.popen("netsh wlan show profiles"):
                        if ("All User Profile" in i):
                            i = str(i).split(":")
                            i = f"{colorama.ansi.Fore.GREEN}Network Name : {colorama.ansi.Fore.MAGENTA} {i[1].strip()}"
                            print(i)
                            continue
                else:
                    return WorksOnlyOnWindows.__doc__
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return AdminPermissionRequestDenied.__doc__
        
    @classmethod
    def ShowSavedNetworkWithPassword(cls , show : bool = False , network_name : str = '') -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Shows Saved Networks_
        """
        if (type(show) is bool):
            if (show is True):
                if (platform.system()[0].upper() == 'W'):
                    for i in os.popen(f'netsh wlan show profile name="{network_name}" key=clear'):
                        if ("Key Content" in i):
                            i = str(i).split(":")
                            i = f"{colorama.ansi.Fore.MAGENTA}Network Name : {colorama.ansi.Fore.GREEN} {network_name} {colorama.ansi.Fore.WHITE}--- {colorama.ansi.Fore.MAGENTA}Password : {colorama.ansi.Fore.GREEN} {i[1].strip()}"
                            return i
                        else:
                            return NoneSelectedNetwork.__doc__
                else:
                    return WorksOnlyOnWindows.__doc__
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return AdminPermissionRequestDenied.__doc__

    @classmethod
    def TestConnection(cls , show : bool = False , timeout : int = 5):
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.
            timeout (int): _Sets The Timeout For Each Request_. Defaults to 5.

        Returns:
            _str_: _Tests Internet Connection_
        """
        if (type(show) is bool):
            if (show is True):
                if (type(timeout) is int):
                    try:
                        req = requests.get("https://www.google.com" , timeout = timeout)
                        return f"{colorama.ansi.Fore.GREEN}You're Connected To Internet"
                    except (requests.ConnectionError , requests.Timeout) as E:
                        return f"{colorama.ansi.Fore.RED}You're not Connected To Internet \n{E}"
                else:
                    return NoneTypeArgumentInt
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod
    def StatusCodeChecker(cls , show : bool = False , link : str = ''):
        """_summary_

        Args:
            _show_ (bool): _Shows The Output_. Defaults to False.
            _link_ (str): Link to The Target Website or IP Address.

        Returns:
            _str_: Status Codes Available in Link or IP Address
        """
        if (type(show) is bool):
            if (show is True):
                if (type(link) is str):
                    for code in range(200 , 599 + 1):
                        if (requests.get(link).status_code == code):
                            print(f"{colorama.ansi.Fore.MAGENTA}Status : {colorama.ansi.Fore.BLUE}{code} {colorama.ansi.Fore.GREEN}is Available")
                        else:
                            print(f"{colorama.ansi.Fore.MAGENTA}Status : {colorama.ansi.Fore.BLUE}{code} {colorama.ansi.Fore.RED}is not Available")
                else:
                    return NoneTypeArgumentString
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__