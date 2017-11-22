#Work in progress. This is a function library exposing all documented functions in the AppDynamics REST API. Written in python3.
import json
import requests
import xml.etree.ElementTree as ET
#from bs4 import BeautifulSoup

class Controller:
    def __init__(self, host='mycontroller.saas.appdynamics.com', un='un', pw='pw', account_name='my_account',
                 https_enabled='t', bus_app_dict=''):
        self.update(host, un, pw, account_name, https_enabled, bus_app_dict)

    def update(self, host, un, pw, account_name, https_enabled, bus_app_dict):
        self.host = host
        self.un = un
        self.pw = pw
        self.account_name = account_name
        self.user_at_account_name = self.un + "@" + self.account_name
        self.https_enabled = https_enabled
        self.bus_app_dict = bus_app_dict
        if self.https_enabled == 't':
            self.url = 'https://' + host
        elif self.https_enabled == 'f':
            self.url = 'http://' + host
        else:
            print('t or f not entered so default chosen, default - SSL=True')

    def reset(self):
        self.update('', '', '', '', '', '')

class AnalyticsEventsService:
    #create_event_schema('sample_schema', 'https://analytics.api.appdynamics.com:443',
    # 'c61d187e-83c1-4d27-9182-9deeadba44e2', 'cdk-test_8d3e1202-40d1-4633-afac-82ef2797dafa', 'create_schema.json')
    def __init__(self, es_url='https://analytics.api.appdynamics.com:443',
                 events_api_key='',
                 events_api_account_name=''):
        self.update(es_url, events_api_key, events_api_account_name)

    def update(self, es_url, events_api_key, events_api_account_name):
        self.es_url = es_url
        self.events_api_key = events_api_key
        self.events_api_account_name = events_api_account_name

    def reset(self):
        self.update('', '', '', '')

def print_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("0. Exit")
    print("1. Menu Option 1 - SUB-MENU 1 - Application Model API")
    print("2. Menu Option 2 - SUB-MENU 2 - Metric and Snapshot API")
    print("3. Menu Option 3 - SUB-MENU 3 - Alert and Respond API")
    print("4. Menu Option 4 - SUB-MENU 4 - Configuration API")
    print("5. Menu Option 5 - SUB-MENU 5 - Configuration Import and Export API")
    print("6. Menu Option 6 - SUB-MENU 6 - Analytics Events API")
    print("7. Menu Option 7 - SUB-MENU 7 - RBAC API")
    print("8. Menu Option 8 - SUB-MENU 8 - MISC API")
    print(67 * "-")

def print_sub_menu_1():
    print(30 * "-", "SUB-MENU 1 - Application Model API", 30 * "-")
    print("0. Exit to Main Menu")
    print("1. Sub-menu Option 1 - Configure Source Controller")
    print("2. Sub-menu Option 2 - Retrieve All Business Applications")
    print("3. Sub-menu Option 3 - Retrieve All Business Transactions in a Business Application")
    print("4. Sub-menu Option 4 - Retrieve All Tiers in a Business Application")
    print("5. Sub-menu Option 5 - Retrieve All Registered Backends in a Business Application With Their Properties")
    print("6. Sub-menu Option 6 - Retrieve Node Information for All Nodes in a Business Application")
    print("7. Sub-menu Option 7 - Retrieve Node Information by Node Name")
    print("8. Sub-menu Option 8 - Retrieve Node Information for All Nodes in a Tier")
    print("9. Sub-menu Option 9 - Retrieve Tier Information by Tier Name")
    print(67 * "-")

def print_sub_menu_2():
    print(30 * "-", "SUB-MENU 2 - Metric and Snapshot API", 30 * "-")
    print("0. Exit to Main Menu")
    print("1. Sub-menu Option 1 - Configure Source Controller")
    print("2. Sub-menu Option 2 - Retrieve Metric Hierarchy")
    print("3. Sub-menu Option 3 - Retrieve Metric Data")
    print("4. Sub-menu Option 4 - Retrieve Transaction Snapshots")
    print("5. Sub-menu Option 5 - Retrieve Controller Audit History")
    print("6. Sub-menu Option 6 - Configure Metric Retention by Account")
    print("7. Sub-menu Option 7 - Configure Metric Retention by Application")
    print(67 * "-")

def print_sub_menu_3():
    print(30 * "-", "SUB-MENU 3 - Alert and Respond API", 30 * "-")
    print("0. Exit to Main Menu")
    print("1. Sub-menu Option 1 - Configure Source Controller")
    print("2. Sub-menu Option 2 - Retrieve All Health Rule Violations in a Business Application")
    print("3. Sub-menu Option 3 - Retrieve Event Data")
    print("4. Sub-menu Option 4 - Create Events")
    print("5. Sub-menu Option 5 - Create a Custom Event")
    print("6. Sub-menu Option 6 - Create Custom URLS for Notifications")
    print("7. Sub-menu Option 7 - Create and Delete Action Suppressions")
    print("8. Sub-menu Option 8 - Retrieve All Existing Action Suppressions")
    print("9. Sub-menu Option 9 - Retrieve a Specific Action Suppression by ID")
    print("10. Sub-menu Option 10 - Create a New Action Suppression")
    print("11. Sub-menu Option 11 - Delete a Specific Action Suppression by ID")
    print(67 * "-")

def print_sub_menu_4():
    print(30 * "-", "SUB-MENU 4 - Configuration API", 30 * "-")
    print("0. Exit to Main Menu")
    print("1. Sub-menu Option 1 - Configure Source Controller")
    print("2. Sub-menu Option 2 - Create AppD User")
    print("3. Sub-menu Option 3 - Modify AppD User")
    print("4. Sub-menu Option 4 - Include a Business Transaction for Monitoring")
    print("5. Sub-menu Option 5 - Exclude a Business Transaction from Monitoring")
    print("6. Sub-menu Option 6 - Retrieve All Controller Settings")
    print("7. Sub-menu Option 7 - Retrieve a Controller Setting by Name")
    print("8. Sub-menu Option 8 - Configure Global Controller Settings")
    print("9. Sub-menu Option 9 - Mark Nodes as Historical")
    print(67 * "-")

def print_sub_menu_5():
    print(30 * "-", "SUB-MENU 5 - Configuration Import and Export API", 30 * "-")
    print("0. Exit to Main Menu")
    print("1. Sub-menu Option 1 - Configure Source Controller")
    print("2. Sub-menu Option 2 - Export Actions from an Application")
    print("3. Sub-menu Option 3 - Import Actions into an Application")
    print("4. Sub-menu Option 4 - Export Email Action Templates from an Account")
    print("5. Sub-menu Option 5 - Import Email Action Templates")
    print("6. Sub-menu Option 6 - Export HTTP Request Action Templates from an Account")

    print("7. Sub-menu Option 7 - Import HTTP Action Templates into an Account")
    print("8. Sub-menu Option 8 - Export Custom Dashboards and Templates")
    print("9. Sub-menu Option 9 - Import Custom Dashboards and Templates")
    print("10. Sub-menu Option 10 - Export Health Rules from an Application")
    print("11. Sub-menu Option 11 - Import Health Rules into an Application")
    print("12. Sub-menu Option 12 - Export Transaction Detection Rules for All Entry Point Types")
    print("13. Sub-menu Option 13 - Import Transaction Detection Rules for All Entry Point Types")
    print("14. Sub-menu Option 14 - Export a Transaction Detection Rule for an Entry Point Type")
    print("15. Sub-menu Option 15 - Import Transaction Detection Rule for an Entry Point Type ")
    print("16. Sub-menu Option 16 - Export Policies")
    print("17. Sub-menu Option 17 - Import Policies")
    print("18. Sub-menu Option 18 - Export Application Analytics Dynamic Service Configuration")
    print("19. Sub-menu Option 19 - Import Application Analytics Dynamic Service Configuration")
    print(67 * "-")

def print_sub_menu_6():
    print(30 * "-", "SUB-MENU 6 - Analytics Events API", 30 * "-")
    print("0. Exit to Main Menu")
    print("1. Sub-menu Option 1 - Configure Source Controller")
    print("2. Sub-menu Option 2 - Publish Events")
    print("3. Sub-menu Option 3 - Create Event Schema")
    print("4. Sub-menu Option 4 - Retrieve Event Schema")
    print("5. Sub-menu Option 5 - Update Event Schema")
    print("6. Sub-menu Option 6 - Delete Event Schema")
    print("7. Sub-menu Option 7 - Single Query")
    print("8. Sub-menu Option 7 - Multi Query JSON")
    print(67 * "-")

def print_sub_menu_7():
    print(30 * "-", "SUB-MENU 7 - RBAC API", 30 * "-")
    print("0. Exit to Main Menu")
    print("1. Sub-menu Option 1 - Configure Source Controller")
    print("2. Sub-menu Option 2 - Create User")
    print("3. Sub-menu Option 3 - Get User by ID")
    print("4. Sub-menu Option 4 - Get User by Name")
    print("5. Sub-menu Option 5 - Get All Users")
    print("6. Sub-menu Option 6 - Update User")
    print("7. Sub-menu Option 7 - Delete User")
    print()
    print("8. Sub-menu Option 8 - Create Group")
    print("9. Sub-menu Option 9 - Get Group by ID")
    print("10. Sub-menu Option 10 - Get Group by Name")
    print("11. Sub-menu Option 11 - Get All Groups")
    print("12. Sub-menu Option 12 - Update Group")
    print("13. Sub-menu Option 13 - Delete Group")
    print("14. Sub-menu Option 14 - Add User to Group")
    print("15. Sub-menu Option 15 - Remove User from Group")
    print()
    print("16. Sub-menu Option 16 - Create Role")
    print("17. Sub-menu Option 17 - Add Role to User")
    print("18. Sub-menu Option 18 - Remove Role from User")
    print("19. Sub-menu Option 19 - Add Role to Group")
    print("20. Sub-menu Option 20 - Remove Role from Group")
    print("21. Sub-menu Option 21 - Get Role by ID")
    print("22. Sub-menu Option 22 - Get Role by Name")
    print("23. Sub-menu Option 23 - Get All Roles")
    print("24. Sub-menu Option 24 - Update Role")
    print("25. Sub-menu Option 25 - Delete Role")
    print(67 * "-")


def print_sub_menu_8():
    print(30 * "-", "SUB-MENU 8 - MISC FUNCTIONS", 30 * "-")
    print("0. Exit to Main Menu")
    print("1. Sub-menu Option 1 - Configure Source Controller")
    print("2. Sub-menu Option 2 - ENABLE new BT config 2.0 for selected bus app")
    print("3. Sub-menu Option 3 - DISABLE new BT config 2.0 for selected bus app")
    print("4. Sub-menu Option 4 - Mark all nodes as historical by tier based on "
          "no metric data for time frame")
    print("5. Sub-menu Option 5 - ")
    print("6. Sub-menu Option 6 - ")
    print("7. Sub-menu Option 7 - ")
    print(67 * "-")

def input_source_controller():
    host = str(input("Enter source controller hostname: "))
    un = str(input("Enter source controller username: "))
    pw = str(input("Enter source controller password: "))
    account_name = str(input("Enter source controller account name: "))
    https_enabled = str(input("Enter 't' for HTTPS (SSL) or 'f' for HTTP: "))
    print("you just entered https_enabled: ", https_enabled)
    mc.update(host, un, pw, account_name, https_enabled)
    print(
        "un: " + mc.un + " pw: " + " " + mc.pw + " account name:" + mc.account_name + " HTTP Enabled = "
        + mc.https_enabled)
    return mc

def input_source_es():
    es_url = str(input("Enter Events Service URL: "))
    events_api_key = str(input("Enter Events API Key: (created under Analtyics > Configuration > API Keys)"))
    events_api_account_name = str(input("Enter Events API Account Name (found on license page, Global Account Name): "))
    es.update(es_url, events_api_key, events_api_account_name)

def load_all_apps():
    bus_app_resp = requests.get(mc.url + '/controller/rest/applications?output=JSON',
                                auth=(mc.user_at_account_name, mc.pw))
    json_resp = json.loads(bus_app_resp.content.decode('utf-8'))
    app_dict = {}
    app_counter = 0
    for item in json_resp:
        app_element = json_resp[app_counter]
        app_id = app_element["id"]
        app_name = app_element["name"]
        #below yields app_name=value, app_id=key
        app_dict[app_id] = app_name
        #print("app ID: ", app_id)
        #print("app name: ", app_name)
        app_counter += 1
    return app_dict

def list_all_apps(app_dict):
    print('APP ID, APP NAME')
    for key, value in app_dict.items():
        print(key, value)

