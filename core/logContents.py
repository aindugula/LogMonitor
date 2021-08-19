
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
            
 
# Driver Code:
if __name__ == '__main__':
    fname = '../Data/testsmall.log'
    N = 3
    list = logContents(fname, N, "completed")
    print(list)
    
