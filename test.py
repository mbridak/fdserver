from json import JSONDecodeError, loads, dumps

with open(
    "wfdserver/data/server_preferences.json", "rt", encoding="utf-8"
) as _file_descriptor:
    preference = loads(_file_descriptor.read())
    MULTICAST_PORT = preference.get("multicast_port")
    MULTICAST_GROUP = preference.get("mullticast_group")
    INTERFACE_IP = preference.get("interface_ip")
    OURCALL = preference.get("ourcall")
    OURCLASS = preference.get("ourclass")
    OURSECTION = preference.get("oursection")
    BATTERYPOWER = preference.get("batterypower")
    NAME = preference.get("name")
    ADDRESS = preference.get("address")
    CITY = preference.get("city")
    STATE = preference.get("state")
    POSTALCODE = preference.get("postalcode")
    COUNTRY = preference.get("country")
    EMAIL = preference.get("email")
    NODE_RED_SERVER_IP = preference.get("node_red_server_ip")
    NODE_RED_SERVER_PORT = preference.get("node_red_server_port")
    BONUS = preference.get("bonus")

for bonus in BONUS:
    if BONUS.get(bonus):
        print(f"{bonus}")
