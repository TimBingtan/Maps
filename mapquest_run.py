
import mapquest_output
import mapquest_connect



def set_locations(total_locations: int) -> list:
    '''Takes the number of locations and sets up inputs according to
       the number of locations.'''
    location_list = []
    for location in range(total_locations):
        destination = input()
        location_list.append(destination)
        
    return location_list


def set_tasks(total_tasks: int) -> list:
    '''Takes the number of tasks and sets up inputs according to
       the number of tasks.'''
    task_list = []
    for task in range(total_tasks):
        command = input()
        task_list.append(command)

    return task_list



def translate_commands(tasks: list) -> list:
    '''Translates user input into one that is able to call the command function.'''
    command_classes = []
    for task in tasks:
        if task.upper() == 'STEPS':
            command_classes.append(mapquest_output.Steps())
        elif task.upper() == 'TOTALDISTANCE':
            command_classes.append(mapquest_output.TotalDistance())
        elif task.upper() == 'TOTALTIME':
            command_classes.append(mapquest_output.TotalTime())
        elif task.upper() == 'LATLONG':
            command_classes.append(mapquest_output.LatLong())                 
        elif task.upper() == 'ELEVATION':
            command_classes.append(mapquest_output.Elevation())

    return command_classes





def commands(commands: ['list of commands'], locations: ['list of locations']):
    '''Calls the output function based on a specific class that is called.'''
    url = mapquest_connect.get_route(locations)
    json = mapquest_connect.results(url)
    try:
        for command in commands:
            command.output(json)
            print()    
    except:
        print('NO ROUTE FOUND')
    else:
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    finally:
        print()


    

def run_mapquest():
    '''Runs complete operations of the Mapquest project.'''
    print("1st input: Total Locations \n"
          +"2nd input(s): List Locations \n"
          +"3rd input: Total Tasks \n"
          +"4th input: List Tasks \n")
    
    total_locations = int(input())
    locations = set_locations(total_locations)
    total_tasks = int(input())
    command_list = set_tasks(total_tasks)
    class_list = translate_commands(command_list)
    print()
    commands(class_list, locations)



if __name__ == '__main__':
    run_mapquest()




