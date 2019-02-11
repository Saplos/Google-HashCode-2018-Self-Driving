# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 19:19:12 2019

@author: Pelumi
"""

class City():
    """This instatiates the city class"""
    
    def __init__(self,siz_city,step,fleet_size,bonus):
        """This instatiates the city class attributes
        
        siz_city this defines the city size
        step     this defines the time running of the simulation
        fleet_size this refers to the fleet size
        """
        self._fleet_available=[] #This is a list of the available cars for servicing rides. Its constantly updated depending on whether the ride is already fulfilled or not
        self._fleet_in_service=[] #This is a list that monitors the cars currently in service across the city
        self._siz_city=siz_city #This is a tuple that is inputed to record the size of the city. As of this instance, no pratical use of this information has been recorded.
        self._step=step #This recognizes the number of steps that would be made 
        self._current_step=0 #This monitors the current step of the city
        self._accrued_points=0 #This is a counter for the accrued points of the model
        self._fleet_size=fleet_size #This represents the amount of vehicles present in the city for servicing rides

        
    def add_to_fleet(self,car):
        """This adds a particular car to the existing fleet"""
        self.fleet_available.append(car)
        
    def _distance_between(self,loc_1,loc_2):
        """This function evaluates the distance between two locations in the city
        loc_1 this is the first location
        loc_2 this is the second location
        """
        distance_step=abs(loc_1[0]-loc_2[0])+abs(loc_1[1]-loc_2[1])
        return distance_step
        
    def ride(self,pick_loc,drop_loc,start,finish,iden):
        """This initialises the operation of quering the system for a ride
        
        pick_loc  this represents the initial location
        drop_loc  this represents the drop off location
        start     this represents the movement of the step
        stop      this represents the drop off time
        
        """
        distance_step=self._distance_between(pick_loc,drop_loc) #This obtains the distance that needs to be travelled
        available_distance={} #This creates a dictionary in a bid to obtain the car that is closest to the drop off zone
        for item in self.fleet_available: #For loop to obtain the car at a minimum distance
            available_distance.update({item.iden:self._distance_between(pick_loc,item.loc)})
        self.fleet_available[min(available_distance)].move(drop_loc,distance_step) #This activates the movement of the car which is at a minimum distance from the drop off zone
        self.fleet_in_service.append(self.fleet_available[min(y)]) #This moves the car from the list of available cars to the list of cars currently in service
        del(self.fleet_available[min(available_distance)]) #This 
        self.accrued_points+=distance_step
        print(available_distance)
        print(self.accrued_points)
    
    def _step_update(self):
        """This carries out certain operations upon change of step"""
        for item in self.fleet_in_service:
            item.update_movement()
            if item.in_use == False:
                self.fleet_available.append(item)
                self.fleet_in_service=self.fleet_in_service.remove(item)
            else:
                pass
        
    def move_step(self):
        """This moves the city through one step"""
        if self.current_step < self.step :
            self._step_update()
            self.current_step+=1
        elif self.current_step==self.step:
            print('The City is done running')
        
        
class Car():
    """This instatiates a new car"""
    
    def __init__(self,iden,loc):
        """This initialises the car especially with location"""
        
        self.loc=loc
        self.iden=iden
        self.gbera=0
        self.movement=0
        self.required_movement=0
        self.trips=0
        self.in_use=False
        
    def move(self,new_loc,steps):
        """This makes the car move and calls for it to update its a location"""
        self.loc=(new_loc)
        self.in_use=True
        self.trips+=1
        self.required_movement=steps
    
    def update_movement(self):
        if self.gbera < self.required_movement:
            self.gbera+=1
        elif self.gbera==self.required_movement:
            self.gbera=0
            self.required_movement=0
            self.in_use=False

            
        
#This is for testing
if __name__=='__main__':
    Ibadan=City((3,4),10,2,2)
    Car1=Car(1,(0,0))
    Car2=Car(2,(0,0))
    Ibadan.add_to_fleet(Car1)
    Ibadan.add_to_fleet(Car2)
    Ibadan.ride((0,0),(1,3),2,9,1)
    print(Ibadan.current_step)
    print(Ibadan.move_step())
    print(Ibadan.current_step)