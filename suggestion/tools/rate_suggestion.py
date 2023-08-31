from typing import Dict
from datetime import datetime, timedelta
import asyncio

from ..config import GlobalConfig


class ControlRateSuggestion:
    """Rate suggestion control system.
    Be careful each time an instance is created a new system is created with an infinity loop.
    """
    
    def __init__(self) -> None:
        self.rate_suggestion: Dict[int, datetime] = {}
        self.start_control_rate()


    def start_control_rate(self) -> None:
        """
        Start rate control system suggestion.
        """
        asyncio.create_task(self.infinity_loop_rate_control())


    def add_user_to_rate_control(self, user_id: int) -> None:
        """
        Add a user to the rate control dictionary with the current datetime.
        Args:
            user_id (int): User's ID
        """
        self.rate_suggestion[user_id] = datetime.now()


    def user_at_rate_limit(self, user_id: int) -> bool:
        """
        Check if the user can send a suggestion.

        Returns:
            - True if the user cannot send a suggestion.
            - False if the user can send a suggestion.
        """
        return True if user_id in self.rate_suggestion else False


    @staticmethod
    def check_rating(date: datetime) -> bool:
        """
        Check if the date the user posted the message waited until time X had elapsed before posting a new message.

        Args:
            date (datetime): Date when the user posted the message

        Returns:
            - True if the message has expired,
            - False if the message must still wait
        """

        elapsed_time = datetime.now() - date
        return elapsed_time > timedelta(seconds=GlobalConfig.RATE_SUGGESTION_PER_SECOND_PER_USER.value)


    async def infinity_loop_rate_control(self) -> None:
        """
        Continuously check and remove expired rate control entries.
        """

        while True:
            for key, items in self.rate_suggestion.items():
                
                if self.check_rating(items):
                    self.rate_suggestion.pop(key)
                await asyncio.sleep(1)

            await asyncio.sleep(60)
