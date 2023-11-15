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
import time
import random

start = time.time()

def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                                             default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options

def run():
    
    # Load bus routes id
    bus_routes_id = traci.route.getIDList()
    bus_routes_id = list(bus_routes_id)
    print("bus_routes_id=", bus_routes_id)
    
    # Get edges with bus stops
    source_bus_stop_id = "S2"
    stop_id = traci.busstop.getIDList()
    stop_id = list(stop_id)
    stop_id.remove('S2')
    print("stop_id=", stop_id)
    bus_stop_num = traci.busstop.getIDCount() #32 bus stops
    print("bus_stop_num including source %s = %s " % (source_bus_stop_id, bus_stop_num))

    #print("busnum = %s , bus stop ID= %s" % (traci.busstop.getIDCount(), str(traci.busstop.getIDList())))
  
    # create passengers with fixed start and random destination edges
    passenger_ids = []
    add_person_edge_id = "UP"
    num_people = 20
    
    for i in range(num_people):
        person_id = f"person_{i}"
        passenger_ids.append(person_id)
        traci.person.add(personID=person_id, edgeID=add_person_edge_id, pos=17.08)
        destination_stop = random.choice(stop_id)
        destination_edge = traci.lane.getEdgeID(traci.busstop.getLaneID(destination_stop))
        print("person %s will take a bus to bus stop %s on edge %s" % (person_id, destination_stop, destination_edge))
        traci.person.appendDrivingStage(personID=person_id, toEdge=destination_edge, lines="bus", stopID=destination_stop)
        
    print("passenger id list=", passenger_ids)
    

 
    #why people are taking the wrong bus? and then teleporting after reaching the end of the route? 
   
    
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
    
    
    for person in passenger_ids:
        travel_time = traci.person.getWaitingTime 
        print("simulation ends at time=%s" % traci.simulation.getTime())

    traci.close()



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
                                            "--tripinfo-output", "tripinfo.xml",
                                            "--stop-output", "stopoutput.xml",
                                            "--time-to-teleport", "-1",
                                            "--statistic-output", "statisticoutput.xml"])
    
    run()
    
    
    
