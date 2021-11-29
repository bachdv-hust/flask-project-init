from app.output_api import output
from flask import Blueprint, request, jsonify

# lấy thông tin sản phẩm muốn đổi


@output.route('/payment/exchange_product', methods=['GET'])
def getExchangeProduct():
    null = None
    res = {
    }
    res["status_code"] = 200
    res["data"] = [{
        "product_id": 1,
        "product_name": "Vay"
    },
        {
        "product_id": 2,
        "product_name": "Ao dai"
    },
        {
        "product_id": 3,
        "product_name": "Vay ngan"
    },

    ]
    return jsonify(res)
@output.route('/payment/loyalty_poin', methods=['GET','POST'])
def getLoyalty_poin():
    
    null = None
    res = {
    }
    res["status_code"] = 200
    if request.method == 'POST':
        res["data"] = {
            "point" : 15
        }
    else:
        res["data"] = {
            "point" : 15
        }
    return jsonify(res)
@output.route('/payment/voicher/<id>',methods=['GET'])
def getVoicherDetail(id):
    res = {
    }
    res["status_code"] = 200
    res["data"] ={
        "title" :"Giảm 1 nửa giá sp",
        "id" :1,
    }
    return jsonify(res)

@output.route('/payment/return_product',methods=['GET'])
def getListReturnProduct ():
    pass
