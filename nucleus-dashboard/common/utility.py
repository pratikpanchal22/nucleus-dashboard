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
            diffStr += "less than a second"
        elif(ts < 60):
            diffStr += "{:.0f} seconds".format(ts)
        else:
            tm, ts = divmod(ts, 60)
            if(round(ts) > 0):
                diffStr += " & {:.0f} seconds".format(ts)

            if(tm == 1):
                diffStr = "a minute" + diffStr 
            elif(tm < 60):
                diffStr = "{:.0f} minutes".format(tm) + diffStr
            else:
                th, tm = divmod(tm, 60)
                if(round(tm) > 0):
                    diffStr = " & {:.0f} minutes".format(tm)

                if(th == 1):
                    diffStr = "an hour" + diffStr 
                elif(th < 24):
                    diffStr = "{:.0f} hours".format(th) + diffStr
                else:
                    td, th = divmod(th, 24)
                    if(round(th) > 0):
                        diffStr = " & {:.0f} hours".format(th)

                    if(td == 1):
                        diffStr = "a day" + diffStr
                    elif(td < 4):
                        diffStr = "{:.0f} days".format(td) + diffStr
                    else:
                        diffStr = "{:.0f} days".format(td)

        if(diffStr != ""):
            diffStr += " ago"       

        return diffStr