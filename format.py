from logger import log


# clean the comment received and return to the sanitize function.
def clean(comment):

    # basic splitting on exclamation mark
    comment = comment.split("!")[1]

    # formatting the comment string for proper input.
    comment.strip()
    comment.lower()

    # checking for discrepancies in the entered string.
    if comment.count(" ") > 1:
        log("More than two hands given!")
        return None, comment
    elif comment.count(" ") < 1:
        log("No hand card given!")
        return None, comment

    # returning the formatted string.
    return comment


clean("Yoo")