class Formatter:

    def percent(
        self,
        disk
    ):

        return round(

            disk.used

            /

            disk.total

            * 100

        )
