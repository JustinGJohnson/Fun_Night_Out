# restaurant api caller
# restaurants.py
import requests, ui, os, log


# request to zomato api one restaurant at a time
def zomato_request(restaurant_id):
    # api key for zomato
    zomato_api = os.environ.get("FOOD_KEY")
    # base url for requests in the Twin Cities area
    base_url = "https://developers.zomato.com/api/v2.1/search?entity_id=826&entity_type=city"
    # header for api request
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": zomato_api}
    # adds on to base_url to create new query with start position passed in and count of 1
    url = base_url + "&start=" + str(restaurant_id) + "&count=1"
    # raw_data from API request
    raw_data = requests.get(url, headers=header)
    # log response status code
    log.write_to_log("Status code for request to Zomato API: " + str(raw_data))

    # error handling for bad API key
    if str(raw_data) == "<Response [403]>":
        ui.print_to_user("\nInvalid API key. Exiting Fun Night Out.\n")
        log.write_to_log("Bad Zomato API key, exiting program.")
        exit(0)

    # return data if response 200 (valid API key, working response)
    elif str(raw_data) == "<Response [200]>":
        # return raw_data
        return raw_data

    # handles all other status codes from API request.
    else:
        ui.print_to_user("\nStatus code: " + str(raw_data))
        ui.print_to_user("An unknown error occured with the Zomato API. Exiting Fun Night Out.\n")
        log.write_to_log("Unknown error with the Zomato API. " + str(raw_data))

# convert raw_data of api call to json format
def convert_to_json(raw_data):

    # return json obj
    return raw_data.json()


# function print_restaurant, takes start which is int value of which restaurant is printed
def print_restaurant(json_obj):
    # hopping through the json_obj and printing the necessary information
    for item in json_obj["restaurants"]:
        restaurant = item["restaurant"]
        location = restaurant["location"]
        ui.print_to_user("\nName: " + restaurant["name"])
        ui.print_to_user("Tags: " + restaurant["cuisines"])
        ui.print_to_user("$ for 2: " + str(restaurant["average_cost_for_two"]) + "$")
        ui.print_to_user("Address: " + location["address"] + "\n")

# food_start function starts restaurant API
def food_start():

    # var used for storing count number of current restaurant from API call
    restaurant_id = 0
    # init choice to "y"
    choice = "y"
    ui.print_to_user("\n*Restaraunts in the Twin Cities Area*")
    # while loop prompting user if they want info on other restaurants
    while choice != "n":
        if choice == "y":
            response = zomato_request(restaurant_id)
            json_obj = convert_to_json(response)
            print_restaurant(json_obj)
            choice = ui.prompt_for_more()
            restaurant_id+=1
        else:
            ui.print_to_user("Please enter y or n:\n")
            choice = ui.prompt_for_more()
            continue
    ui.print_to_user("\n*Main Menu*")
    log.write_to_log("Back to main menu.")