def get_account_id():
    resp = requests.get(mc.url + '/controller/api/accounts/myaccount', auth=(mc.user_at_account_name, mc.pw))
    json_resp = json.loads(resp.content.decode('utf-8'))
    accountId = json_resp['id']
    print("acc ID: " + accountId)
    return accountId

#CURRENT
def does_app_exist(app_dict, app_name):
    #for key, value in app_dict.items():
        #print('app_dict - value : key')
        #print(value, key)
    if app_name in app_dict.values():
        print('App name found')
        return True
    else:
        print('App name not found, exiting to sub-menu')
        return False

#PROBLEM WITH METHOD, assigns
def get_app_id_and_does_app_exist(app_name_in):
    bus_app_resp = requests.get(mc.url + '/controller/rest/applications?output=JSON',
                                auth=(mc.user_at_account_name, mc.pw))
    json_resp = json.loads(bus_app_resp.content.decode('utf-8'))
    d = {}
    a = 0
    for child in json_resp:
        app_element = json_resp[a]
        app_id = app_element["id"]
        app_name = app_element["name"]
        d[app_name] = app_id
        a += 1
    if app_name_in in d:
        return d[app_name_in], True
    else:
        return '', False

#WORKS
#GET /controller/rest/applications/application_name/tiers
def does_tier_exist(app_dict, app_name, tier_name_to_search_for):
    if app_name in app_dict.values():
        r = requests.get(mc.url + '/controller/rest/applications/{}/tiers?output=JSON'.format(app_name),
                         auth=(mc.user_at_account_name, mc.pw))
        json_resp = json.loads(r.content.decode('utf-8'))
        tier_dict = {}
        tier_counter = 0
        for item in json_resp:
            tier_element = json_resp[tier_counter]
            tier_id = tier_element["id"]
            tier_name = tier_element["name"]
            tier_dict[tier_id] = tier_name
            tier_counter+=1
        if tier_name_to_search_for in tier_dict.values():
            print('Tier name found')
            return True
        else:
            print('Tier name not found')
            return False
    else:
        print('App name not found')
        return False

#GET /controller/rest/applications/application_name/nodes
def does_node_exist(app_dict, app_name, node_name_to_search_for):
    if app_name in app_dict.values():
        r = requests.get(mc.url + '/controller/rest/applications/{}/nodes?output=JSON'.format(app_name),
                         auth=(mc.user_at_account_name, mc.pw))
        json_resp = json.loads(r.content.decode('utf-8'))
        node_dict = {}
        node_counter = 0
        for item in json_resp:
            node_element = json_resp[node_counter]
            node_id = node_element["id"]
            node_name = node_element["name"]
            node_dict[node_id] = node_name
            node_counter+=1
        if node_name_to_search_for in node_dict.values():
            print('Node name found')
            return True
        else:
            print('Node name not found')
            return False
    else:
        print('App name not found')
        return False

def get_tier_id_and_does_tier_exist(app_name='', tier_name=''):
    print()

def get_node_id_and_does_node_exist(app_name='', node_name=''):
    print()

#'/controller/rest/applications/{}/nodes?output=JSON
def get_node_id(app_name='', node_name_to_find=''):
    app_id = get_app_id_and_does_app_exist(app_name)
    if app_id[1]:
        print('app found')
        print("app id = true, appID=", app_id[0])
        app_id_str = str(app_id[0])
        node_app_resp = requests.get(mc.url + '/controller/rest/applications/{}/nodes?output=JSON'.format(app_id_str),
                                    auth=(mc.user_at_account_name, mc.pw))
        if node_app_resp.status_code == 200:
            json_resp = json.loads(node_app_resp.content.decode('utf-8'))
            a = 0
            d = {'key': 'value'}
            for child in json_resp:
                node_element = json_resp[a]
                # print(app_element)
                node_id = node_element["id"]
                node_name = node_element["name"]
                d[node_name] = node_id
                a+=1
            if node_name_to_find in d:
                print('node found')
                return d[node_name_to_find], True
            else:
                print('node not found')
                return 'node_not_found', False
        else:
            print("status code != 200")
            return 'status_code=200', False
    else:
        print('app not found')
        return 'app_not_found', False

#'/controller/rest/applications/{}/nodes?output=JSON
#function for finding node name by nodeID & also returning if nodeID exists
def get_tier_id(app_name='', tier_name_to_find=''):
    app_id = get_app_id_and_does_app_exist(app_name)
    if app_id[1]:
        print('app found')
        print("app id = true, appID=", app_id[0])
        app_id_str = str(app_id[0])
        tier_app_resp = requests.get(mc.url + '/controller/rest/applications/{}/tiers?output=JSON'.format(app_id_str),
                                    auth=(mc.user_at_account_name, mc.pw))
        if tier_app_resp.status_code == 200:
            json_resp = json.loads(tier_app_resp.content.decode('utf-8'))
            a = 0
            d = {'key': 'value'}
            for child in json_resp:
                tier_element = json_resp[a]
                # print(app_element)
                tier_id = tier_element["id"]
                tier_name = tier_element["name"]
                d[tier_name] = tier_id
                a+=1
            if tier_name_to_find in d:
                print('tier found')
                return d[tier_name_to_find], True
            else:
                print('tier not found')
                return 'tier_not_found', False
        else:
            print("status code != 200")
            return 'status_code=200', False
    else:
        print('app not found')
        return 'app_not_found', False

def load_controller_hierarchy():
    app_resp = requests.get(mc.url + '/controller/rest/applications?output=JSON',
                                auth=(mc.user_at_account_name, mc.pw))
    print(app_resp.content)
    print(app_resp)
    app_response_json = json.loads(app_resp.content.decode('utf-8'))
    app_dict = {}
    tier_dict = {}
    node_dict = {}
    app_counter = 0
    #tier_counter = 0
    #node_counter = 0
    for item in app_response_json:
        app_element = app_response_json[app_counter]
        print(app_element)
        app_id = app_element["id"]
        app_name = app_element["name"]
        app_dict[app_name] = app_id
        print("app_id: ", app_id)
        print("app_name" ,app_name)
        tier_resp = \
            requests.get('https://cdk-test.saas.appdynamics.com/controller/rest/applications/{}/tiers?output=JSON'
                         .format(app_id),
                         auth=(mc.user_at_account_name, mc.pw))
        tier_response_json = json.loads(tier_resp.content.decode('utf-8'))
        tier_counter = 0
        for item in tier_response_json:
            tier_element = tier_response_json[tier_counter]
            tier_id = tier_element["id"]
            tier_name = tier_element["name"]
            tier_dict[tier_name] = tier_id
            print("tier ID: ", tier_id)
            print("tier name: ", tier_name)
            tier_counter+=1

        #GET /controller/rest/applications/application_name/nodes
        node_resp = requests.get(mc.url + '/controller/rest/applications/{}/nodes?output=JSON'
                                 .format(app_id),
                                 auth=(mc.user_at_account_name, mc.pw))
        node_response_json = json.loads(node_resp.content.decode('utf-8'))
        node_counter = 0
        for item in node_response_json:
            node_element = node_response_json[node_counter]
            node_id = node_element["id"]
            node_name = node_element["name"]
            node_dict[node_name] = node_id
            print("node ID: ", node_id)
            print("node name: ", node_name)
            node_counter+=1

        app_counter+=1
        #how can we return a tuple from this function with a list for apps, tiers, & nodes?
    return app_dict

def list_all_apps_xml():
    bus_app_resp = str(requests.get(mc.url + '/controller/rest/applications', auth=(mc.user_at_account_name, mc.pw)).text)
    busAppRoot = ET.fromstring(bus_app_resp)
    d = {}
    a = 0
    for child in busAppRoot:
        app_name = busAppRoot[a][1].text
        app_id = busAppRoot[a][0].text
        d[app_name] = app_id

        #getting null pointer exceptions for below code. must handle case where <description></description> field is empty
        #if busAppRoot[a][2].text == "":
        #    print('No bus app description')
        #else:
        #    app_description = busAppRoot[a][2].text
        #    print('bus app description: ', app_description)
        #appDescription = busAppRoot[a][2].text
#        print(app_name)
        a=a+1
    return d

#GET /controller/rest/applications/application_name/tiers
def list_all_tiers(list_tiers_from_app_name=''):
    tier_resp = requests.get(mc.url + '/controller/rest/applications/{}/tiers?output=JSON'.format(list_tiers_from_app_name),
                                    auth=(mc.user_at_account_name, mc.pw))
    json_resp = json.loads(tier_resp.content.decode('utf-8'))
    tier_dict = {}
    a = 0
    print('TIER ID, TIER NAME')
    for item in json_resp:
        tier_element = json_resp[a]
        tier_id = tier_element["id"]
        tier_name = tier_element["name"]
        tier_dict = tier_id
        print(tier_id, tier_name)
        a+=1
    return tier_dict

#GET /controller/rest/applications/application_name/business-transactions
def list_all_transactions_from_app(list_transactions_from_app_name=''):
    bt_dict = {}
    # print("un: " + mc.un + " pw: " + mc.pw + " " + mc.url)
    transaction_resp = str(requests.get(mc.url + '/controller/rest/applications/{}/business-transactions'.format(list_transactions_from_app_name),
                                auth=(mc.user_at_account_name, mc.pw)).text)
    transaction_root = ET.fromstring(transaction_resp)
    print('ID, NAME')
    a = 0
    for child in transaction_root:
        transaction_id = transaction_root[a][0].text
        transaction_name = transaction_root[a][1].text
        print(transaction_id, transaction_name)
        a = a + 1

# GET /controller/rest/applications/application_name/business-transactions
def list_all_transactions_from_app_json(list_transactions_from_app_name=''):
        bt_internal_name_dict = {'key': 'value'}
        bt_renamed_in_ui_dict = {'key':'value'}
        bt_internal_names_list = []
        # print("un: " + mc.un + " pw: " + mc.pw + " " + mc.url)
        transaction_resp = requests.get(
            mc.url + '/controller/rest/applications/{}/business-transactions?output=JSON'.format(list_transactions_from_app_name),
            auth=(mc.user_at_account_name, mc.pw))
        bt_json_resp = json.loads(transaction_resp.content.decode('utf-8'))
        print('bt json resp: ', bt_json_resp)
        a = 0
        for item in bt_json_resp:
            element = bt_json_resp[a]
            app_id = element["id"]
            name = element["name"]
            internal_name = element["internalName"]
            entry_point_type = element["entryPointType"]


            print("ID: ", app_id)
            print("name: ", name)
            print("internal name: ", internal_name)
            print("tier ID: ", element["tierId"])
            print("entry point type: ", entry_point_type)
            print("background: ", element["background"])
            print("tier name: ", element["tierName"])
            if name != internal_name:
                str = "BT name: {} is NOT EQUAL to BT internal name: {}".format(name, internal_name)
                print(str)
                print("consider creating a custom rule for this BT as best practice instead of renaming through UI")
                bt_renamed_in_ui_dict[name] = internal_name
                bt_internal_name_dict[internal_name] = app_id

            #make list of all servlet internal_name's BTs detected
            if entry_point_type == "SERVLET":
                bt_internal_names_list.append(internal_name)

            print()
            a = a + 1
        return bt_renamed_in_ui_dict

#GET /controller/rest/applications/application_name/backends
def list_all_backends_with_props_from_app(list_all_backends_with_props_from_app_name):
    backend_resp = requests.get(mc.url + '/controller/rest/applications/{}/backends?output=JSON'.format(list_all_backends_with_props_from_app_name),
                                 auth=(mc.user_at_account_name, mc.pw))
    backend_json_resp = json.loads(backend_resp.content.decode('utf-8'))
    counter = 0
    for item in backend_json_resp:
        element = backend_json_resp[counter]
        print("ID: ", element["id"])
        print("Name: ", element["name"])
        print("Type: ", element["exitPointType"])
        print("Property name: ", element["properties"][0]["name"])
        print("Property ID: ", element["properties"][0]["id"])
        print("Property value: ", element["properties"][0]["value"])
        print()
        counter += 1

#GET /controller/rest/applications/application_name/nodes
def list_all_nodes_with_props_from_app(list_all_nodes_from_app_name):
    node_resp = requests.get(mc.url + '/controller/rest/applications/{}/nodes?output=JSON'.format(list_all_nodes_from_app_name),
                                auth=(mc.user_at_account_name, mc.pw))
    node_json_resp = json.loads(node_resp.content.decode('utf-8'))
    counter=0
    for item in node_json_resp:
        element = node_json_resp[counter]
        print("NODE NAME: ", element["name"])
        print("node type: ", element["type"])
        print("id: ", element["id"])
        print("app agent version: ", element["appAgentVersion"])
        print("agent type: ", element["agentType"])
        print("node unique local Id: ", element["nodeUniqueLocalId"])
        print("machine Id: ", element["machineId"])
        print("machine OS type: ", element["machineOSType"])
        print("IP addresses: ", element["ipAddresses"])
        print("machine name: ", element["machineName"])
        print("machine agent version: ", element["machineAgentVersion"])
        print("app agent present for machine agent: ", element["appAgentPresent"])
        print("tier Id: ", element["tierId"])
        print("tier name: ", element["tierName"])
        print("machine agent present: ", element["machineAgentPresent"])
        print()
        counter+=1

