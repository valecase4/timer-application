import math

def converter(total_seconds: int) -> str:
        """
        This function takes the total amount of seconds and converts it in the format time hh:mm:ss
        ready to be displayed to the user

        :param total_seconds: total amount of seconds for the timer
        :return: time string 
        """

        hours_value = math.floor(total_seconds / 3600)

        hours = "0{}".format(hours_value) if len(str(hours_value)) == 1 else "{}".format(hours_value)

        remainder = total_seconds % 3600

        if remainder < 60:
            minutes = "00"
            seconds = "0{}".format(remainder) if len(str(remainder)) == 1 else str(remainder)
        else:
            minutes_value = math.floor(remainder / 60)
            minutes = "0{}".format(minutes_value) if len(str(minutes_value)) == 1 else str(minutes_value)
            total_seconds = remainder % 60
            seconds = "0{}".format(total_seconds) if len(str(total_seconds)) == 1 else str(total_seconds)

        return "{hours}:{minutes}:{seconds}".format(hours=hours, minutes=minutes, seconds=seconds)