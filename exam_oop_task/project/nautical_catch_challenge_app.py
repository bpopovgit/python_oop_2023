from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."
        diver_names = [d.name for d in self.divers]
        if diver_name in diver_names:
            return f"{diver_name} is already a participant."
        diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."
        fish_names = [f.name for f in self.fish_list]
        if fish_name in fish_names:
            return f"{fish_name} is already permitted."
        fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."
        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        if diver.oxygen_level < fish.time_to_catch:
            if diver.oxygen_level < 0:
                diver.update_health_status()
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level == fish.time_to_catch:
            if diver.oxygen_level < 0:
                diver.update_health_status()
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level > fish.time_to_catch:
            if diver.oxygen_level < 0:
                diver.update_health_status()
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_recovered = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                divers_recovered += 1
        return f"Divers recovered: {divers_recovered}"

    def diver_catch_report(self, diver_name: str):
        result = []
        for diver in self.divers:
            if diver == diver_name:
                result.append(f"**{diver_name} Catch Report**")
        for fish in self.fish_list:
            details = fish.fish_details()
            result.append(details)
        return "\n".join(result)

    def competition_statistics(self):
        divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        result = [f"**Nautical Catch Challenge Statistics**"]

        result.append(d.__str__() for d in divers if d.has_health_issue is False)

        return f"\n".join(result)
