import os
import sys
import optparse



# import python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
    
    
    
from sumolib import checkBinary
import traci



def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                                             default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options


# contains traci control loop
def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        print(step)
        
        #bus_stop_list = []
        #bus_stop_list = 
        
        print("busnum = %s , bus stop ID= %s" % (traci.busstop.getIDCount(), str(traci.busstop.getIDList())))
        #32 bus stops
        
        #add person
        
        #traci.person.add(self, personID, edgeID, pos, depart=-3, typeID='DEFAULT_PEDTYPE')
        #traci.person.add(personID="", edgeID="", pos="0", typeID="")
        #traci.person.add("newPerson", "UP", "17.08", "passenger")
        
        #traci.person.appendWalkingStage(personID=f"bp_{passengerBatchNo}_{i}",edges=random.choice(combinedRouteList), stopID="bs_1", arrivalPos=str(busstopID))
        #traci.person.appendWalkingStage("newPerson", "UP", "17.08")
        
        
        #traci.person.appendDrivingStage(self, personID, toEdge, lines, stopID='')
        #traci.person.appendDrivingStage(personID="newPerson", toEdge="B2", lines="bus")
        
        #print("getIDList", traci.person.getIDList())
        #print("numPersons=%s, minExpected=%s" % (
        #        traci.person.getIDCount(),
        #        traci.simulation.getMinExpectedNumber()))
        
        # traci.person.appendDrivingStage()
        # traci.person.getVehicle()
        # traci.person.getWaitingTime()
        
       # #bus stop
       # traci.busstop.getName
       # traci.busstop.getIDList()
        
        
        step += 1

    traci.close()
    sys.stdout.flush()


# main entry point
if __name__ == "__main__":
    options = get_options()
    
    #check binary
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')
    
    #traci starts sumo as a subprocess and then this script connects and runs
    traci.start([sumoBinary, "-c", "test.sumocfg",
                                            "--tripinfo-output", "tripinfo.xml"])
    
    run()
