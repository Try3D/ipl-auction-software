from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from .models import Player
from django.http import JsonResponse


pool_name_map = {
    1: "MARQUEE SET",
    2: "BATSMEN 1",
    3: "ALL ROUNDERS 1",
    4: "WICKET KEEPERS 1",
    5: "FAST BOWLERS 1",
    6: "SPIN BOWLERS 1",
    7: "BATSMEN 2",
    8: "WICKET KEEPERS 2",
    9: "ALL ROUNDERS 2",
    10: "FAST BOWLERS 2",
    11: "SPIN BOWLERS 2",
    12: "ALL ROUNDERS 3",
    13: "BATSMEN 3",
    14: "ALL ROUNDERS 4",
}

pool_code_map = {
    1: "MS",
    2: "BA1",
    3: "AR1",
    4: "WK1",
    5: "FB1",
    6: "SB1",
    7: "BA2",
    8: "WK2",
    9: "AR2",
    10: "FB2",
    11: "SB2",
    12: "AR3",
    13: "BA3",
    14: "AR4",
}

rtm_use = {
    "MI": 0,
    "CSK": 0,
    "RCB": 0,
    "KKR": 0,
    "SRH": 0,
    "DC": 0,
    "RR": 0,
    "PBKS": 0,
    "GT": 0,
    "": 0,
}

code_to_name = {
    "MI": "Mumbai Indians",
    "CSE": "Chennai Super Kings",
    "RCB": "Royal Challengers Bangalore",
    "KKR": "Kolkata Knight Riders",
    "SRH": "Sunrisers Hyderabad",
    "DC": "Delhi Capitals",
    "RR": "Rajasthan Royals",
    "PBKS": "Punjab Kings",
    "GT": "Gujarat Titans",
    "": "No team",
}

lst = []
for i in list(pool_code_map.keys()):
    j = np.array(Player.objects.filter(setNo=i))
    if j.any():
        np.random.shuffle(j)
    lst.extend(j)


def index(request):
    return redirect("getPlayer/1/")


def player(request, pk):
    try:
        newpool = (
            True
            if lst[int(pk) - 1].setNo != lst[int(pk) - 2].setNo or int(pk) == 1
            else False
        )
        output = {
            "player": lst[int(pk) - 1],
            "id": pk,
            "pool": {
                "poolName": pool_name_map[lst[int(pk) - 1].setNo],
                "poolCode": pool_code_map[lst[int(pk) - 1].setNo],
                "isNewPool": newpool,
            },
            "rtm": rtm_use[lst[int(pk) - 1].prev_team] < 3
            and lst[int(pk) - 1].prev_team != "",
            "team": {
                "name": code_to_name[lst[int(pk) - 1].prev_team.upper()],
                "code": lst[int(pk) - 1].prev_team,
            },
        }
        return render(request, "index.html", output)
    except IndexError:
        if int(pk) == len(lst) + 1:
            return render(request, "index.html", {"status": "done"})
        return JsonResponse({"error": "Player not found"})


@csrf_exempt
def addplayer(request):
    try:
        set_no = request.POST.get("setNo")
        name = request.POST.get("name")
        country = request.POST.get("country")
        prev_team = request.POST.get("prevTeam")
        base_price = request.POST.get("basePrice")
        age = request.POST.get("age")
        num_matches = request.POST.get("numMatches")
        num_runs = request.POST.get("numRuns")
        batting_avg = request.POST.get("battingAvg")
        strike_rate = request.POST.get("strikeRate")
        num_wickets = request.POST.get("numWickets")
        bowling_avg = request.POST.get("bowlingAvg")
        bowling_economy = request.POST.get("bowlingEconomy")

        # Save the uploaded image to the 'img' field of the Player model
        img = request.FILES.get("img")
        Player.objects.create(
            setNo=set_no,
            name=name,
            img=img,
            country=country,
            prev_team=prev_team,
            basePrice=base_price,
            age=age,
            numMatches=num_matches,
            numRuns=num_runs,
            battingAvg=batting_avg,
            strikeRate=strike_rate,
            numWickets=num_wickets,
            bowlingAvg=bowling_avg,
            bowlingEconomy=bowling_economy,
        )

        return JsonResponse({"message": "Player added successfully"}, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def player_rtm(request):
    try:
        team_code = request.GET.get("team_code", "").upper()

        if team_code not in rtm_use:
            return JsonResponse({"error": "Invalid parameters"}, status=400)

        rtm_use[team_code] += 1

        return JsonResponse({"message": "RTM count updated successfully"}, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
