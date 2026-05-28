def https_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "unknown"
        case _:
            return "default"
print(https_status(200))

dic1={
       1:'krishn',
       2:'Jatav'
       }
dic2={
        2:'Jattu',
        3:'bhai'
        }
merge=dic1 | dic2
print(merge)
