# Random-T20-py
Randomized T20 cricket tournament

This is acommand line application to maintain player and team performances during a T20 cricket tournament. A tournament consists of a one major round. During the round, all teams that are placed in the
same group compete each other. Further, the tournament consists of two groups (Group A, Group B). Each group has 4 teams. Overall there will be 8 teams.

These are the functionality of the application;
1) Player information is stored using file I/O in text file using comma separated values (csv). The league will only start after all player profiles have been created.

2) Before the tournament starts the user can delete/edit player and team profiles and the application gives separate options for each and every functionality. These functionalities are disabled after starting the tournament.

3) Starting from the toss, everything about the game needs is random (no hardcoded snippets). The team who wins the toss takes the
decision to ball first or bat first. Then the program initiates the first innings. Scores of each batsman, balls took for scoring, wickets by bowlers, overs, fall of wickets, the method of the dismissal, final score of the innings is decided by the algorithm. Next the second innings start and the process is repeated as for the first innings but now for the second team. The data being saved to the csv file can be seen below.

![image](https://user-images.githubusercontent.com/100549603/219356611-2c19e28b-a25f-46a2-989d-5b09919bedc3.png)


4) Additionally, the application can display match summmary for a given match and displays the tournament standings. 

A flowchart of this application can be seen below.

![image](https://user-images.githubusercontent.com/100549603/219356165-67c64580-2edc-408f-8a85-0679a50d55a4.png)

This game was designed to run on the command-line, I hope to design a GUI later on and convert this python code to Java so that I can implement OOP concepts. A look at the command line interface is given below.

![image](https://user-images.githubusercontent.com/100549603/219356914-2c698ac4-a1ed-4ddb-b2a7-6cec88c26bdc.png)