#GET /controller/rest/applications/application_name/nodes/node_name
def get_node_info_by_node_name(app_name, node_name):
    node_resp = requests.get(mc.url + '/controller/rest/applications/{}/nodes/{}?output=JSON'.format(app_name, node_name),
                                auth=(mc.user_at_account_name, mc.pw))
    jsonResponseHolder = json.loads(node_resp.content.decode('utf-8'))
    #print(jsonResponseHolder)

    counter = 0
    for item in jsonResponseHolder:
        element = jsonResponseHolder[counter]
        #print(element)
        print("app agent version: ", element["appAgentVersion"])
        print("machine agent version: ", element["machineAgentVersion"])
        print("agent type: ", element["agentType"])

        print("type: ", element["type"])
        print("machine name: ", element["machineName"])
        print("app agent present: ", element["appAgentPresent"])

        print("node unique local Id: ", element["nodeUniqueLocalId"])
        print("machine Id: ", element["machineId"])
        print("machine OS type: ", element["machineOSType"])

        print("tier Id: ", element["tierId"])
        print("tier name: ", element["tierName"])
        print("machine agent present: ", element["machineAgentPresent"])

        print("NODE name: ", element["name"])
        print("IP addresses: ", element["ipAddresses"])
        print("ID: ", element["id"])
        print()
        counter += 1

#8 - testing sub-menu 8
#Retrieve Node Information for All Nodes in a Tier
#GET /controller/rest/applications/application_name/tiers/tier_name/nodes
def get_all_node_info_for_tier(app_name, tier_name):
    node_resp = requests.get(mc.url + '/controller/rest/applications/{}/tiers/{}/nodes?output=JSON'.format(app_name, tier_name),
                                auth=(mc.user_at_account_name, mc.pw))
    json_resp = json.loads(node_resp.content.decode('utf-8'))
    #node_dict = {}
    counter = 0
    for item in json_resp:
        element = json_resp[counter]
        node_name = element["name"]
        node_id = element["id"]
        #node_dict[node_name] = node_id
        print("app agent version: ", element["appAgentVersion"])
        print("machine agent version: ", element["machineAgentVersion"])
        print("agent type: ", element["agentType"])

        print("type: ", element["type"])
        print("machine name: ", element["machineName"])
        print("app agent present: ", element["appAgentPresent"])

        print("node unique local Id: ", element["nodeUniqueLocalId"])
        print("machine Id: ", element["machineId"])
        print("machine OS type: ", element["machineOSType"])

        print("tier Id: ", element["tierId"])
        print("tier name: ", element["tierName"])
        print("machine agent present: ", element["machineAgentPresent"])

        print("NODE name: ", element["name"])
        print("IP addresses: ", element["ipAddresses"])
        print("ID: ", element["id"])
        print()
        counter += 1

#sub-menu 9
#Retrieve Tier Information by Tier Name
#GET /controller/rest/applications/application_name/tiers/tier_name
def get_tier_info_by_tier_name(app_name, tier_name):
    node_resp = requests.get(mc.url + '/controller/rest/applications/{}/tiers/{}?output=JSON'.format(app_name, tier_name),
                                auth=(mc.user_at_account_name, mc.pw))
    json_resp = json.loads(node_resp.content.decode('utf-8'))
    counter = 0
    for item in json_resp:
        element = json_resp[counter]
        #print(element)
        print("agent type: ", element["agentType"])
        print("name: ", element["name"])
        print("description: ", element["description"])
        print("ID: ", element["id"])
        print("number of nodes: ", element["numberOfNodes"])
        print("type: ", element["type"])
        counter += 1

###############################################################################
#Metric and Snapshot API Functions below
###############################################################################
#GET /controller/rest/applications/application_name/metric-data
def retrieve_metric_hierarchy(app_name):
    node_resp = requests.get(
        mc.url + '/controller/rest/applications/{}/metrics?output=JSON'.format(app_name),
        auth=(mc.user_at_account_name, mc.pw))
    json_resp = json.loads(node_resp.content.decode('utf-8'))
    counter = 0
    for item in json_resp:
        element = json_resp[counter]
        #print(element)
        print("name: ", element['name'])
        print("type: ", element['type'])
        print()
        counter += 1

#BEFORE_NOW: To use this value, you must also specify the "duration-in-mins" parameter.
#BEFORE_TIME: To use this value, you must also specify the "duration-in-mins" and "end-time" parameters.
#AFTER_TIME: To use this value, you must also specify the "duration-in-mins" and "start-time" parameters.
#BETWEEN_TIMES: To use this value, you must also specify the "start-time" and "end-time" parameters. The "BETWEEN_TIMES" range includes the start- time and excludes the end-time.
def set_time():
    print()

#End%20User%20Experience%7CBase%20Pages%7Cnitra.f1rd.com%2Fsla-test%2Fserviceapptform%7CSynthetic%20Fully%20Loaded%20Time%20%28ms%29
#bool_rollup
def retrieve_metric_data(app_name, metric_path, time_in_minutes, bool_rollup):
    node_resp = requests.get(
        mc.url + '/controller/rest/applications/{}/'
                 'metric-data?metric-path={}&time-range-type=BEFORE_NOW&duration-in-mins={}&output=JSON&rollup={}'
        .format(app_name, metric_path, time_in_minutes, bool_rollup),
        auth=(mc.user_at_account_name, mc.pw))
    json_resp = json.loads(node_resp.content.decode('utf-8'))
    counter = 0
    for item in json_resp:
        element = json_resp[counter]
        print(element)
        print('metric name: ', element['metricName'])
        print('metric ID: ', element['metricId'])
        print('metric path: ', element['metricPath'])
        print('frequency: ', element['frequency'])
        metric_values = element['metricValues']
        print('metric values element: ', metric_values)
        metric_values_counter = 0
        for item in metric_values:
            print('\toccurrences: ', element['metricValues'][metric_values_counter]['occurrences'])
            print('\tcurrent: ', element['metricValues'][metric_values_counter]['current'])
            print('\tmin: ', element['metricValues'][metric_values_counter]['min'])
            print('\tmax: ', element['metricValues'][metric_values_counter]['max'])
            print('\tstartTimeInMillis: ', element['metricValues'][metric_values_counter]['startTimeInMillis'])
            print('\tuseRange: ', element['metricValues'][metric_values_counter]['useRange'])
            print('\tcount: ', element['metricValues'][metric_values_counter]['count'])
            print('\tsum: ', element['metricValues'][metric_values_counter]['sum'])
            print('\tvalue: ', element['metricValues'][metric_values_counter]['value'])
            print('\tstandardDeviation: ', element['metricValues'][metric_values_counter]['standardDeviation'])
            print()
            metric_values_counter += 1
        print()

#GET /controller/rest/applications/application_name/request-snapshots
def retrieve_snapshots(app_name, time_range_type, duration_in_min, guids, archived_bool, deep_dive_policy, app_component_ids, app_component_node_ids, bt_ids, user_exp, first_in_chain, need_props,
                       need_exit_calls, execution_time_in_millis, session_id, user_principle_id, error_ids, starting_req_id, ending_req_id, error_occured,
                       diagnostic_snapshot, bad_req, diagnostic_sesh_guid, data_collector_name, data_collector_type,
                       output, max_results):
    print()

def retrieve_audit_hist():
    print()

#POST /controller/actiontemplate/email
def import_email_action_templates_ex(json_filename):
    with open(json_filename, 'rb') as f:
        r = requests.post(mc.url + '/controller/actiontemplate/email', auth=(mc.user_at_account_name, mc.pw), files={'file=@' + json_filename: f})
    f.close()
    print(r.status_code)
    print(r.content)

#403 forblidden returned when running cURL. I have all necessary permissions.  bug?
def config_metric_reten_by_account(account_id):
    r = requests.post(mc.url + '/controller/api/accounts/{}/metricstaleduration/3'.format(account_id), auth=(mc.user_at_account_name, mc.pw))
    print("r: ", r)
    print("HTTP Return Code: ", r.status_code)
    print("request content: ", r.content)

def config_metric_reten_by_app():
    print()

#####################################################################
#SUB-MENU 3 - Alert and Respond API
#####################################################################

#Sub-menu Option 2 - Retrieve All Health Rule Violations in a Business Application
#/controller/rest/applications/application_id/problems/healthrule-violations
def retrieve_all_hr_violations_in_app(app_name, duration_in_mins):
    hrv_resp = requests.get(
        mc.url +
        '/controller/rest/applications/{}/problems/healthrule-violations?time-range-type=BEFORE_NOW&duration-in-mins={}&output=JSON'
        .format(app_name, duration_in_mins),
        auth=(mc.user_at_account_name, mc.pw))
    json_resp = json.loads(hrv_resp.content.decode('utf-8'))
    print("resp: ", json_resp)
    counter = 0
    for item in json_resp:
        element = json_resp[counter]
        print("element: ", element)
        counter += 1
    print()

#curl --user user1@customer1:secret http://demo.appdynamics.com/
# controller/rest/applications/6/events?time-range-type=BEFORE_NOW\&duration-in-mins=30\&event-types=%20APPLICATION_ERROR,DIAGNOSTIC_SESSION\&severities=INFO,WARN,ERROR
def retrieve_event_data(app_name, time_in_min, event_types, severities):
    a_resp = requests.get(mc.url + '/controller/rest/applications/{}/events?time-range-type=BEFORE_NOW&duration-in-mins={}&event-types={}&severities={}&output=JSON'.format(app_name, time_in_min, event_types, severities),
                          auth=(mc.user_at_account_name, mc.pw))
    #print(a_resp)
    #print(a_resp.content)
    json_resp=json.loads(a_resp.content.decode('utf-8'))
    counter = 0
    for item in json_resp:
        element = json_resp[counter]
        #print('element: ', element)

        type = element['type']
        print('type: ', type)

        sever = element['severity']
        print('severity: ', sever)

        summary = element['summary']
        print('summary: ', summary)


        affected_entities = element['affectedEntities']
        print(affected_entities)

        entity_counter=0
        for item in affected_entities:
            print('\tentity name:', element['affectedEntities'][entity_counter]['name'])
            print('\tentity ID: ', element['affectedEntities'][entity_counter]['entityId'])
            print('\tentity type: ', element['affectedEntities'][entity_counter]['entityType'])
            entity_counter+=1
            print()
        print()
        print()
        counter += 1



#POST /controller/rest/applications/application_id/events
def create__event(app_id, summary, comment, event_type, severity):
    print()

def create_custom_events():
    print()

#POST /controller/rest/accounts/customer_name/update-controller-url
def create_custom_urls():
    print()

def create_action_supps():
    print()

#GET /controller/api/accounts/account_id/applications/application_id/actionsuppressions
def retrieve_all_action_supps(acc_id, app_name):
    act_resp = requests.get(
        mc.url + '/controller/api/accounts/{}/applications/{}/actionsuppressions'.format(acc_id,app_name),
        auth=(mc.user_at_account_name, mc.pw))
    print("resp content: ", act_resp.content)
    print("resp: ", act_resp)
    print("resp status code: ", act_resp.status_code)
    json_resp = json.loads(act_resp.content.decode('utf-8'))

    print('json resp: ', json_resp)

    #json_resp = json.loads(act_resp.content.decode('utf-8'))

    act_root = json_resp["actions"]
    print("act root: ", act_root)

    if "actionSuppressions" in json_resp:
        act_supp_root = json_resp["actionSuppressions"]
        print("sup root: ", act_supp_root)
        act_supp_root_counter = 0
        for item in act_supp_root:
            element = act_supp_root[act_supp_root_counter]
            print("el: ", element)
            id = element['id']
            name = element['name']
            time_range = element['timeRange']
            hr_ids = element['healthRuleIds']
            affects = element['affects']

            print('id: ', id)
            print('name: ', name)
            print('time range: ', time_range)
            print('hr_ids: ', hr_ids)
            print('affects: ', affects)
            act_supp_root_counter += 1
    else:
        print("No action suppressions exist for this app, exiting...")

