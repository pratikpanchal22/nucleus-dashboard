import inspect
from json import JSONEncoder
import datetime

def logger(logLevel, *argsv):
    s=""
    if(str(argsv[0]).startswith('\n')):
        s+="\n"

    s += "{}{:<16.16}{}".format("[", inspect.stack()[1][3], "]")
    for arg in argsv:
        if(str(arg).startswith('\n')):
            s += " " + str(arg).lstrip()
        else:
            s += " " + str(arg)
    print (s)

def comma_separated_params_to_list(param):
    result = []
    for val in param.split(','):
        if val:
            result.append(val)
    return result    

class DateTimeEncoder(JSONEncoder):
    #Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

def passed_time_string_for_past_dto(dto):
    if not (isinstance(dto, datetime.datetime)):
        return "Invalid datetime object"

    now = datetime.datetime.now()
    if(now < dto):
        return "Provide datetime is in future"
    else:
        difference = now - dto
        print ("difference: ",difference)
        print ("Type of difference ", type(difference))
        ts = difference.total_seconds()
        print ("total seconds: ", difference.total_seconds())

        diffStr = ""
        if(ts < 1):
            diffStr = "less than a second"
        elif(ts < 60):
            diffStr = str(ts) + " seconds"
        else:
            tm, ts = divmod(ts, 60)
            diffStr = str(ts) + " seconds"

            if(tm == 1):
                diffStr = "A minute and " + diffStr 
            elif(tm < 60):
                diffStr = str(tm) + " minutes, " + diffStr
            else:
                th, tm = divmod(tm, 60)
                diffStr = str(tm) + " minutes, " + diffStr
        
        #if(difference.year > 0):
        #    diffStr += str(difference.year) + " year"
        #    if(difference.year > 1):
        #        diffStr += 's '

        #if(difference.month > 0):
        #    diffStr += str(difference.month) + " month"
        #    if(difference.month > 1):
        #        diffStr += 's '

        #if(difference.day > 0):
        #    diffStr += str(difference.day) + " day"
        #    if(difference.day > 1):
        #        diffStr += 's '

        #if(difference.hour > 0):
        #    diffStr += str(difference.hour) + " hour"
        #    if(difference.hour > 1):
        #        diffStr += 's '       

        #if(difference.minute > 0):
        #    diffStr += str(difference.minute) + " minute"
        #    if(difference.minute > 1):
        #        diffStr += 's '    

        #if(difference.second > 0):
        #    diffStr += str(difference.second) + " second"
        #    if(difference.second > 1):
        #        diffStr += 's '

        if(diffStr != ""):
            diffStr += " ago"       

        return diffStr