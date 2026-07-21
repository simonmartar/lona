from settings import (

    WARNING_LIMIT,

    CRITICAL_LIMIT

)


class WarningLevel:

    def status(

        self,

        percent

    ):

        if percent >= CRITICAL_LIMIT:

            return "Critical"

        if percent >= WARNING_LIMIT:

            return "Warning"

        return "Healthy"