#/controller/api/accounts/account_id/applications/application_id/actionsuppressions/actionsuppression_id
#/controller/api/accounts/4/applications/113/actionsuppressions/1
def retrieve_specfic_action_supp_by_id(acc_id, app_id, supp_id):
    conn_str = mc.url + '/controller/api/accounts/{}/applications/{}/actionsuppressions/{}'.format(acc_id, app_id, supp_id)
    print('url str: ', conn_str)
    act_resp = requests.get(
        conn_str,
        auth=(mc.user_at_account_name, mc.pw))
    print("resp content: ", act_resp.content)
    print("resp: ", act_resp)
    print("resp status code: ", act_resp.status_code)
    json_resp = json.loads(act_resp.content.decode('utf-8'))
    print('json resp: ', json_resp)
    #act_root = json_resp["actions"]
    #print("act root: ", act_root)

    print("id: ", json_resp['id'])
    print("name: ", json_resp['name'])
    print("time range: ", json_resp['timeRange'])
    print("hr ids: ", json_resp['healthRuleIds'])
    print("affects: ", json_resp['affects'])
    #id = element['id']
    #name = element['name']
    #time_range = element['timeRange']
    #hr_ids = element['healthRuleIds']
    #affects = element['affects']

    #print('id: ', id)
    #print('name: ', name)
    #print('time range: ', time_range)
    #print('hr_ids: ', hr_ids)
    #print('affects: ', affects)
    #act_supp_root_counter += 1

def create_new_action_supp():
    print()

# DELETE /controller/api/accounts/account_id/applications/application_id/actionsuppressions/actionsuppression_id
def delete_specific_action_supp_by_id(acc_id, app_id, supp_id):
    conn_str = mc.url + '/controller/api/accounts/{}/applications/{}/actionsuppressions/{}'.format(acc_id, app_id,
                                                                                                   supp_id)
    r = requests.delete(conn_str, auth=(mc.user_at_account_name, mc.pw))
    print("resp content: ", r.content)
    print("resp: ", r)
    print("resp status code: ", r.status_code)
    if r.status_code == 204:
        print("action suppression sucessfully deleted.  Hard refresh action supp screen to see it gone... ")

#####################################################################
#SUB-MENU 4 - Configuration API
#####################################################################

#curl -X POST --user user1@customer1:secret
# http://demo.appdynamics.com/controller/rest/users?user-name=user2\&user-display-name=User%20Two\&user-password=welcome\&user-email=user2\@example.com
def create_user(user_name, user_display_name, user_roles, user_password, user_email):
    if user_roles == '':
        print('Nothing entered for User Roles...')
        req1 = requests.post(
            mc.url + '/controller/rest/users?user-name={}&user-display-name={}&user-password={}&user-email={}'.format(
                user_name, user_display_name, user_password, user_email),
            auth=(mc.user_at_account_name, mc.pw))
        print(req1.status_code)
        print(req1.content)
    elif user_roles != '':
        req2 = requests.post(
            mc.url + '/controller/rest/users?user-name={}&user-display-name={}&user-password={}&user-email={}&user-roles={}'.format(
                user_name, user_display_name, user_password, user_email, user_roles),
            auth=(mc.user_at_account_name, mc.pw))
        print(req2.status_code)
        print(req2.content)

    #r = requests.post(mc.url + '/controller/rest/users?user-name={}&user-display-name={}&user-password={}&user-email={}&user-id={}'.format(user_name, user_display_name, user_password, user_email, user_id),
    #                  auth=(mc.user_at_account_name, mc.pw))
    #print(r.content)
    #print(r.status_code)

def update_user(user_name, user_display_name, user_id, user_roles, user_password, user_email):
    print()

#POST /controller/rest/applications/application_id/business-transactions
#need to get b'<>' out of the outputted xml file
#s:  b'<business-transactions><business-transaction><id>1576</id></business-transaction></business-transactions>'
def include_exclude_transaction_for_monitoring(app_name, bt_list, bool_exclude):
    business_transactions_root = ET.Element('business-transactions')
    s = ET.tostring(business_transactions_root)

    print('s type: ', type(s))
    counter=0
    for item in bt_list:
        #print('counter: ', counter)
        business_transaction_sub_element = ET.SubElement(business_transactions_root, 'business-transaction')
        id_sub_element = ET.SubElement(business_transaction_sub_element, 'id')
        id_sub_element.text = item

    #s = ET.tostring(business_transactions_root)
    f = ET.fromstring(s)

    print('s ET.tostr: ', s)
    #conv = str(s.decode(encoding='UTF-8'))
    #print('conv str: ', conv)
    string_conversion = s.decode(encoding='UTF-8')
    print(string_conversion)
    a=0
    for child in business_transactions_root:
        element = business_transactions_root[a].text
        print('element: ', element)
        #appName = business_transactions_root[a][1].text
        bt_id = business_transactions_root[a][0].text
        #print('el 1:', appName)
        print('sub element:', bt_id)
        a+=1

#below, try writing to an actual file that is created. then load file. test this.  getting malformed xml currently
    to_file = "bt_list.xml"
    print('XML file being created...')
    with open(to_file, "w") as code:
        #code.write(conv)
        code.write(string_conversion)
    code.close()

    session = requests.Session()
    session.auth = (mc.user_at_account_name, mc.pw)
    session.headers['Content-Type'] = 'application/xml'
    login = session.get(mc.url + '/controller/auth?action=login')

    if bool_exclude == 'true':
        print('exclude == ', bool_exclude)
        with open(to_file, 'rb') as f:
            r = session.post(mc.url + '/controller/rest/applications/{}/business-transactions?exclude=true'.format(app_name), files={'file=@' + to_file: f})
        print(r.content)
    elif bool_exclude == 'false':
        print('exclude == ', bool_exclude)
        with open(to_file, 'rb') as f:
            r = requests.post(mc.url + '/controller/rest/applications/{}/business-transactions?exclude=false'.format(app_name), auth=(mc.user_at_account_name, mc.pw),
                            files={'file=@' + to_file: f})
        print(r.content)

#GET /controller/rest/configuration
def retrieve_all_controller_settings():
    node_resp = requests.get(
        mc.url + '/controller/rest/configuration?output=JSON',
        auth=(mc.user_at_account_name, mc.pw))
    jsonResponseHolder = json.loads(node_resp.content.decode('utf-8'))
    #print(jsonResponseHolder)
    counter = 0
    for item in jsonResponseHolder:
        element = jsonResponseHolder[counter]
        #print(element)
        print("name: ", element["name"])
        print("value: ", element["value"])
        print("updateable: ", element["updateable"])
        print("description: ", element["description"])
        print()
        counter += 1



#BROKEN, won't even work with hard-coded url
#Retrieve a Controller Setting by Name
#GET  /controller/rest/configuration?name=controller_setting_name
def retrieve_controller_setting_by_name(setting_name_in):
    node_resp = requests.get(
        mc.url + '/controller/rest/configuration?name=metrics.min.retention.period?output=JSON',
        auth=(mc.user_at_account_name, mc.pw))
    #node_resp = requests.get(mc.url + '/controller/rest/configuration?name={}?output=JSON'.format(setting_name), auth=(mc.user_at_account_name, mc.pw))
    print(node_resp)
    print(node_resp.content)
    jsonResponseHolder = json.loads(node_resp.content.decode('utf-8'))
    #print(jsonResponseHolder)
    counter = 0
    for item in jsonResponseHolder:
        element = jsonResponseHolder[counter]
        #print(element)
        print("name: ", element["name"])
        print("value: ", element["value"])
        print("updateable: ", element["updateable"])
        print("description: ", element["description"])
        print()
        counter += 1

# POST /controller/rest/mark-nodes-historical?application-component-node-ids=value
# http://demo.appdynamics.com/controller/rest/mark-nodes-historical?application-component-node-ids=44,45
def mark_node_as_historical(node_id):
    r = requests.post(mc.url + '/controller/rest/mark-nodes-historical?application-component-node-ids={}'.format(node_id),
                    auth=(mc.user_at_account_name, mc.pw))
    print(r.status_code)

#GET /controller/actions/application_id
def export_actions(app_name):
    r = str(
        requests.get(mc.url + '/controller/actions/{}'.format(app_name), auth=(mc.user_at_account_name, mc.pw)).text)
    print(r)
    json_filename = '{}_actions.json'.format(app_name)
    print('JSON file being created in home dir you ran this script from...')
    with open(json_filename, "w") as code:
        code.write(r)
    code.close()
    print('done creating file - {} in script home directory.'.format(json_filename))

#POST /controller/actions/application_id
def import_actions(app_name, json_filename):
    with open(json_filename, 'rb') as f:
        r = requests.post(mc.url + '/controller/actions/{}'.format(app_name), auth=(mc.user_at_account_name, mc.pw), files={'file=@' + json_filename: f})
    f.close()
    print(r.status_code)
    print(r.content)

#GET /controller/actiontemplate/email
#This API exports all the email action templates in the current account in JSON format.
def export_email_action_templates_from_account():
    r = str(
        requests.get(mc.url + '/controller/actiontemplate/email', auth=(mc.user_at_account_name, mc.pw)).text)
    print(r)
    json_filename = 'email_action_template.json'
    print('JSON file being created in home dir you ran this script from...')
    with open(json_filename, "w") as code:
        code.write(r)
    code.close()
    print('done creating file - {} in script home directory.'.format(json_filename))

#POST /controller/actiontemplate/email
def import_email_action_templates(json_filename):
    with open(json_filename, 'rb') as f:
        r = requests.post(mc.url + '/controller/actiontemplate/email', auth=(mc.user_at_account_name, mc.pw), files={'file=@' + json_filename: f})
    f.close()
    print(r.status_code)
    print(r.content)

#GET /controller/actiontemplate/httprequest/
def export_http_req_action_templates_from_account():
    r = str(
        requests.get(mc.url + '/controller/actiontemplate/httprequest', auth=(mc.user_at_account_name, mc.pw)).text)
    print(r)
    json_filename = 'http_request_action_template.json'
    print('JSON file being created in home dir you ran this script from...')
    with open(json_filename, "w") as code:
        code.write(r)
    code.close()
    print('done creating file - {} in script home directory.'.format(json_filename))

#POST? /controller/actiontemplate/httprequest
def import_http_req_action_templates_into_account(json_filename):
    with open(json_filename, 'rb') as f:
        r = requests.post(mc.url + '/controller/actiontemplate/httprequest', auth=(mc.user_at_account_name, mc.pw), files={'file=@' + json_filename: f})
    f.close()
    print(r.status_code)
    print(r.content)

#GET /controller/CustomDashboardImportExportServlet?dashboardId=dashboard_id
def export_custom_dashboards_and_templates(dashboard_id):
    r = str(
        requests.get(mc.url + '/controller/CustomDashboardImportExportServlet?dashboardId={}'.format(dashboard_id), auth=(mc.user_at_account_name, mc.pw)).text)
    print(r)
    json_filename = 'id_{}_dashboard.json'.format(dashboard_id)
    print('JSON file being created in home dir you ran this script from...')
    with open(json_filename, "w") as code:
        code.write(r)
    code.close()
    print('done creating file - {} in script home directory.'.format(json_filename))

#POST /controller/CustomDashboardImportExportServlet
def import_custom_dashboards_and_templates(json_filename):
    with open(json_filename, 'rb') as f:
        r = requests.post(mc.url + '/controller/CustomDashboardImportExportServlet', auth=(mc.user_at_account_name, mc.pw), files={'file=@' + json_filename: f})
    f.close()
    print(r.status_code)
    print(r.content)
    print()

#test below method next
#NEXT: write code in loop where this method is called
#filename field added so users can name it themselves. all i do is append .xml or .json to it so it is valid file
#GET /controller/healthrules/application_id?name=health_rule_name
def export_health_rules_from_app(app_name, health_rule_name):
    if health_rule_name == '':
        r = str(requests.get(mc.url + '/controller/healthrules/{}'.format(app_name),
                            auth=(mc.user_at_account_name, mc.pw)).text)
        xml_filename = '{}_healthrules.xml'.format(app_name)
        print(r)
    elif health_rule_name != '':
        r = str(requests.get(mc.url + '/controller/healthrules/{}?name={}'.format(app_name, health_rule_name),
                             auth=(mc.user_at_account_name, mc.pw)).text)
        xml_filename = '{}_{}_healthrules.xml'.format(app_name, health_rule_name)
        print(r)
    print('XML file being created in home dir you ran this script from...')
    with open(xml_filename, "w") as code:
        code.write(r)
    code.close()
    print('done creating file - {} in script home directory.'.format(xml_filename))

