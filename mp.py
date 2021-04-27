"""
This is a helper file to list the main steps that need to be finished for the operator implementation.
It's optional to use the methods/structure defined in this file. You can have your own implementation.

"""
import csv
import sys
import json

class OnePassOperator:
    def __init__(self, config):
        self.memory = 0
        self._loadConfig(config)

def _loadConfig(configFile):
    # load config file as json, extract the memory and block size, return the memory size and block size
    f = open(configFile)
    data = json.load(f)
    memorySize, blockSize = data["memory_size"], data["block_size"]

    return memorySize, blockSize


def _loadColNames(inputFile):
    # extract column names from the input file, you can generate a dict of {columnName:index} pair, return the dict
    colNames = {}

    with open(inputFile) as csvFile:
        firstRow = csvFile.readline().strip('\n')
        firstRow = firstRow.split(",")

        for idx, colName in enumerate(firstRow):
            colNames[colName] = idx

    return colNames




def onePassOperator(config, table1, table2, output):
    outputFile = open(output, 'w')
    csvWriter = csv.writer(outputFile)
    # TODO: step 1 - load config.txt as json, extract memory size (Number of blocks in the main memory) and block size(Number of Tuples in a     # block), compute maximal number of rows(tuples) that can be loaded into memory
    memorySize, blockSize = _loadConfig(config)
    maxNumOfTuples = -1

    # TODO: step 2 - check the size of the input table 1 and input table 2, decide if the input is valid
    size1, size2 = -1, -1

    
    colNames1 = _loadColNames(table1)
    colNames2 = _loadColNames(table2)

    # TODO: step 3 - load smaller data table into memory 
    memory = []
    with open(table1) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")
        for row in csvReader:  
            pass #TODO
    
    memory.sort() #sorts memory
    # TODO: step 4 - write column names to the output file
    # TODO: step 5 - write tuples of small file to the output.


    # TODO: step 5 - load larger data table row by row into memory,if that row is not in the smaller table, write it to the output
    with open(table2) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")
        for row in csvReader:
            pass #TODO
    
    outputFile.close()

if __name__ == "__main__":
    config, table1, table2, output = sys.argv[1:]
    onePassOperator(config, table1, table2, output)