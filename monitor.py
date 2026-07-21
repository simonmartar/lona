from formatter import Formatter

from warning import WarningLevel


class Monitor:

    def analyze(

        self,

        disks

    ):

        result = []

        formatter = Formatter()

        checker = WarningLevel()

        for disk in disks:

            percent = formatter.percent(

                disk

            )

            result.append(

                {

                    "disk": disk,

                    "percent": percent,

                    "status":

                        checker.status(

                            percent

                        )

                }

            )

        return result
