import re
with open("../Data-Sprint53/log.txt","r") as file:
    data=file.read()
    commits=data.split('commit')[1:]
    with open("../Data-Sprint53/output.csv","a") as out:
        for commit in commits:
            parsed_commit=commit.split('\n')
            while '' in parsed_commit:
                parsed_commit.remove('')
            if len(parsed_commit) == 4 :
                (commit_id, author, date, info)=parsed_commit[:]
                print (commit_id+" "+author+" "+date+" "+info)
                out.write(str(commit_id).strip(',')+","+ str(author).strip(',')+","+str(date).strip(',')+","+str(info).strip(',')+"\n")

