TODO:

- savedataofferstate -> without transport url (error)
- savedataofferstate multiple times -> duplicate key problem


producer.py launchpad1 


1. launchpad controller is listening for any changes on "data offers"
2. hooker is listening for any changes on "data subscriptions"
3. sdm_kafka_agent updates data offer state
4. sdm_ui creates a data offer -> to the data offer state
5. launchpad controller shows new data offer #do1 on row1
6. pressing on the row1 button triggers the creation of a data subscription #ds1 in the logistics API against the data offer #do1
7. hooker is getting updates about the new data subscription #ds1 and starts consuming from the associated topic (through data offer -> data offer state). all data is forwarded to the launchpad controller.
8. pressing on the row1 button deletes the data subscription #ds1 in the logistics API
9. hooker is getting informed about the deletion of the data subscription and stops consuming from all related kafka topics.