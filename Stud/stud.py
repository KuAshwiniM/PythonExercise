import exception
import log

def calculate_result(marks):
    try:
        validated_marks =[]
        for mark in marks:
            exception.invalidmarks(mark)
            exception.numcheck(mark)
            validated_marks.append(mark)
        print(validated_marks)

        total = sum(validated_marks)
        percentage = (total / len(validated_marks)) * 100 if validated_marks else 0

        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"
    except Exception as e:
        log.log_msg("error", "Exception occurred while calculating result: {}".format(e))
        return None