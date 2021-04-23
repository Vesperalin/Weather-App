from datetime import datetime


def get_date(timestamp):
    """
        takes timestamp in unix time format
        returns tuple of integers: (year, month, day)
    """
    try:
        time = int(timestamp)
        date_sequence = datetime.utcfromtimestamp(time).__str__()
        date = date_sequence.split(" ")[0].split("-")
        ret_date = (int(date[0]), int(date[1]), int(date[2]))
        return ret_date
    except ValueError:
        return None


if __name__ == '__main__':
    # TODO - delete
    print(get_date(1619172000))
