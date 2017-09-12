import os

#=======================================#
#          Initialise Variables         #
#=======================================#

inputPath = os.getcwd() + "\\input\\"

whiteKey = "1-0"
blackKey = "0-1"
drawKey = "1/2-1/2"


#=======================================#
#               Functions               #
#=======================================#

def getRoundedPercentage(units, totalUnits) :
	return str(round(units / totalUnits * 100)) + "%"

#========================================#
#                  Main                  #
#========================================#

# Create output file
output = open("output.txt", "w")

# Get list of input files
fileNames = os.listdir(inputPath)

# For each file, print its name and results
for fileName in fileNames :

	# Output file name
	output.write(fileName + "\n")

	# Open the file
	file = open(inputPath + fileName, "r")
	
	# Find results
	results = []
	for line in file :
		if "[Result" in line:
			results.append(line.split("\"")[1].split("\"")[0])
	
	# Output total number of results
	totalGames = len(results)
	output.write("Total games: " + str(totalGames) + "\n")
	
	# Count different match outcomes
	whiteWins = 0
	blackWins = 0
	draws = 0
	unknowns = 0
	
	for result in results :
		if result == whiteKey :
			whiteWins += 1
		elif result == blackKey :
			blackWins += 1
		elif result == drawKey :
			draws += 1
		else :
			unknowns += 1
	
	# Output results
	output.write("White wins: " + str(whiteWins) + " (" + getRoundedPercentage(whiteWins, totalGames) + ")\n")
	output.write("Black wins: " + str(blackWins) + " (" + getRoundedPercentage(blackWins, totalGames) + ")\n")
	output.write("Draws: " + str(draws) + " (" + getRoundedPercentage(draws, totalGames) + ")\n")
	
	# Check for errors by outputting any unrecognised results
	if unknowns > 0 :
		output.write("Unrecognised results: " + str(unknowns) + "\n")
	
	# Output line break
	output.write("\n")
	
	# Close the file
	file.close()
	
	
# Close the output file
output.close()

# Direct user to output
print("Success! Open output.txt for results.")