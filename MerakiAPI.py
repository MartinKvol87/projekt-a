import meraki 
from tkinter import *
from tkinter import ttk 

##https://developer.cisco.com/meraki/api-v1/#!get-device
API_KEY = "6083248ab12f9bdbe9a4e09bca9b5bcdf79c4a49"
ORG_ID = "629977"

def getMerakiData():
    """
    Laver en forbindelse til Meraki Dashboardet. Vi får adgang via en API key, som vi generated fra Dashboardet
    """
    dashboard = meraki.DashboardAPI(API_KEY)
    networkList = dashboard.organizations.getOrganizationNetworks(ORG_ID, total_pages="all")
    return dashboard.networks.getNetworkClients(networkList[0]["id"], total_pages='all')

def setupGUI(data):
    """
    Laver en GUI, for at visualisere det data, vi vælger at fokusere på.
    """
    screen = Tk()
    screen.title("Meraki GUI")
    screen.resizable(width=0, height=0)

    view = ttk.Treeview(screen, selectmode = 'browse')
    view.pack(side='left', fill='y')
    scrollBar = ttk.Scrollbar(screen, orient='vertical', command=view.yview)
    scrollBar.pack(side='right', fill='y')
    view.configure(yscrollcommand=scrollBar.set)

    view['columns']= ('id', 'IP', 'Status', 'Sent by client', 'Received by client')
    view.column("#0", width=0,  stretch=NO)
    view.column("id",anchor=CENTER, width=80)
    view.column("IP",anchor=CENTER, width=100)
    view.column("Status",anchor=CENTER, width=80)
    view.column("Sent by client",anchor=CENTER, width=80)
    view.column("Received by client",anchor=CENTER, width=120)

    view.heading("#0",text="",anchor=CENTER)
    view.heading("id",text="ID",anchor=CENTER)
    view.heading("IP",text="IP",anchor=CENTER)
    view.heading("Status",text="Status",anchor=CENTER)
    view.heading("Sent by client",text="Sent by client",anchor=CENTER)
    view.heading("Received by client",text="Received by client",anchor=CENTER)


    for i, client in enumerate(data):
        print(client)
        view.insert(parent='',index='end',iid=i,text='',
            values=(client['id'], client['ip'], client['status'], client['usage']['sent'], client['usage']['recv']))

    screen.mainloop()


def main():
    merakiData = getMerakiData()
    setupGUI(merakiData)

main()
