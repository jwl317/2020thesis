# Introduction

Jae Won Lee

2015314213

Computer Science and Engineering, College of Computing, SKKU

Supervisor: Professor Jaehoon Paul Jeong

Title: Factors guaranteeing Quality of Service in Shared Bus Scheduling

Simulation Program: SUMO v1.8.0

System: Linux Ubuntu v22.04.3 LTS on Oracle VM VirtualBox v7.0

//

How to Run:
1. Go to sumoproject\Updated folder and download the following files in a new folder.
> 9x9grid.net.xml,
> bus.rou.xml,
> test.add.xml,
> test.sumocfg,
> runner.py
3. Edit the configuration addresses of net-file, route-file, additional-file in test.sumocfg according to your local file addresses.
4. From the folder, open a terminal and enter "python runner.py".
5. SUMO GUI will load. Change the view setting to "real world". Run the simulation.
6. Tripinfo and stopinfo will be saved in tripinfo.xml and stopoutput.xml. Time taken by person can be seen in tripinfo.xml.