#POST /controller/healthrules/application_id?overwrite=true_or_false
def import_health_rules(app_name, xml_filename, bool_overwrite):
    with open(xml_filename, 'rb') as f:
        r = requests.post(mc.url + '/controller/healthrules/{}?overwrite={}'.format(app_name, bool_overwrite), auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
    print(r.status_code)
    print(r.content)




#export All:
#curl --user user1@customer1:secret http://demo.appdynamics.com/controller/transactiondetection/38/auto
#
#curl --user user1@customer1:secret http://demo.appdynamics.com/controller/transactiondetection/ECommerce/Inventory-Services/custom
#
#curl --user uesr1@customer1:secret http://demo.appdynamics.com/controller/transactiondetection/38/exclude
#
#auto: Automatic detection rules
#custom: Custom detection rules in the configuration
#exclude: Custom exclude rules for transaction detection
#
##GET /controller/transactiondetection/application_id/[tier_name/]rule_type
def export_transaction_detection_rules_for_all_entry_point_types(app_name, tier_name, rule_type):
    if tier_name != '':
        r = str(requests.get(mc.url + '/controller/transactiondetection/{}/{}/{}'.format(app_name, tier_name, rule_type), auth=(mc.user_at_account_name, mc.pw)).text)
    elif tier_name == '':
        r = str(
            requests.get(mc.url + '/controller/transactiondetection/{}/{}'.format(app_name, rule_type),
                         auth=(mc.user_at_account_name, mc.pw)).text)

    print(r)

    xml_filename = '{}_{}_bt_rules_all_entry_point_types.xml'.format(app_name, rule_type)
    print('XML file being created in home dir you ran this script from...')
    with open(xml_filename, "w") as code:
        code.write(r)
    print('done creating file - {} in script home directory.'.format(xml_filename))

#POST /controller/transactiondetection/application_id/[tier_name/]rule_type
def import_transaction_detection_rules_for_all_entry_point_types(app_name, tier_name, rule_type, overwrite, xml_filename):
    with open(xml_filename, 'rb') as f:
        r = requests.post(mc.url + '/controller/transactiondetection/{}/{}/{}'.format(app_name, tier_name, rule_type), auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
    print(r.status_code)
    print(r.content)


#http://demo.appdynamics.com/controller/transactiondetection/38/auto/servlet
#GET /controller/transactiondetection/application_id/[tier_name/]rule_type/entry_point_type[/rule_name]
def export_transaction_detection_rule_for_single_entry_point_type(app_name, tier_name, rule_type, entry_point_type, rule_name):
    if tier_name == '' and rule_name != '':
        r = str(requests.get(
            mc.url + '/controller/transactiondetection/{}/{}/{}/{}'.format(app_name, rule_type, entry_point_type, rule_name),
            auth=(mc.user_at_account_name, mc.pw)).text)
        print(r)
    elif tier_name != '' and rule_name == '':
        r = str(requests.get(
            mc.url + '/controller/transactiondetection/{}/{}/{}/{}'.format(app_name, tier_name, rule_type, entry_point_type),
            auth=(mc.user_at_account_name, mc.pw)).text)
        print(r)
    elif tier_name == '' and rule_name == '':
        r = str(requests.get(
            mc.url + '/controller/transactiondetection/{}/{}/{}'.format(app_name, rule_type,
                                                                        entry_point_type),
            auth=(mc.user_at_account_name, mc.pw)).text)
        print(r)
    elif tier_name != '' and rule_name != '':
        r = str(requests.get(
            mc.url + '/controller/transactiondetection/{}/{}/{}/{}/{}'.format(app_name, tier_name, rule_type,
                                                                        entry_point_type, rule_name),
            auth=(mc.user_at_account_name, mc.pw)).text)
        print(r)

    xml_filename = '{}_{}_bt_rule_single_entry_point_type.xml'.format(rule_type, entry_point_type)
    print('XML file being created in home dir you ran this script from...')
    with open(xml_filename, "w") as code:
        code.write(r)
    print('done creating file - {} in script home directory.'.format(xml_filename))


#***TEST THIS
#POST /controller/transactiondetection/application_id/[tier_name/]rule_type/entry_point_type[/rule_name]
def import_transaction_detection_rule_for_single_entry_point_type(app_name, tier_name, rule_type, entry_point_type, rule_name, bool_overwrite, xml_filename):
    if tier_name == '' and rule_name != '':
        if bool_overwrite == 'y':
            with open(xml_filename, 'rb') as f:
                r = requests.post(
                    mc.url + '/controller/transactiondetection/{}/{}/{}/{}?overwrite=true'.format(app_name, rule_type, entry_point_type, rule_name),
                    auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
            f.close()
            print(r)
            print(r.status_code)
            print(r.content)
        elif bool_overwrite == 'n':
            with open(xml_filename, 'rb') as f:
                r = requests.post(
                    mc.url + '/controller/transactiondetection/{}/{}/{}/{}'.format(app_name, rule_type, entry_point_type, rule_name),
                    auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
            f.close()
            print(r)
            print(r.status_code)
            print(r.content)
    elif tier_name != '' and rule_name == '':
        if bool_overwrite == 'y':
            with open(xml_filename, 'rb') as f:
                r = requests.post(
                    mc.url + '/controller/transactiondetection/{}/{}/{}/{}?overwrite=true'.format(app_name, tier_name, rule_type, entry_point_type),
                    auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
            f.close()
            print(r)
            print(r.status_code)
            print(r.content)
        elif bool_overwrite == 'n':
            with open(xml_filename, 'rb') as f:
                r = requests.post(
                    mc.url + '/controller/transactiondetection/{}/{}/{}/{}'.format(app_name, tier_name, rule_type, entry_point_type),
                    auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
            f.close()
            print(r)

    elif tier_name == '' and rule_name == '':
        if bool_overwrite == 'y':
            with open(xml_filename, 'rb') as f:
                r = requests.post(
                    mc.url + '/controller/transactiondetection/{}/{}/{}?overwrite=true'.format(app_name, rule_type, entry_point_type),
                    auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
            f.close()
            print(r)
        elif bool_overwrite == 'n':
            with open(xml_filename, 'rb') as f:
                r = requests.post(
                    mc.url + '/controller/transactiondetection/{}/{}/{}'.format(app_name, rule_type, entry_point_type),
                    auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
            f.close()
            print(r)
    elif tier_name != '' and rule_name != '':
        if bool_overwrite == 'y':
            with open(xml_filename, 'rb') as f:
                r = requests.post(
                    mc.url + '/controller/transactiondetection/{}/{}/{}/{}/{}?overwrite=true'.format(app_name, tier_name, rule_type, entry_point_type, rule_name),
                    auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
            print(r)
        elif bool_overwrite == 'n':
            with open(xml_filename, 'rb') as f:
                r = requests.post(
                    mc.url + '/controller/transactiondetection/{}/{}/{}/{}/{}'.format(app_name, tier_name, rule_type, entry_point_type, rule_name),
                    auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
            print(r)


#GET /controller/policies/application_id
def export_policies(app_name):
    r = str(requests.get(mc.url + '/controller/policies/{}'.format(app_name), auth=(mc.user_at_account_name, mc.pw)).text)
    print(r)
    json_filename = '{}_policies.json'.format(app_name)
    print('JSON file being created in home dir you ran this script from...')
    with open(json_filename, "w") as code:
        code.write(r)
    code.close()
    print('done creating file - {} in script home directory.'.format(json_filename))


#curl  -X POST --user user1@customer1:secret http://demo.appdynamics.com/controller/policies/38 -F file=@ExportPolicies.json
#{"success":true,"errors":[],"warnings":[]}
#POST /controller/policies/application_id
def import_policies(app_name, json_filename):
    with open(json_filename, 'rb') as f:
        r = requests.post(mc.url + '/controller/policies/{}'.format(app_name), auth=(mc.user_at_account_name, mc.pw), files={'file=@' + json_filename: f})
    f.close()
    print(r.status_code)
    print(r.content)

#NOTE: did not code in parameter for filename as per api docs - ?filename=x
#http://demo.appdynamics.com/controller/analyticsdynamicservice/10
#GET /controller/analyticsdynamicservice/application_id
def export_app_analytics_dynamic_service_configuration(app_name):
    r = str(
        requests.get(mc.url + '/controller/analyticsdynamicservice/{}'.format(app_name), auth=(mc.user_at_account_name, mc.pw)).text)
    print(r)

    xml_filename = '{}_analytics_dynamic_service_config.xml'.format(app_name)
    print('XML file being created in home dir you ran this script from...')
    with open(xml_filename, "w") as code:
        code.write(r)
    code.close()
    print('done creating file - {} in script home directory.'.format(xml_filename))

#tested ok w/no analytics dynamic config. create dynamic config & test more
#http://demo.appdynamics.com/controller/analyticsdynamicservice/10 -F file=@dynamicservice.xml
#POST /controller/analyticsdynamicservice/application_id
def import_app_analytics_dynamic_service_configuration(app_name, xml_filename):
    with open(xml_filename, 'rb') as f:
        r = requests.post(mc.url + '/controller/analyticsdynamicservice/{}'.format(app_name), auth=(mc.user_at_account_name, mc.pw), files={'file=@' + xml_filename: f})
    f.close()

    print(r.status_code)
    print(r.content)

#######################################################################
#ANALYTICS API
#######################################################################
#POST http://<events_service_endpoint>:9080/events/schema/{schemaName}

def create_event_schema(schema_name, es_url, events_api_key, events_api_account_name, json_filename):
    headers = {'X-Events-API-Key': events_api_key, 'X-Events-API-AccountName': events_api_account_name,
               'Accept': 'application/vnd.appd.events+json;v=2','Content-type': 'application/vnd.appd.events+json;v=2'}
               #,'Accept': 'application/vnd.appd.events+json;v=2'}

    full_url = es_url + "/events/schema/{}".format(schema_name)
    #data = [{'Application': appName, 'Tier': tierName, 'Node': nodeName,
    #         'Business_Transaction': businessTransactionName, 'Error': error,
    #         'Error_Detail': errorDetail,
    #         'requestGUID': requestGUID, 'Response_Time_ms': timeTakenInMilliSecs,
    #         'userExperience': userExperience, 'httpParams': httpParams}]


    print("full url: ", full_url)
    # data = [schema_dict]
    #print("schema dict wrapped in square braces: ", data)
    #print("data type: ", type(data))
    #data_accepted_json = {"schema": [{"Application": "string", "Tier": "string", "Node": "string"}]}

    ###NEED TO FIND WAY TO TAKE INPUT DICT AND PASS IT INTO THE BELOW LINE:
    #data_accepted_json = {"schema": [{"Application": "string", "Tier": "string", "Node": "string"}]}
    #print("data_accepted_json TYPE: ", type(data_accepted_json))
    #print("json file type: ", type(json_filename))

    #json_resp = json.loads(json_filename)

    #with open(json_filename, 'rb') as f:
    #    r = requests.post(full_url, headers=headers, files={'file=@' + json_filename: f})

    with open(json_filename) as json_data:
        d = json.load(json_data)
        print(d)
        r = requests.post(full_url, headers=headers, json=d)

    json_data.close()
    print(r.status_code)
    print(r.content)

    #r = requests.post(full_url, headers=headers, json=data_accepted_json)
    print("req status: ", r.status_code, r.content, r)
    if r.status_code == 201:
        print("Event Schema Successfully Published...")
    elif r.status_code == 406:
        print("Event Schema has error in schema payload...")
    elif r.status_code == 401:
        print("401 error... verify all of your keys are correct...")
    elif r.status_code == 407:
        print("407 error... schema already exists with this name...")

#GET http://<events_service_endpoint>:9080/events/schema/{schemaName}
def retrieve_event_schema(schema_name, es_url, events_api_key, events_api_account_name):
    headers = {'X-Events-API-Key': events_api_key, 'X-Events-API-AccountName': events_api_account_name,
               'Accept': 'application/vnd.appd.events+json;v=2'}
    full_url = es_url + "/events/schema/{}".format(schema_name)

    r = requests.get(full_url, headers=headers)
    print("req status code: ", r.status_code)
    print("req content: ", r.content)

#PATCH http://analytics.api.example.com/events/schema/{schemaName}
def update_event_schema(schema_name, es_url, events_api_key, events_api_account_name, json_filename):
    headers = {'X-Events-API-Key': events_api_key, 'X-Events-API-AccountName': events_api_account_name,
               'Accept': 'application/vnd.appd.events+json;v=2',
               'Content-type': 'application/vnd.appd.events+json;v=2'}
    full_url = es_url + "/events/schema/{}".format(schema_name)
    with open(json_filename) as json_data:
        d = json.load(json_data)
        print(d)
        r = requests.patch(full_url, headers=headers, json=d)

    print("req status code: ", r.status_code)
    print("req content: ", r.content)
    if r.status_code == 415:
        print("No event type could be found for this account.")

#DELETE http://<events_service_endpoint>:9080/events/schema/{schemaName}
def delete_event_schema(schema_name, es_url, events_api_key, events_api_account_name):
    headers = {'X-Events-API-Key': events_api_key, 'X-Events-API-AccountName': events_api_account_name}
    full_url = es_url + "/events/schema/{}".format(schema_name)

    r = requests.delete(full_url, headers=headers)
    print("req status: ", r.status_code, r.content, r)
    if r.status_code == 404:
        print("schema name does not exist...")

#POST http://<events_service_endpoint>:9080/events/query
def query_events_json(es_url, events_api_key, events_api_account_name, json_filename):
    headers = {'X-Events-API-Key': events_api_key, 'X-Events-API-AccountName': events_api_account_name,
               'Content-type': 'application/vnd.appd.events+json;v=2'}
    full_url = es_url + "/events/query"
    with open(json_filename) as json_data:
        d = json.load(json_data)
        print(d)
        r = requests.post(full_url, headers=headers, json=d)

    json_data.close()
    print(r.status_code)
    print(r.content)

def publish_all_bt_data_to_es(schema_name, es_url, events_api_key, events_api_account_name):
    headers = {'X-Events-API-Key': events_api_key, 'X-Events-API-AccountName': events_api_account_name,
               'Content-type': 'application/vnd.appd.events+json;v=2'}
    full_url = es_url + "/events/publish/{}".format(schema_name)
    resp = str(requests.get(
        mc.url + '/controller/rest/applications/df_serviceconnect/request-snapshots?time-range-type=BEFORE_NOW&'
                 'duration-in-mins=10080',
        auth=(un, pw)).text)
    print(resp)
    root = ET.fromstring(resp)
    appName = 'df_serviceconnect'
    a = 0
    for child in root:
        #applicationId = int(root[a][4].text)
        businessTransactionId = int(root[a][3].text)
        error = root[a][21].text
        errorDetail = root[a][30].text
        applicationComponentNodeId = int(root[a][6].text)
        requestGUID = root[a][2].text
        timeTakenInMilliSecs = int(root[a][16].text)
        timestamp = root[a][8].text
        userExperience = root[a][15].text
        httpParams = root[a][31].text

        tierName = getTierNameFromNodeId(applicationComponentNodeId)
        #print("Tier name: ", tierName)

        nodeName = getNodeNameFromId(applicationComponentNodeId)
        #print("Node name: ", nodeName)

        businessTransactionName = getBtNameFromId(businessTransactionId)
        #print("BT name: ", businessTransactionName)

        data = [{'Application':appName, 'Tier':tierName, 'Node':nodeName,
                 'Business_Transaction':businessTransactionName, 'Error':error,
                'Error_Detail':errorDetail,
                'requestGUID':requestGUID, 'Response_Time_ms':timeTakenInMilliSecs,
                'userExperience':userExperience, 'httpParams':httpParams}]

        print('applicationName:', appName)
        print('businessTransactionId:', businessTransactionId)
        print('businessTransactionName:', businessTransactionName)
        print('error:', error)
        print('errorDetail:', errorDetail)
        print('applicationComponentNodeId:', applicationComponentNodeId)
        print('requestGUID:', requestGUID)
        print('timeTakenInMilliSecs:', timeTakenInMilliSecs)
        #print('timeStamp:', timestamp)
        print('userExperience:', userExperience)
        print('httpParams:', httpParams)
        print()

        r = requests.post(es.es_url, headers=headers, json=data)
        print('hit POST... status code:')
        print(r.status_code)
        print(r.headers)
        a = a + 1

def publish_all_event_data_to_es(schema_name, es_url, events_api_key, events_api_account_name):
    headers = {'X-Events-API-Key': events_api_key, 'X-Events-API-AccountName': events_api_account_name,
               'Content-type': 'application/vnd.appd.events+json;v=2'}
    full_url = es_url + "/events/publish/{}".format(schema_name)
    resp = str(requests.get(
        mc.url + '/controller/rest/applications/df_serviceconnect/request-snapshots?time-range-type=BEFORE_NOW&'
                 'duration-in-mins=10080',
        auth=(un, pw)).text)
    print(resp)
    root = ET.fromstring(resp)
    appName = 'df_serviceconnect'
    a = 0
    for child in root:
        #applicationId = int(root[a][4].text)
        businessTransactionId = int(root[a][3].text)
        error = root[a][21].text
        errorDetail = root[a][30].text
        applicationComponentNodeId = int(root[a][6].text)
        requestGUID = root[a][2].text
        timeTakenInMilliSecs = int(root[a][16].text)
        timestamp = root[a][8].text
        userExperience = root[a][15].text
        httpParams = root[a][31].text

        tierName = getTierNameFromNodeId(applicationComponentNodeId)
        #print("Tier name: ", tierName)

        nodeName = getNodeNameFromId(applicationComponentNodeId)
        #print("Node name: ", nodeName)

        businessTransactionName = getBtNameFromId(businessTransactionId)
        #print("BT name: ", businessTransactionName)

        data = [{'Application':appName, 'Tier':tierName, 'Node':nodeName,
                 'Business_Transaction':businessTransactionName, 'Error':error,
                'Error_Detail':errorDetail,
                'requestGUID':requestGUID, 'Response_Time_ms':timeTakenInMilliSecs,
                'userExperience':userExperience, 'httpParams':httpParams}]

        print('applicationName:', appName)
        print('businessTransactionId:', businessTransactionId)
        print('businessTransactionName:', businessTransactionName)
        print('error:', error)
        print('errorDetail:', errorDetail)
        print('applicationComponentNodeId:', applicationComponentNodeId)
        print('requestGUID:', requestGUID)
        print('timeTakenInMilliSecs:', timeTakenInMilliSecs)
        #print('timeStamp:', timestamp)
        print('userExperience:', userExperience)
        print('httpParams:', httpParams)
        print()

        r = requests.post(es.es_url, headers=headers, json=data)
        print('hit POST... status code:')
        print(r.status_code)
        print(r.headers)

        a = a + 1

def retrieve_event_data_for_script(app_name, time_in_min, event_types, severities):
    a_resp = requests.get(mc.url + '/controller/rest/applications/{}/events?time-range-type=BEFORE_NOW&duration-in-mins={}&event-types={}&severities={}&output=JSON'.format(app_name, time_in_min, event_types, severities),
                          auth=(mc.user_at_account_name, mc.pw))
    #print(a_resp)
    #print(a_resp.content)
    json_resp=json.loads(a_resp.content.decode('utf-8'))
    counter = 0
    for item in json_resp:
        element = json_resp[counter]
        #print('element: ', element)

        type = element['type']
        print('type: ', type)

        sever = element['severity']
        print('severity: ', sever)

        summary = element['summary']
        print('summary: ', summary)


        affected_entities = element['affectedEntities']
        print(affected_entities)

        entity_counter=0
        for item in affected_entities:
            print('\tentity name:', element['affectedEntities'][entity_counter]['name'])
            print('\tentity ID: ', element['affectedEntities'][entity_counter]['entityId'])
            print('\tentity type: ', element['affectedEntities'][entity_counter]['entityType'])
            entity_counter+=1
            print()
        print()
        print()
        counter += 1

def getBtNameFromId(bt_id):
    getBts = str(requests.get(mc.host + '/controller/rest/applications/df_serviceconnect/business-transactions',
                              auth=(un, pw)).text)
    btRoot = ET.fromstring(getBts)
    z = 0
    for child in btRoot:
        id = int(btRoot[z][0].text)
        # print("id:", id)
        name = btRoot[z][1].text
        # print("name:", name)

        if bt_id == id:
            return name
        z += 1

def getNodeNameFromId(node_id):
    getNodes = str(requests.get(mc.url + '/controller/rest/applications/df_serviceconnect/nodes',
                                auth=(un, pw)).text)
    nodeRoot = ET.fromstring(getNodes)
    y = 0
    for child in nodeRoot:
        print('node_id passed into func:', node_id)
        nid = int(nodeRoot[y][0].text)
        print("Nodeid:", nid)
        nname = nodeRoot[y][1].text
        print("Nodename:", nname)

        if nid == node_id:
            return nname
        y += 1

def getTierNameFromNodeId(node_id, app_name):
    getNodes = str(requests.get(mc.url + '/controller/rest/applications/df_serviceconnect/nodes',
                                auth=(un, pw)).text)
    nodeRoot = ET.fromstring(getNodes)
    x = 0
    for child in nodeRoot:
        id = int(nodeRoot[x][0].text)
        # print("nodeid:", id)
        nodeName = nodeRoot[x][1].text
        # print("nodename:", nodeName)
        tier_name = nodeRoot[x][4].text

        if node_id == id:
            return tier_name
        x += 1

#####################################################################
# SUB-MENU 4 - Configuration API -
#NOTE: ONLY WORKS WITH CONTROLLER 4.4 OR HIGHER
#####################################################################

#work in progress; add auth to req call
#POST /controller/api/rbac/v1/users
def rbac_create_user(name, security_provider_type, display_name, pw):
    req = requests.post(
        mc.url + '/controller/api/rbac/v1/users')
    print(req.status_code)
    print(req.content)

#GET /controller/api/rbac/v1/users
def get_all_users():
    conn_str = mc.url + '/controller/api/rbac/v1/users'
    print("conn str: " + conn_str)
    resp = requests.get(
        conn_str,
        auth=(mc.user_at_account_name, mc.pw))
    print(resp)
    print(resp.content)
    json_resp = json.loads(resp.content.decode('utf-8'))
    counter = 0
    for item in json_resp:
        element = json_resp[counter]
        print("el: ", element)

def delete_dynamic_nodes(source_app, source_tier, time_in_min):
    #initialize node_dict with node_name/node_id for all nodes in the selected tier
    node_dictionary = get_all_node_info_for_tier(source_app, source_tier)

    #create dict for storing node_name/node_id for all nodes that have
    no_calls_node_dict = {}

    for key, value in node_dictionary.items():
        print('node_dict - value : key')
        print(value, key)
        snapshot_response_xml = str(requests.get(mc.url +
                                                 '/controller/rest/applications/{}/'
                                                 'metric-data?metric-path='
                                                 'Overall%20Application%20Performance%7C'
                                                 '{}%7CIndividual%20Nodes%7C'
                                                 '{}%7CCalls%20per%20Minute'
                                                 '&time-range-type=BEFORE_NOW&duration-in-mins={}'
                                                 .format(source_app, source_tier, key, time_in_min),
                                                 auth=(mc.user_at_account_name, mc.pw)).text)

        snapshot_root = ET.fromstring(snapshot_response_xml)
        a = 0
        for child in snapshot_root:
            transaction_name = snapshot_root[a][1].text
            metricname = snapshot_root[a][2].text
            print(transaction_name)
            print('metricname: ', metricname)
            if metricname == 'METRIC DATA NOT FOUND':
                print('METRIC DATA NOT FOUND, MARKING NODE AS HISTORICAL - ', value)
                print('node: ', value)
                print('tier: ', source_tier)
                print('app: ', source_app)
                #no_calls_node_dict[key] = value
                r = requests.post(
                    mc.url + '/controller/rest/mark-nodes-historical?application-component-node-ids={}'.format(
                        value),
                    auth=(mc.user_at_account_name, mc.pw))
                print('post req: ', r.content)
                print(r)
                print('key: ', key)
                print('value: ', value)
                print(r.status_code)
                print()
            else:
                print('METRIC DATA FOUND - ', metricname)
                print()
                print()
                print()
            a = a + 1

def enable_new_bt_config(app_name):
    acc_id = get_account_id()
    app_id = get_app_id_and_does_app_exist(app_name)
    if app_id[1]:
        print("app id = true, appID = ", app_id[0])
        app_id_str = str(app_id[0])
        #print(app_id_str)
        r = requests.post(mc.url + '/controller/api/accounts/{}/applications/{}/enablemdsconfig'.format(acc_id, app_id_str),
                          auth=(mc.user_at_account_name, mc.pw))
        if r.status_code == 200:
            print('NEW BT config successfully enabled...')

    else:
        print(app_name + " app not found")

def disable_new_bt_config(app_name):
    acc_id = get_account_id()
    app_id = get_app_id_and_does_app_exist(app_name)
    if app_id[1]:
        print("app Id found, appID =", app_id[0])
        #app_id_bool = app_id[1]
        app_id_str = str(app_id[0])
        #print(app_id_str)
        r = requests.post(mc.url + '/controller/api/accounts/{}/applications/{}/disablemdsconfig'.format(acc_id, app_id_str),
                          auth=(mc.user_at_account_name, mc.pw))
        if r.status_code == 200:
            print(r.status_code)
            print(r.content)
            print('NEW BT config successfully disabled...')
    else:
        print(app_name + " app not found")

mc = Controller()
es = AnalyticsEventsService()
bus_app_dict = load_all_apps()
#print('app dict: ', bus_app_dict)
#print(bus_app_dict[113])

#print('id: ', app_id2)
entry_point_type_list = ['binaryRemoting', 'servlet', 'strutsAction', 'springBean', 'ejb', 'pojo', 'jms',
                         'webService', 'aspDotNet', 'dotNetWebService', 'wcf', 'poco', 'dotNetJms', 'dotNetRemoting',
                         'phpWeb', 'phpMvc', 'phpDrupal', 'phpWordpress', 'phpCli', 'phpWebService', 'nodeJsWeb']
#mc.update() #how to update just one parameter from the constructor?  can you have more than 1 constructor in py?
#################################################################
# MENU LOOP
loop = True
while loop:  ## While loop which will keep going until loop = False
    print_menu()  ## Displays menu
    choice = input("Enter your choice [1-10]: ")
    if choice == "0":
        loop = False
    #sub-menu
    elif choice == "1":
        print("Sub-menu 1 has been selected - Application Model API")
        inner_loop = True
        while inner_loop:
            print_sub_menu_1()
            subm_choice = input("Enter your choice [0-9]: ")
            if subm_choice == "0":
                inner_loop = False
            elif subm_choice == "1":
                print("Sub-menu 1 has been selected - Configure Source Controller")
                input_source_controller()
            elif subm_choice == "2":
                print("Sub-menu 2 has been selected - Retrieve All Business Applications")
                list_all_apps(bus_app_dict)
            elif subm_choice == "3":
                print("Sub-menu 3 has been selected - Retrieve All Business Transactions in a Business Application")
                app_name = input("Enter app name: ")
                app_exists_bool = does_app_exist(bus_app_dict, app_name)
                if app_exists_bool == True:
                    list_all_transactions_from_app_json(app_name)
            elif subm_choice == "4":
                print("Sub-menu 4 has been selected - Retrieve All Tiers in a Business Application")
                app_name = input("Enter app name: ")
                app_exists_bool = does_app_exist(bus_app_dict, app_name)
                if app_exists_bool == True:
                    list_all_tiers(app_name)
            elif subm_choice == "5":
                print("Sub-menu 5 has been selected - Retrieve All Registered Backends in a Business Application With Their Properties")
                app_name = input("Enter app name: ")
                app_exists_bool = does_app_exist(bus_app_dict, app_name)
                if app_exists_bool == True:
                    list_all_backends_with_props_from_app(app_name)
            elif subm_choice == "6":
                print("Sub-menu 6 has been selected - Retrieve Node Information for All Nodes in a Business Application")
                app_name = input("Enter app name: ")
                app_exists_bool = does_app_exist(bus_app_dict, app_name)
                if app_exists_bool == True:
                    list_all_nodes_with_props_from_app(app_name)
            elif subm_choice == "7":
                print("Sub-menu 7 has been selected - Retrieve Node Information by Node Name")
                app_name = input("Enter app name: ")
                node_name = input("Enter node name: ")
                does_node_exist_bool = does_node_exist(bus_app_dict, app_name, node_name)
                if does_node_exist_bool == True:
                    get_node_info_by_node_name(app_name, node_name)
            elif subm_choice == "8":
                print("Sub-menu 8 has been selected - Retrieve Node Information for All Nodes in a Tier")
                app_name = input("Enter app name: ")
                tier_name = input("Enter tier name: ")
                does_tier_exist_bool = does_tier_exist(bus_app_dict, app_name, tier_name)
                if does_tier_exist_bool == True:
                    get_all_node_info_for_tier(app_name, tier_name)
            elif subm_choice == "9":
                print("Sub-menu 9 has been selected - Retrieve Tier Information by Tier Name")
                app_name = input("Enter app name: ")
                tier_name = input("Enter tier name: ")
                bool_tier_exists = does_tier_exist(bus_app_dict, app_name, tier_name)
                if bool_tier_exists == True:
                    get_tier_info_by_tier_name(app_name, tier_name)
    elif choice == "2":
        print("Sub-menu 2 has been selected - Metric and Snapshot API")
        inner_loop2 = True
        while inner_loop2:
            print_sub_menu_2()
            subm2_choice = input("Enter your choice [0-9]: ")
            if subm2_choice == "0":
                inner_loop2 = False
            elif subm2_choice == "1":
                print("Sub-menu 2 has been selected - Configure Source Controller")
                input_source_controller()
            elif subm2_choice == "2":
                print("Sub-menu 2 has been selected - Retrieve Metric Hierarchy")
                app_name = input("Enter app name: ")
                retrieve_metric_hierarchy(app_name)
            elif subm2_choice == "3":
                print("Sub-menu 3 has been selected - Retrieve Data")
                #http://localhost:8090/controller/rest/applications/t/metric-data?metric-path=Overall%20Application%20Performance%7CCalls%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15
                #def retrieve_metric_data(app_name, metric_path, time_in_minutes, bool_rollup)
                retrieve_metric_data('t', 'Overall%20Application%20Performance%7CCalls%20per%20Minute', '10000', 'false')
                #app_name = input("Enter app name: ")
            elif subm2_choice == "6":
                print("Sub-menu Option 6 - Configure Metric Retention by Account")
                acc_id = get_account_id()
                #i = input("Enter number of days you want to retain stale metrics: ")
                config_metric_reten_by_account(acc_id)

    elif choice == "3":
        print("Sub-menu 3 has been selected - Alert and Respond API")
        inner_loop3 = True
        while inner_loop3:
            print_sub_menu_3()
            subm3_choice = input("Enter your choice [0-9]: ")
            if subm3_choice == "0":
                inner_loop3 = False
            elif subm3_choice == "1":
                print("Sub-menu 1 has been selected - Configure Source Controller")
                input_source_controller()
            elif subm3_choice == "2":
                print("Sub-menu 2 has been selected - Retrieve All Health Rule Violations in a Business Application")
                retrieve_all_hr_violations_in_app('pss_alm', 60)
            elif subm3_choice == "3":
                print("Sub-menu 3 has been selected - Retrieve Event Data")
                #input_appname = input('enter app name: ')
                #input_timeinmin = input('enter time in min: ')
                #input_event_types = input('enter event types: ')
                #input_severities = input("enter severities: ")
                #retrieve_event_data(input_appname, input_timeinmin, input_event_types, input_severities)
                retrieve_event_data('pss_alm', '1000', 'APPLICATION_ERROR,DIAGNOSTIC_SESSION', 'INFO,WARN,ERROR')
            elif subm3_choice == "4":
                print("Sub-menu 4 has been selected - Create Events")
            elif subm3_choice == "5":
                print("Sub-menu 5 has been selected - Create a Custom Event")
            elif subm3_choice == "6":
                print("Sub-menu 6 has been selected - Create Custom URLS for Notifications")
            elif subm3_choice == "7":
                print("Sub-menu 7 has been selected - Create and Delete Action Suppressions")
            elif subm3_choice == "8":
                print("Sub-menu 8 has been selected - Retrieve All Existing Action Suppressions")
                acc_id = get_account_id()
                app_in = input("Enter app name: ")
                app_id_in = get_app_id_and_does_app_exist(app_in)
                if app_id_in[1]:
                    print('app found')
                    print("app id = true, appID = ", app_id_in[0])
                    app_id_str = str(app_id_in[0])
                retrieve_all_action_supps(acc_id, app_id_str)
            elif subm3_choice == "9":
                print("Sub-menu 9 has been selected - Retrieve a Specific Action Suppression by ID")
                acc_id = get_account_id()
                app_in = input("Enter app name: ")
                app_id_in = get_app_id_and_does_app_exist(app_in)
                supp_id_in = input("Enter action suppression ID: ")
                if app_id_in[1]:
                    print('app found')
                    print("app id = true, appID = ", app_id_in[0])
                    app_id_str = str(app_id_in[0])
                retrieve_specfic_action_supp_by_id(acc_id, app_id_str, supp_id_in)
                #retrieve_all_action_supps(acc_id, app_id_str)

            elif subm3_choice == "10":
                print("Sub-menu 10 has been selected - Create a New Action Suppression")
            elif subm3_choice == "11":
                print("Sub-menu 11 has been selected - Delete a Specific Action Suppression by ID")
                acc_id = get_account_id()
                app_in = input("Enter app name: ")
                app_id_in = get_app_id_and_does_app_exist(app_in)
                supp_id_in = input("Enter action suppression ID: ")
                if app_id_in[1]:
                    print('app found')
                    print("app id = true, appID = ", app_id_in[0])
                    app_id_str = str(app_id_in[0])
                    delete_specific_action_supp_by_id(acc_id, app_id_str, supp_id_in)

    elif choice == "4":
        print("Menu 4 has been selected - Configuration API")
        inner_loop4 = True
        while inner_loop4:
            print_sub_menu_4()
            subm4_choice = input("Enter your choice [0-9]: ")
            if subm4_choice == "0":
                inner_loop4 = False
            elif subm4_choice == "1":
                print("Sub-menu 1 has been selected - Configure Source Controller")
                input_source_controller()
            elif subm4_choice == "2":
                #user_name, user_display_name, user_roles, user_password, user_email
                print("Sub-menu 2 has been selected - Create AppD User")
                un = input("Enter user name:")
                dn = input("Enter display name:")
                pw = input("Enter password:")
                em = input("Enter email address:")
                print("Next field is optional - User Roles.  Just hit ENTER if you don't want to configure any roles")
                ur = input("Enter comma seperated list of user roles:")
                create_user(un, dn, ur, pw, em)
            elif subm4_choice == "3":
                print("Sub-menu 3 has been selected - Modify/Update AppD User")
            elif subm4_choice == "4":
                print("Sub-menu 4 has been selected - Include BT for Monitoring")
                bt_list = []
                #app_in = ('Enter app name:')
                bool_exclude = input("Enter 'true' for exclude rule or 'false' for include rule: ")
                inner_loop = True
                while inner_loop:  ## While loop which will keep going until loop = False
                    choice = input("Enter '1' to add BTs to the list, '0' when you are done: ")
                    if choice == "0":
                        inner_loop = False
                    else:
                        bt = input('Enter Business Transaction Name: ')
                        bt_list.append(bt)
                include_exclude_transaction_for_monitoring('newBDR4dot3', bt_list, bool_exclude)

            elif subm4_choice == "5":
                print("Sub-menu 5 has been selected - Exclude BT from Monitoring")
            elif subm4_choice == "6":
                print("Sub-menu 6 has been selected - Retrieve All Controller Settings")
                retrieve_all_controller_settings()
            elif subm4_choice == "7":
                print("Sub-menu 7 has been selected - Retrieve a Controller Setting by Name")
                setting_name_input = input("Enter controller setting name: ")
                retrieve_controller_setting_by_name(setting_name_input)
            elif subm4_choice == "8":
                print("Sub-menu 8 has been selected - Configure Global Controller Settings")
            elif subm4_choice == "9":
                print("Sub-menu 9 has been selected - Mark Nodes as Historical")
                node_id = input('Enter node ID: ')
                mark_node_as_historical(node_id)

    elif choice == "5":
        print("Menu 5 has been selected - Configuration Import and Export API")
        inner_loop5 = True
        while inner_loop5:
            print_sub_menu_5()
            subm5_choice = input("Enter your choice [0-9]: ")
            if subm5_choice == "0":
                inner_loop5 = False
            elif subm5_choice == "1":
                print("Sub-menu 1 has been selected - Configure Source Controller")
                input_source_controller()
            elif subm5_choice == "2":
                print("Sub-menu 2 has been selected - Export Actions")
                app_name = input('Export Actions, enter app name:')
                app_exists_bool = does_app_exist(bus_app_dict, app_name)
                if app_exists_bool == True:
                    export_actions(app_name)
            elif subm5_choice == "3":
                print("Sub-menu 3 has been selected - Import Actions")
                app_name = input('Import Actions, enter app name:')
                json_filename = input('Enter filename relative path to where script is ran from:')
                import_actions(app_name, json_filename)
            elif subm5_choice == "4":
                print("Sub-menu 4 has been selected - Export Email Action Templates from an account")
                export_email_action_templates_from_account()
            elif subm5_choice == "5":
                print("Sub-menu 5 has been selected - Import Email Action Templates to an account")
                json_filename = input('Enter filename relative path to where script is ran from (script home dir):')
                import_email_action_templates(json_filename)
            elif subm5_choice == "6":
                print("Sub-menu 6 has been selected - Export HTTP Request Action Templates from an Account")
                export_http_req_action_templates_from_account()
            elif subm5_choice == "7":
                print("Sub-menu 7 has been selected - Import HTTP Request Action Templates into an Account")
                json_filename = input('Enter filename relative path to where script is ran from (script home dir):')
                import_http_req_action_templates_into_account(json_filename)
            elif subm5_choice == "8":
                print("Sub-menu 8 has been selected - Export Custom Dashboards and Templates")
                dashboard_id = input("Enter dashboard ID: ")
                export_custom_dashboards_and_templates(dashboard_id)
            elif subm5_choice == "9":
                print("Sub-menu 9 has been selected - Import Custom Dashboards and Templates")
                json_filename = input('Enter filename relative path to where script is ran from (script home dir):')
                import_custom_dashboards_and_templates(json_filename)
            elif subm5_choice == "10":
                print("Sub-menu 10 has been selected - Export Health Rules")
                app_name = input('Export Health Rules, enter app name:')
                app_exists_bool = does_app_exist(bus_app_dict, app_name)
                if app_exists_bool == True:
                    export_health_rules_from_app(app_name, '')
            elif subm5_choice == "11":
                print("Sub-menu 11 has been selected - Import Health Rules")
                app_name = input('Import Health Rules, enter app name:')
                json_filename = input('Enter filename relative path to where script is ran from:')
                import_health_rules(app_name, json_filename, 'true')
            elif subm5_choice == "12":
                print("Sub-menu 12 has been selected - Export Transaction Detection Rules for ALL Entry Point Types")
                app_name = input('Enter app name:')
                tier_name = input('Enter tier name (OPTIONAL, just hit ENTER for NO tier):')
                rule_type = input("Enter rule type, options are: 'auto', 'custom', 'exclude'")
                export_transaction_detection_rules_for_all_entry_point_types(app_name, tier_name, rule_type)
            elif subm5_choice == "13":
                print("Sub-menu 13 has been selected - Import a Transaction Detection Rule for ALL Entry Point Types")
                app_name = input('Enter app name:')
                tier_name = input('Enter tier name:')
                rule_type = input("Enter rule type, options are: 'auto', 'custom', 'exclude'")
                overwrite = input('Enter overwrite t or f')
                xml_filename = input('Enter filename relative path to where script is ran from:')
                import_transaction_detection_rules_for_all_entry_point_types(app_name, tier_name, rule_type, overwrite, xml_filename)
            elif subm5_choice == "14":
                print("Sub-menu 14 has been selected - Export a Transaction Detection Rule for ONE Entry Point Type")
                app_name = input('Enter app name:')
                tier_name = input('Enter tier name (Optional, ENTER for NONE):')
                entry_point_type = input("Enter entry point type, (servlet, wcf, etc.), ENTER: ")
                rule_type = input("Enter rule type, options are: 'auto', 'custom', 'exclude': ")
                #print('ept: ', entry_point_type)
                rule_name = ''
                if rule_type == 'custom' or rule_type == 'exclude':
                    print("custom / exclude rule chosen...")
                    rule_name = input('Enter rule name:')
                elif rule_type == 'auto':
                    rule_name == ''
                if entry_point_type in entry_point_type_list:
                    print('Entry point type {} found...'.format(entry_point_type))
                    export_transaction_detection_rule_for_single_entry_point_type(app_name, tier_name, rule_type, entry_point_type, rule_name)
                else:
                    print('Entry point type {} not found.  Types are case sensitive, exiting to sub-menu...')
            elif subm5_choice == "15":
                print("Sub-menu 15 has been selected - Import a Transaction Detection Rule for ONE Entry Point Type")
                app_name = input('Enter app name:')
                tier_name = input('Enter tier name (Optional, ENTER for NONE):')
                entry_point_type = input("Enter entry point type, (servlet, wcf, etc.), ENTER: ")
                rule_type = input("Enter rule type, options are: 'auto', 'custom', 'exclude': ")
                overwrite = input("Enter 'y' to overwrite, 'n' NOT to overwrite: ")
                xml_filename = input('Enter filename relative path to where script is ran from:')
                # print('ept: ', entry_point_type)
                rule_name = ''
                if rule_type == 'custom' or rule_type == 'exclude':
                    print("custom / exclude rule chosen...")
                    rule_name = input('Enter rule name:')
                elif rule_type == 'auto':
                    rule_name == ''
                if entry_point_type in entry_point_type_list:
                    print('Entry point type {} found...'.format(entry_point_type))
                    import_transaction_detection_rule_for_single_entry_point_type(app_name, tier_name, rule_type,
                                                                                  entry_point_type, rule_name, overwrite, xml_filename)
                else:
                    print('Entry point type {} not found.  Types are case sensitive, exiting to sub-menu...')
            elif subm5_choice == "16":
                print("Sub-menu 16 has been selected - Export Policies")
                app_name = input('Export Policies, enter app name:')
                app_exists_bool = does_app_exist(bus_app_dict, app_name)
                if app_exists_bool == True:
                    export_policies(app_name)
            elif subm5_choice == "17":
                print("Sub-menu 17 has been selected - Import Policies")
                app_name = input('Import Policies, enter app name:')
                json_filename = input('Enter filename relative path to where script is ran from:')
                import_policies(app_name, json_filename)
            elif subm5_choice == "18":
                print("Sub-menu 18 has been selected - Export Application Analytics Dynamic Service Configuration")
                app_name = input("Enter app name: ")
                export_app_analytics_dynamic_service_configuration(app_name)
            elif subm5_choice == "19":
                print("Sub-menu 19 has been selected - Import Application Analytics Dynamic Service Configuration")
                app_name = input("Enter app name: ")
                xml_filename = input('Enter filename relative path to where script is ran from:')
                import_app_analytics_dynamic_service_configuration(app_name, xml_filename)
    elif choice == "6":
        print("Menu 6 has been selected - Analytics Events API")
        inner_loop6 = True
        while inner_loop6:
            print_sub_menu_6()
            subm6_choice = input("Enter your choice [0-9]: ")
            if subm6_choice == "0":
                inner_loop6 = False
            elif subm6_choice == "1":
                print("Sub-menu 1 has been selected - Configure Source Analytics Events Service")
                input_source_es()
            elif subm6_choice == "2":
                print("Sub-menu 2 has been selected - Publish Event")
            elif subm6_choice == "3":
                print("Sub-menu 3 has been selected - Create Event Schema..")
                #acc_id = get_account_id()

                #schema_in = input("Enter schema name: ")
                #es_url_in = input("Enter Events Service URL: ")
                #ev_api_key_in = input("Enter Events API key: ")
                #e_api_acc_nm_in = input("Enter Events API Account Name (Global Account Name on License page): ")
                #print("Now it is time to define your schema as a collection of key-value pairs...")

                #inner_loop = True
                #schema_dict = {}
                #while inner_loop:  ## While loop which will keep going until loop = False
                #    choice = input("Enter '1' to add key-type for schema to the list, '0' when you are done: ")
                #    if choice == "0":
                #        inner_loop = False
                #    else:
                #        key = input('Enter Key: ')
                #        data_type = input('Enter data type, options are: integer, float, string, ')
                #        schema_dict[key] = data_type

                #schema_dict_in = schema_dict
                create_event_schema('all_events_custom', es.es_url, es.events_api_key, es.events_api_account_name, 'create_schema.json')
                #create_event_schema(account_id, schema_name, es_url, events_api_key, events_api_account_name, schema_dict)

            elif subm6_choice == "4":
                print("Sub-menu 4 has been selected - Retrieve Event Schema")
                retrieve_event_schema('sample_schema9', es.es_url, es.events_api_key, es.events_api_account_name)
            elif subm6_choice == "5":
                print("Sub-menu 5 has been selected - Update Event Schema")
                update_event_schema('sample_schema9', es.es_url, es.events_api_key, es.events_api_account_name, 'update_schema.json')
            elif subm6_choice == "6":
                print("Sub-menu 6 has been selected - Delete Event Schema")
                delete_event_schema('Correlate_BT_Data', es.es_url, es.events_api_key, es.events_api_account_name)
            elif subm6_choice == "7":
                print("Sub-menu 7 has been selected - Single Query")
            elif subm6_choice == "8":
                print("Sub-menu 8 has been selected - Multi Query JSON")
                query_events_json(es.es_url, es.events_api_key, es.events_api_account_name, 'analytics_multi_query.json')
                #def query_events_json(es_url, events_api_key, events_api_account_name, json_filename)
            elif subm6_choice == "9":
                print("Sub-menu 9 has been selected - publish snapshot, metric, & HR violation events for a given BT to Analytics API")
                publish_all_bt_data_to_es('custom_bt_data', es.es_url, es.events_api_key,es.events_api_account_name)
                #publish_all_bt_data_to_es(schema_name, es_url, events_api_key, events_api_account_name)
    elif choice == "7":
        print("Menu 7 has been selected - RBAC API - *ONLY SUPPORTED FOR 4.4+ Controllers!")
        inner_loop7 = True
        while inner_loop7:
            print_sub_menu_7()
            subm7_choice = input("Enter your choice [0-9]: ")
            if subm7_choice == "0":
                inner_loop7 = False
            elif subm7_choice == "1":
                print("Sub-menu 1 has been selected - Configure Source Controller")
                input_source_controller()
            elif subm7_choice == "2":
                print("Sub-menu 2 has been selected - Create User")
            elif subm7_choice == "3":
                print("Sub-menu 3 has been selected - Get User by ID")
            elif subm7_choice == "4":
                print("Sub-menu 4 has been selected - Get User by Name")
            elif subm7_choice == "5":
                print("Sub-menu 5 has been selected - Get All Users")
                get_all_users()
            elif subm7_choice == "6":
                print("Sub-menu 6 has been selected - Update User")
            elif subm7_choice == "7":
                print("Sub-menu 7 has been selected - Delete User")
            elif subm7_choice == "8":
                print("Sub-menu 8 has been selected - Create Group")
            elif subm7_choice == "9":
                print("Sub-menu 9 has been selected - Get Group by ID")
            elif subm7_choice == "10":
                print("Sub-menu 10 has been selected - Get Group by Name")
            elif subm7_choice == "11":
                print("Sub-menu 11 has been selected - Get All Groups")
            elif subm7_choice == "12":
                print("Sub-menu 12 has been selected - Update Group")
            elif subm7_choice == "13":
                print("Sub-menu 13 has been selected - Delete Group")
            elif subm7_choice == "14":
                print("Sub-menu 14 has been selected - Add User to Group")
            elif subm7_choice == "15":
                print("Sub-menu 15 has been selected - Remove User from Group")
            elif subm7_choice == "16":
                print("Sub-menu 16 has been selected - Create Role")
            elif subm7_choice == "17":
                print("Sub-menu 17 has been selected - Add Role to User")
            elif subm7_choice == "18":
                print("Sub-menu 18 has been selected - Remove Role from User")
            elif subm7_choice == "19":
                print("Sub-menu 19 has been selected - Add Role to Group")
            elif subm7_choice == "20":
                print("Sub-menu 20 has been selected - Remove Role from Group")
            elif subm7_choice == "21":
                print("Sub-menu 21 has been selected - Get Role by ID")
            elif subm7_choice == "22":
                print("Sub-menu 22 has been selected - Get Role by Name")
            elif subm7_choice == "23":
                print("Sub-menu 23 has been selected - Get All Roles")
            elif subm7_choice == "24":
                print("Sub-menu 24 has been selected - Update Role")
            elif subm7_choice == "25":
                print("Sub-menu 25 has been selected - Delete Role")
    elif choice == "8":
        print("Menu 8 has been selected - MISC API")
        inner_loop8 = True
        while inner_loop8:
            print_sub_menu_8()
            subm8_choice = input("Enter your choice [0-9]: ")
            if subm8_choice == "0":
                inner_loop8 = False
            elif subm8_choice == "1":
                print("Sub-menu 1 has been selected - Configure Source Controller")
                input_source_controller()
            elif subm8_choice == "2":
                print("Sub-menu 2 has been selected - ENABLE new BT config 2.0 for selected bus app")
                source_enable_for_app = input("Enter app name:")
                #source_enable_for_app = ''
                enable_new_bt_config(source_enable_for_app)
            elif subm8_choice == "3":
                print("Sub-menu 3 has been selected - DISABLE new BT config 2.0 for selected bus app")
                source_disable_for_app = input("Enter app name:")
                disable_new_bt_config(source_disable_for_app)
            elif subm8_choice == "4":
                print("Sub-menu 4 has been selected - "
                      "Mark all nodes as historical by tier based on no metric data for time frame")
                #source_app = input("Enter app name:")
                #source_tier = input("Enter tier name:")
                delete_dynamic_nodes('pss_dsda', 'storage', '5000')
    else:
        # Any integer inputs other than values 1-5 we print an error message
        input("Wrong option selection. Enter any key to try again..")
