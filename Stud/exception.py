from log import log_msg

def invalidmarks(marks):
    try:
        if marks <0 or marks >100:
            log_msg("info", "Invalid marks: {}".format(marks))
    except Exception as e:
        log_msg("error", "Exception occurred: {}".format(e))


def numcheck(marks):
    try:
        if not isinstance(marks, (int, float)):
            log_msg("info", "Invalid type for marks: {}".format(type(marks)))
    except Exception as e:
        log_msg("error", "Exception occurred: {}".format(e))