from app.output_api import output
from flask import Blueprint, request, jsonify

@output.route('/report/feedback')
def getMessageFeedBack() :
    res ={}
    res["status_code"] = 200
    res["data"] =[
        {
            "from_user_id" :13,
            "type" :"lỗi giao diện",
           "mess" :  "Giao diện khó dùng quá admin ơi"
        },
        {
            "from_user_id" :13,
            "type" :"lỗi giao diện",
           "mess" :  "Giao diện khó dùng quá admin ơi"
        },
        {
            "from_user_id" :13,
            "type" :"lỗi giao diện",
           "mess" :  "Giao diện khó dùng quá admin ơi"
        },
    ]
    return jsonify(res) 