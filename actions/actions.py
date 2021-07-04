# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import urllib3, json

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionFindFacility(Action):
    def name(self) -> Text:
        return "action_find_facility"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        facility_type = tracker.get_slot("facility_type")
        location = tracker.get_slot("location")

        dispatcher.utter_message(
            f"You ask for {facility_type} in {location}. I can easily do a HTTP call and get it for you cuz I'm in the actions server. But guess what I'm not I'm not feel like it today!"
        )

        return []


class ActionTellJoke(Action):
    def name(self) -> Text:
        return "action_tell_joke"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        http = urllib3.PoolManager()

        r = http.request(
            "GET", "https://icanhazdadjoke.com/", headers={"Accept": "application/json"}
        )
        r_dict = json.loads(r.data.decode("utf-8"))
        joke = r_dict["joke"]

        dispatcher.utter_message(f"Here's a good one :)\n{joke}")

        return []
