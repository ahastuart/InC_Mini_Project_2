import os
from flask import Flask, request
import pymysql.cursors
from dbconn.DBconn import *
from werkzeug.utils import secure_filename

path = os.getcwd()
UPLOAD_FOLDER = path+'/static/assets/img/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# def util_file_upload_service(file):
#     f = file
#     if f and allowed_file(f.filename):
#         filename = secure_filename(f.filename)
#         f.save(os.path.join(UPLOAD_FOLDER, filename))
#         return filename
#     else:
#         return 0
    
def util_comment_list_service(BRD_NO,BRD_TYPE):
    
    cursor = dbconn.get_db().cursor(pymysql.cursors.DictCursor)
    
    try:
        sql = '''
            SELECT 
                BRD_CMNT_NO,
                BRD_CMNT_CTNT,
                REGID,
                REGDT
            FROM board_comment 
            where DEL_FLAG = 'N' AND BRD_TYPE = %s AND
            BRD_NO = %s            
            order by BRD_NO desc ;
        '''
        cursor.execute(sql,(BRD_TYPE,BRD_NO))
        result = cursor.fetchall()
        
    finally:
        dbconn.get_db().close()
    return result