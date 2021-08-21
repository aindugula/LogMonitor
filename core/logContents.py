import os

#get the contents of a file based on certain criteria
#similar to tail in linux
def logContents(fname, N=None, searchText=None):
    queue = []
    #using list as a queue to store the last N lines in the file    
    with open(fname) as file:
        for line in (file.readlines()):
            if searchText is not None:
                if searchText not in line:
                    continue
            queue.append(line)
            if N is not None:
                if len(queue) > N:
                    queue.pop(0)
    #reverse the list to get the results in reverse time order
    queue.reverse()
    return queue
            
def logContents_Tail(fname, N=None, searchText=None):

    list = []
    if N is None:
        with open(fname) as file:
            list = file.readlines()
            list.reverse()
        return list
    
    numlines = 0
    with open(fname) as file:
        file.seek(0, os.SEEK_END)
        pos = file.tell();
        
        while pos > 0:
            pos = pos - 1
            file.seek(pos, os.SEEK_SET)
            try:
                c = file.read(1)
            except:
                c = ''
            
            if c == '\n':
                if numlines == N:
                    break
                numlines += 1
        lines = file.readlines()
        
    lines.reverse()
    
    if searchText == None:
        return lines
    list = []
    for item in lines:
        if searchText in item:
            list.append(item)
    return list

# Driver Code:
if __name__ == '__main__':
    fname = '../Data/testsmall.log'
    N = 900
    list = logContents_Tail(fname, N, 'completed')
    print(list)
    
