def print_report(

    report

):

    print()

    print(

        "Disk Scan"

    )

    print()

    warnings = 0

    for item in report:

        print(

            f"Drive {item['disk'].name}"

        )

        print(

            f"Used: {item['percent']}%"

        )

        print(

            f"Status: {item['status']}"

        )

        print()

        if item["status"] != "Healthy":

            warnings += 1

    print(

        "Summary"

    )

    print()

    print(

        f"Total drives: {len(report)}"

    )

    print(

        f"Warnings: {warnings}"

    )
