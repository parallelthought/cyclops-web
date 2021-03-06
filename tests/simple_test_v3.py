'''
Created on Jan 3, 2014

@author:  Tea Kolevska
@contact: tea.kolevska@zhaw.ch
@organization: ICCLab, Zurich University of Applied Sciences
@summary: Module to test the ceilometer service

'''

import textwrap
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'os_api')))
import ceilometer_api
import compute_api
import keystone_api
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'processes')))
import periodic

def main(argv):
    print "Hello There. This is a simple test application making a test API call to OpenStack"
    auth_uri = 'http://160.85.4.64:5000' #internal test-setup, replace it with your own value
    status, token_data = keystone_api.get_token_v3(auth_uri,False)
    if status:
        print 'The authentication was successful, below are the data we got:'
        print '--------------------------------------------------------------------------------------------------------'
        print '%1s %32s %2s %64s %1s' % ('|', 'key', '|', 'value', '|')
        print '--------------------------------------------------------------------------------------------------------'
        for key, value in token_data.iteritems():
            if key not in {'token_id'}:
                print '%1s %32s %2s %64s %1s' % ('|', key, '|', value, '|')
        print '--------------------------------------------------------------------------------------------------------'
        print 'The authentication token is: ', token_data["token_id"]
        pom=token_data["token_id"]

    else:
        print "Authentication was not successful."
    if status:
        status,tenant_list=keystone_api.get_list_tenants(pom,auth_uri)
        status,user_list=keystone_api.get_users_per_tenant(pom,auth_uri,'4e9c4e1b93124cdba2a930e98eb26ede')
        for i in range(len(user_list)):
            print '%20s %20s' %(user_list[i]["user_id"], user_list[i]["user_name"])
            
        #status, server_list = compute_api.get_server_list(token_data["token-id"], token_data["computev3"])
        #if status:
         #   print "The list of servers are printed next."
         #   print server_list
        status, meter_list = ceilometer_api.get_meter_list(pom, token_data["metering"])
        total_price=periodic.daily_count("2014-02-26",1, "323936522894416b903d3528fa971537")
        if status:
            print "The list of available meters are printed next."
            print '--------------------------------------------------------------------------------------------------------------------------'
            print '%1s %16s %2s %10s %2s %10s %2s %40s %1s %70s' % ('|','meter-name', '|', 'meter-type', '|', 'meter-unit', '|', 'meter-id', '|','resource-id')
            print '--------------------------------------------------------------------------------------------------------------------------'
            for i in range(len(meter_list)):
                print '%1s %16s %2s %10s %2s %10s %2s %40s %1s %70s' % ('|', meter_list[i]["meter-name"], '|', meter_list[i]["meter-type"], '|', meter_list[i]["meter-unit"], '|', meter_list[i]["meter-id"].strip(), '|',meter_list[i]["resource-id"])
            print '--------------------------------------------------------------------------------------------------------------------------'
 
        meter_name=raw_input("Enter meter name: ")

        st,stat_list=ceilometer_api.meter_statistics(meter_name, token_data["metering"],pom,meter_list,False)
        if st:
            print '--------------------------------------------------------------------------------------------------------------------------'
            print "The statistics for your meters is printed next."
            print '--------------------------------------------------------------------------------------------------------------------------'
            
            for i in range(len(stat_list)):
                print "Average: " + str(stat_list[i]["average"]) 
                print "Count: " + str(stat_list[i]["count"])
                print "Duration: "+ str(stat_list[i]["duration"]) 
                print "Duration end: " + str(stat_list[i]["duration-end"]) 
                print "Duration start: "+ str(stat_list[i]["duration-start"]) 
                print "Max: " + str(stat_list[i]["max"])
                print "Min: " + str(stat_list[i]["min"]) 
                print "Period: " + str(stat_list[i]["period"]) 
                print "Period end: " + str(stat_list[i]["period-end"]) 
                print "Period start: " + str(stat_list[i]["period-start"]) 
                print "Sum: " + str(stat_list[i]["sum"]) 
                print "Unit: " + str(stat_list[i]["unit"]) 
                print "Group by: " + str(stat_list[i]["group-by"]) 
                print '--------------------------------------------------------------------------------------------------------------------------'         
            print '--------------------------------------------------------------------------------------------------------------------------'
        
        print "Query initialization for meter samples function."
        status,sample_list=ceilometer_api.get_meter_samples(meter_name,token_data["metering"],pom,True,meter_list,False,"")
        if status:
            print '--------------------------------------------------------------------------------------------------------------------------'
            print "The samples for your meter are printed next."
            print '--------------------------------------------------------------------------------------------------------------------------'
            
            for i in range(len(sample_list)):
                print "Counter name: " + str(sample_list[i]["counter-name"]) 
                print "Counter unit: " + str(sample_list[i]["counter-unit"])
                print "Counter volume: "+ str(sample_list[i]["counter-volume"]) 
                print "Counter type: " + str(sample_list[i]["counter-type"]) 
                print "Message id: "+ str(sample_list[i]["message-id"]) 
                print "Project id: " + str(sample_list[i]["project-id"])
                print "Resource id: " + str(sample_list[i]["resource-id"]) 
                print "Resource metadata: " 
                print sample_list[i]["resource-metadata"]
                print "Source: " + str(sample_list[i]["source"]) 
                print "Timestamp: " + str(sample_list[i]["timestamp"]) 
                print "User ID: " + str(sample_list[i]["user-id"]) 
                print '--------------------------------------------------------------------------------------------------------------------------'         
            print '--------------------------------------------------------------------------------------------------------------------------'
        
        print "Query initialization for get resources function."
        status,resources_list=ceilometer_api.get_resources(token_data["metering"], pom,True)
        if status:
            print '--------------------------------------------------------------------------------------------------------------------------'
            print "The resources for your meter are printed next."
            print '--------------------------------------------------------------------------------------------------------------------------'
            
            for i in range(len(resources_list)):
                print "Resource id: " + str(resources_list[i]["resource-id"])
                print "Links: " 
                for j in range(len(resources_list[i]["links"])):
                    print "Href: " + str(resources_list[i]["links"][j]["href"])
                    print "Rel: " + str(resources_list[i]["links"][j]["rel"])
                print "Project id: " + str(resources_list[i]["project-id"])
                 
                print "Resource metadata: " 
                print resources_list[i]["metadata"]
                #print "Source: " + str(resources_list[i]["source"]) 

                print "User ID: " + str(resources_list[i]["user-id"]) 
                print '--------------------------------------------------------------------------------------------------------------------------'         
        
        print "Query initialization for get resources by id function."    
        resource_id=raw_input("Enter resource id: ")
        status,resources_list=ceilometer_api.get_resources_by_id(token_data["metering"], pom,resource_id)

        if status:
            print '--------------------------------------------------------------------------------------------------------------------------'
            print "The resources for your meter are printed next."
            print '--------------------------------------------------------------------------------------------------------------------------'
            
            for i in range(len(resources_list)):
                print "Resource id: " + str(resources_list[i]["resource-id"])
                print "Links: " 
                for j in range(len(resources_list[i]["links"])):
                    print "Href: " + str(resources_list[i]["links"][j]["href"])
                    print "Rel: " + str(resources_list[i]["links"][j]["rel"])
                print "Project id: " + str(resources_list[i]["project-id"])
                 
                print "Resource metadata: " 
                print resources_list[i]["metadata"]
                #print "Source: " + str(resources_list[i]["source"]) 
                #print "First sample timestamp: " + str(resources_list[i]["first-sample-timestamp"]) 
                #print "Last sample timestamp: " + str(resources_list[i]["last-sample-timestamp"]) 

                print "User ID: " + str(resources_list[i]["user-id"]) 
                print '--------------------------------------------------------------------------------------------------------------------------'         
        
        
    return True
    
if __name__ == '__main__':
    main(sys.argv[1:])
