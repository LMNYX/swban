import requests
import inquirer, json
from config import *

print("Steamworks Ban Utility")

while True:
    _w = inquirer.prompt([
        inquirer.List("what",
        message="What do you want to do?",
        choices=["Only generate report", "Request a ban", "Generate report and request a ban", "Request an unban", "Exit"])
    ])

    if _w['what'] == "Only generate report":
        _x = inquirer.prompt([inquirer.Text("steamid", message="SteamID64")])
        _x = requests.post("https://partner.steam-api.com/ICheatReportingService/ReportPlayerCheating/v1/", {
            "key": STEAM_WEB_API_KEY,
            "steamid": _x['steamid'],
            "appid": APP_ID
        }).json()
        print("Generated ReportID is: "+_x['response']['reportid'])
    elif _w['what'] == "Request a ban":
        _x = inquirer.prompt([inquirer.Text("steamid", message="SteamID64"), inquirer.Text("reportid", message="Report ID"), inquirer.Text("duration", message="Duration (0 is permament)", default="0")])
        _x = requests.post("https://partner.steam-api.com/ICheatReportingService/RequestPlayerGameBan/v1/", {
            "key": STEAM_WEB_API_KEY,
            "steamid": _x['steamid'],
            "appid": APP_ID,
            "reportid": _x['reportid'],
            "cheatdescription": "Banned",
            "duration": _x['duration'],
            "delayban": 0,
            "flags": 0
        })
        print("Ban requested.")
    elif _w['what'] == "Generate report and request a ban":
        _x = inquirer.prompt([inquirer.Text("steamid", message="SteamID64"), inquirer.Text("duration", message="Duration (0 is permament)", default="0")])
        _c = requests.post("https://partner.steam-api.com/ICheatReportingService/ReportPlayerCheating/v1/", {
            "key": STEAM_WEB_API_KEY,
            "steamid": _x['steamid'],
            "appid": APP_ID
        }).json()
        _x = requests.post("https://partner.steam-api.com/ICheatReportingService/RequestPlayerGameBan/v1/", {
            "key": STEAM_WEB_API_KEY,
            "steamid": _x['steamid'],
            "appid": APP_ID,
            "reportid": _c['response']['reportid'],
            "cheatdescription": "Banned",
            "duration": _x['duration'],
            "delayban": 0,
            "flags": 0
        })
        print("Report generated and ban requested.")
    elif _w['what'] == "Request an unban":
        _x = inquirer.prompt([inquirer.Text("steamid", message="SteamID64")])
        _x = requests.post("https://partner.steam-api.com/ICheatReportingService/RemovePlayerGameBan/v1/", {
            "key": STEAM_WEB_API_KEY,
            "steamid": _x['steamid'],
            "appid": APP_ID
        })
        print("Requested an unban.")
    elif _w['what'] == "Exit":
        exit()
exit()