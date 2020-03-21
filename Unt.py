import os
import requests
from rasa_core_sdk.forms import FormAction
from rasa_core_sdk.events import SlotSet


class FormSuggestion(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "form_suggestion"

    @staticmethod
    def required_slots(tracker):
        # type: () -> List[Text]
        """A list of required slots that the form has to fill"""

        return ["suggestion"]

    def validate(self, dispatcher, tracker, domain):
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        requested_slot = tracker.get_slot("requested_slot")
        if not requested_slot or requested_slot != "suggestion":
            return [SlotSet("requested_slot", "suggestion")]
        return [SlotSet("suggestion", tracker.latest_message['text'])]

    def submit(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Define what the form has to do
            after all required slots are filled"""

        suggestion = tracker.get_slot("suggestion")
        # do something with suggestion
        return [SlotSet("suggestion", None), SlotSet("requested_slot", None)]



