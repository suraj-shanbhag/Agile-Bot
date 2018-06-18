import pandas as pd

class CommitFrame:
    def __init__(self, file_location='../Data-Sprint53/output.csv'):
        file=open(file_location)
        commits=file.readlines()
        commit_table=[]
        for commit in commits:
            parsed_commit=commit.split(',',3)
            commit_table.append(parsed_commit)
        self.commit_frame=pd.DataFrame(commit_table,columns={'Commit Id','Author','Date','Info'})
if __name__ == '__main__':
    frame=CommitFrame()
    commit_info=list(frame.commit_frame.iloc[0:, 3])
    print (commit_info)




