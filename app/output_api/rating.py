from app.output_api import output
from flask import Blueprint, request, jsonify


@output.route('/rating/<id>', methods=['GET'])
def getRatingWithID(id):
    null = None
    res = {
    }
    res["status_code"] = 200
    res["data"] = [{
        "average": 5,
        "title": "Rất hài lòng",
        "message": "Sản phẩm chính hãng, đúng mô tả. Đóng gói cẩn thận. Giao hàng hơi lâu do dịch bệnh nhưng vẫn chấp nhận được. Hài lòng. Sẽ ủng hộ tiếp trong những lần sau.",
        "image": ["Ford", "BMW", "Fiat"]
    },
        {
        "average": 5,
        "title": "Rất hài lòng",
        "message": "Sản phẩm chính hãng, đúng mô tả. Đóng gói cẩn thận. Giao hàng hơi lâu do dịch bệnh nhưng vẫn chấp nhận được. Hài lòng. Sẽ ủng hộ tiếp trong những lần sau.",
        "image": ["Ford", "BMW", "Fiat"]
    },
    ]
    return jsonify(res)
