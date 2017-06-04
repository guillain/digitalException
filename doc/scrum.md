# Scrum

## People
* Product Owner: Guillain
* Scrum Master: Bernard

Squad:
* SEAP Hyper Collaboration: Guillaume
* ShellBot: Bernard
* Commercial: Sandrine
* Cisco Spark: Guillain

## Stories
1/ When button is triggered Cisco Spark space is created
* Days: 3
* Priority: high
* Demo: Button is triggered, SEAP catch the signal and data and submit the event and its context to Bot. Bot creates the Cisco Spark space and associates the Stress Engineer.
* Schema: Button -> SEAP -> Bot -> Space(membership)
* Statu: Todo
* Sprint: 1

2/ Ask the Shop floor to enter information
* Days: 1
* Priority: Medium
* Demo: Bot ask the Shop floor people to enter part number et picture of the issue. Bot must continue to ask or remember it until the acknowledgement of each information.
* Schema: Bot -> Space(Shop Floor) -> Bot
* Statu: Ongoing
* Sprint: 1

3/ People are engaged over mobile
* Days: 1
* Priority: Medium
* Demo: People can communicate and can use modern support as picture, audio, video, white board, web conferencing and file sharing.
* Schema: User -> Space
* Statu: Done
* Sprint: 1

4/ Stress Engineer can request escalation to the Design Engineer
* Days: 1
* Priority: Medium
* Demo: Stress Engineer can ask by chat with the bot and at any time the support of Design Engineer.
* Schema: Space(Stress Engineer) -> Bot -> Space(Design Engineer)
* Statu: Done
* Sprint: 1
	
5/ The information exchanged in the space are duplicated in realteam in SAP
* Days: 3
* Priority: Medium
* Demo: Text chat and file are duplicated in SAP via SEAP. Events are also reported. Miroring feature can be suspended during 1minute by Stress or Field Engineer's request.
* Schema: Space(Text/File) -> Bot -> SEAP -> SAP
* Statu: ToDo
* Sprint: 2

6/ Stress Engineer close the folder
* Days: 2
* Priority: Medium
* Demo: When issue is solved the Stress Engineer (only) can close the folder via chatbot request. When this action is requested the Space is closed and SEAP is updated.
* Schema: Space(Stress Engineer) -> Bot -> SEAP
* Statu: ToDo
* Sprint: 2

7/ Shop Floor consults SAP documents/references
* Days: 3
* Priority: Low
* Demo: Shop Floor consults documents and references located in SAP
* Schema: Space(Shop Floor) -> Bot -> SEAP -> SAP -> SEAP -> Bot -> sapce-Shop Floor)
* Statu: ToDo
* Sprint:

8/ The escalation is speed up by SMS/call
* Days: 3
* Priority: Low
* Demo: After have raised escalation and (minutes delay done, SMS and call featuer are activated to contact the SPOC.
* Schema: Space(Stress Engineer) -> Bot -> Twilio(SPOC)
* Statu: ToDo
* Sprint:

9/ Identity of Shop Flor is known by the Space

* Days: 3
* Priority: Low
* Demo: When button is pressed by the Shop Flor, the user is identified by SAP via the user's planning and affectation.
* Schema: Button -> SEAP -> SAP -> SEAP -> Bot -> Space(User)
* Statu: ToDo
* Sprint:

10/ IoT flot is managed by SEAP Hyper Collaboration

* Days: 3
* Priority: Medium
* Demo: IoT devices are properly registered and managed by SEAP Hyper Collaboration. Reports and audit features provide overview on the infrastructure.
* Schema:
* Statu: ToDo
* Sprint: 3

11/ Part number is identified and specific information related to the piece is provided in the space

* Days: 3
* Priority: Low
* Demo: After that the Shop Floor has provided the part number, SEAP search the product and its documents/references and provide the usefull info to the Space.
* Schema: Space(part number) -> Bot -> SEAP -> SAP -> SEAP -> Bot -> Space(product info)
* Statu: ToDo
* Sprint:

12/ Dashboard real time report

* Days: 2
* Priority: Low
* Demo: Provide real time dashboard of the solution
* Schema: Bot/SEAP -> Web
* Statu: ToDo, Ongoing, Done
* Sprint: 4

13/ Audio/video records

* Days: 9
* Priority: Low
* Demo: Enable audio and video records for the audio/video communications done with the space.
* Schema: Space(audio/video) -> Record
* Statu: ToDo
* Sprint:

14/ Images define as calque and superposed

* Days: 8
* Priority: Low
* Demo: Picture/Screenshot and documents/references are superposed to hiligh the default of the piece.
* Schema:
* Statu: ToDo
* Sprint:

15/ Analytics report available for the product
* Days: 3
* Priority: Low
* Demo: Reports are generated to provide Space, Bot and SEAP usages
* Schema:
* Statu: ToDo
* Sprint:

16/ Trends report available for the product and the factory
* Days: 3
* Priority: Low
* Demo: Reports are generated to provide product and factory trends. This must highlight the benefist of the continuous engagement system.
* Schema:
* Statu: ToDo
* Sprint:

17/ Pieces are tracked
* Days: 8
* Priority: Low
* Demo: Each pieces are tracked by geolocalisation chipset. SEAP Hyper Collaboration is used to provide global overview and pieces follow up/tracking.
* Schema: IoT(Piece) -> SEAP
* Statu: ToDo, Ongoing, Done
* Sprint:

18/ Space identified which is the faulty piece and provide report on its
* Days: 3
* Priority: Low
* Demo: After have pushed the button SEAP identified which piece is the faulty one and provide its report (geolocalisation and timestamp to corelate to the factory planning) in the space
* Schema: Button -> SEAP -> Bot -> Space(piece's history)
* Statu: ToDo
* Sprint:

19/ Factory bottleneck reports
* Days: 3
* Priority: Low
* Demo: Analytic feature provides trends and reports on faults and bottleneck
* Schema:
* Statu: ToDo
* Sprint:
	
20/ Bot scenario creation with SEAP
* Days: 1
* Priority: Low
* Demo: Create new bot scenario with SEAP
* Schema:
* Statu: ToDo
* Sprint:
	
21/ Bot scenario update with SEAP
* Days: 1
* Priority: Low
* Demo: Update bot scenario with SEAP
* Schema:
* Statu: ToDo
* Sprint:
