# miniProject-backend API Docs
http://group2.exceed19.online
1. get all data : [get] http://group2.exceed19.online/
    - return list of 
        - light_id : int (1-3)
        - status : bool[True: เปิด, False: ปิด]
        - mode : enum[“AUTO”,”MANUAL”,”DISCO”]
        - brightness : int(0-100)
2. get data from light_id :[get]  http://group2.exceed19.online/{id}
      - return
        - light_id : int (1-3)
        - status : bool[True: เปิด, False: ปิด]
        - mode : enum[“AUTO”,”MANUAL”,”DISCO”]
        - brightness : int(0-100)
3. update data : [put] http://group2.exceed19.online/update
      - input JSON object as body
        - light_id : int (1-3)
        - status : bool[True: เปิด, False: ปิด]
        - mode : enum[“AUTO”,”MANUAL”,”DISCO”]
        - brightness : int(0-100)
      - return JSON object
        - success : bool
