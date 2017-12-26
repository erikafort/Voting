'''
    A program that allows a set of pre-registered users to vote on their cusisine preference
    4/3/2017
    Author(s): Sharon Stansfield, Paul, Dickson, Toby Dragon, Erika Fortune
'''

def findVoter(voters,name):
    '''
    Arg: name and registerdVoters list
    Return: Boolean of True or False
    Purpose: to determine if the name is in the predetermined list aka registeredVoters
    '''
    for x in range(len(voters)):
        if(voters[x]==name):
            return True
    return False
def addToVoted(name, alreadyVotedList):
    '''
    Arg: list of names who already vote (alreadyVotedList) and the name of the current voter (name)
    Return: the alreadyVotedList with the name of the current voter (name) added to it
    Purpose: To add the current voters name to the alreadyVotedList
    '''
    newVotedList=alreadyVotedList.append(name)
    return newVotedList
def processVote(voteCount,votedIndex):
    '''
    Arg: the list which stores the about of votes for each cuisine (voteCount) and the index number of the food the user wants to vote for
    Return: the new cusine voteCount list with the vote added to the proper index of the food the person voted for
    Purpose: To add the vote from the voter to the cusine index in which it corresponds to
    '''
    
    voteCount[votedIndex]=(voteCount[votedIndex]+1)
    return voteCount

def findWinner(voteCount):
    '''
    Arg: the list of vote counts per cuisine (voteCount)
    Return: the position index of the winner in the cuisines list
    Purpose: to determine the winner based on vote counts
    '''
    firstplace=0
    for x in range(len(voteCount)):
        if (voteCount[x]>firstplace):
            firstplace=voteCount[x]
            new=x
    return new
    
def main():
    #all registered voters are listed here, only they may vote
    registeredVoters = ["Allen", "Carlson", "Black", "Jones", "Smith", "Johnson", "Stevens",
                        "Hernandez", "Park", "Chen", "Matino","Fellini", "Gates", "Williams"]
    #all cuisines are lists here, in the order they will be presented to voters
    cuisines = ["American", "Cajun","Chinese", "French", "Greek",
                      "Indian", "Italian", "Japanese", "Mexican", "Morroccan", "Thai"]
    #there are 0 votes for each cuisine to start
    voteCount = [0,0,0,0,0,0,0,0,0,0,0]
    #no one has already voted
    alreadyVotedList = [] 

    anotherVoter = "y"
    while anotherVoter == "y":
        name = input("Please enter your last name: ")

        registered = findVoter(registeredVoters,name)
        if registered:  

            alreadyVoted = findVoter(alreadyVotedList,name)
            if not alreadyVoted:
                addToVoted(name, alreadyVotedList)
                
                print("Please vote for your favorite cuisine:")
                for index in range(len(cuisines)):
                    #print numbers starting at 1, not 0
                    print(index+1, " - ", cuisines[index])  
                
                vote = int(input("Enter the number corresponding to your choice: "))
                while(vote <= 0 or vote >=12):
                  vote = int(input("Invalid Input.  Enter the number corresponding to your choice: "))

                votedIndex = vote -1 #get the index by subtracting the 1 added during printout
                processVote(voteCount, votedIndex)
            else:
                print("Denied. You can't vote more than once.")
        else:
            print("Denied. You must be registered to vote.")
            
        anotherVoter = input("Is there another voter (y): ")

    #find the winner and print the winning cuisine
    winner = findWinner(voteCount)
    print ("The winner is", cuisines[winner])
    

#run the program
main()
