
from datetime import datetime
def can_schedule_all(unloading_times):
    """
    :param unloading_times: (list) The list of datetimes
    :returns: (bool) Returns True if the datetimes don't overlap else returns False
    
    """
    unloading_times.sort(key = lambda x : x[0])
    end_time = datetime.min
    for start, end in unloading_times:
        if start < end_time:
            return False
        end_time = end
    return True
