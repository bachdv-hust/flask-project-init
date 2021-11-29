from app.output_api import output
from flask import Blueprint, request, jsonify

@output.route('/shiping',methods =['GET'])
def getShipping() :
    return "hello" 